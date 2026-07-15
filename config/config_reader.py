import yaml
from pathlib import Path

class ConfigReader:

    _instance = None
    
    # new() is used instead of init() bcoz we are using singleton and memory needs to be created    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            config_path = Path(__file__).parent / "config.yaml"
            with open(config_path, "r") as file:
                cls._instance.config = yaml.safe_load(file)
        return cls._instance
    
    # this will replace n no: of methods to get each parameter mentioned in the yaml file. Later in case if any 
    # configuration is added, we need not write any of the additional method for the same
    def get(self, *keys):
        value = self.config
        for key in keys:
            value = value[key]
        return value