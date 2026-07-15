from config.config_reader import ConfigReader

conf_read = ConfigReader()
print(conf_read.get("qa", "base_url"))
print(conf_read.get("timeout"))