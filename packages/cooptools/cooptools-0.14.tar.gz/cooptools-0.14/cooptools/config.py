from configparser import ConfigParser
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class ConfigStateException(Exception):
    def __init__(self, txt: str = None):
        logging.error(txt)
        super().__init__(txt)

class ConfigStateFactory:

    def __init__(self, config_file_path: str = None):

        self.parser = ConfigParser()
        self.current_file_path = config_file_path
        self.loaded = False
        self._try_load_pass(config_file_path)

    def _try_load_pass(self, config_file_path:str):
        try:
            self.load(config_file_path=config_file_path)
        except:
            pass

    def _config_file_exists(self):
        return os.path.isfile(self.current_file_path)

    def load(self, config_file_path: str = None):
        if config_file_path is not None:
            self.current_file_path = config_file_path

        if not self._config_file_exists():
            issue = f"Unable to load config from directory: \"{self.current_file_path}\" does not exist"
            raise ConfigStateException(issue)

        try:
            self.parser.read(self.current_file_path)
            logger.info(f"Config set from directory: {self.current_file_path}")
            self.loaded = True
        except Exception as e:
            issue = f"Unable to load config from directory: {self.current_file_path}" \
                    f"\n{e}"
            raise ConfigStateException(issue) from e

    def _try_access_parser_default(self, header, name, default):
        if self.loaded:
            try:
                return self.parser.get(header, name)
            except Exception as e:

                raise ConfigStateException(str(e)) from e
        else:
            return default

    def get_config(self, header, name, default):
        val = self._try_access_parser_default(header, name, default)
        logger.debug(f"Value for {header}|{name}: {val}")
        return val

if __name__ == "__main__":
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter('%(name)s : %(asctime)s : [%(levelname)s] %(message)s (%(filename)s lineno: %(lineno)d)'))
    logger.addHandler(console)

    for ii in range(30):
        logger.info("Hello")
