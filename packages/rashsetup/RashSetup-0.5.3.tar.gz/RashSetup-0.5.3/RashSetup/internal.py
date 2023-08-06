import importlib
import sys
import subprocess
import sqlite3
import pathlib
import shutil
import logging
import typing
from crawlers import *

__all__ = ["pipInstall", "ModuleManager"]

__all__.extend(ALL)


def pipInstall(packages: typing.List[str]):
    subprocess.run([sys.executable, "-m", "pip", "install", *packages])


class ModulePathManager:
    def __init__(self):
        self.mod = pathlib.Path(__file__).parent / "__RashModules__"
        self.mod.mkdir(exist_ok=True)

        _ = self.mod / "__init__.py"
        None if _.exists() else _.write_text("")

    def check_module(self, name):
        return all(
            (
                (self.mod / name).exists(),
                (self.mod / name / "__init__.py").exists(),
                (self.mod / name / "settings.json").exists(),
            )
        )

    def uninstall_module(self, name):
        shutil.rmtree(self.mod / name)

    def gen_path(self, name):
        mod = self.mod / name
        mod.mkdir(exist_ok=True)
        return self.mod / name

    def settings(self, module):
        return SettingsParser(self.gen_path(module) / "settings.json", True)


class DBManager(ModulePathManager):
    def __init__(self):
        super().__init__()
        self.sql = self.mod.parent / "__RashSQL__.sql"
        self.connector = sqlite3.connect(
            self.mod / "__RashModules__.db", check_same_thread=False
        )

        self.__start()

    def cursor(self):
        return self.connector.cursor()

    def __start(self):
        temp = self.cursor()
        temp.executescript(self.sql.read_text())
        self.connector.commit()

    def sql_code(self, code, *args) -> tuple:
        return self.execute_one_line(
            *self.execute_one_line(
                "SELECT SQL, Empty FROM Sql WHERE Hash = ?", False, code
            ),
            *args
        )

    def execute_one_line(self, script, all_=False, *args):
        temp = self.cursor()
        temp.execute(script, args)

        return temp.fetchall() if all_ else temp.fetchone()

    def commit(self):
        self.connector.commit()

    def close(self):
        self.connector.close()

    def downloaded(self, name, hosted, version, readme):
        self.sql_code(10, name, hosted, version, readme)

        self.commit()

    def update_settings(self, name, version, readme=None):
        self.sql_code(8, version, name)

        self.sql_code(9, readme, name) if readme else None

        self.commit()


class HeavyModuleManager(DBManager):
    def download(self, name: str, url: typing.Optional[str] = None, _=None):
        url = url if url else self.sql_code(3, name)[0]
        path = str(self.gen_path(name))

        setup = RawSetup(RepoSetup, url, path)
        setup.process.start()
        setup.process.join()

        return setup.parse()

    def grab_readme(self, url):
        setup = RawSetup(READMESetup, url)
        setup.process.start()
        setup.process.join()

        status, result = setup.parse()

        if not status:
            return ""

        return result

    def check_for_update(self, *args, **_):
        pass

    def update_settings(self, settings: SettingsParser, *_) -> None:
        return super().update_settings(
            settings.name(), settings.version(), settings.readme()
        )


class ModuleManager(HeavyModuleManager):
    def __init__(self):
        super().__init__()
        self.linkers = {}

    def check(self):
        for module in self.sql_code(5):
            module: str = module[0]

            if self.check_module(module):
                continue

            yield module


class RashRawSetup(ModuleManager):
    def __init__(self):
        super().__init__()
        self.root = format_root()

    def setup(self, module):
        self.root.info("Downloading Missing default Module %s", module)

        status, result = self.download(module)
        assert status, result

        self.root.debug("Downloaded %s, updating details to database", module)
        settings = self.settings(module)

        temp = self.grab_readme(settings.readme())
        settings.update_readme(temp) if temp else None

        self.update_settings(settings)

    def block(self):
        self.root.critical(
            "Failed to start Rash because of the above exception. Please try again."
        )
        self.root.info(
            "If you find this unreasonable, please raise an issue at: https://github.com/RahulARanger/RashSetup"
        )

        while True:
            pass

    def start(self):
        self.root.info("Starting RashSetup!")

        passed = True
        for module in self.check():
            try:
                self.setup(module)
            except Exception as _:
                self.root.exception("Failed to Download %s", module, exc_info=True)
                passed = False
                break

        None if passed else self.block()


class RashSetup(DBManager):
    def start(self):
        self.process() if self.check() else None

        import RashSetup.__RashModules__.Rash.Start
        sys.exit(0)

    def check(self):
        for module in self.sql_code(6):
            if not self.check_module(module[0]):
                return True

        return False

    @staticmethod
    def process():
        skip_code = """
import RashSetup.internal
process = RashRawSetup()
process.start()    
    """
        return subprocess.run([
            sys.executable, '-c', skip_code
        ], creationflags=subprocess.CREATE_NEW_CONSOLE)  # TODO: see more options

    def clean(self):
        ...  # TODO: clean all current cache

