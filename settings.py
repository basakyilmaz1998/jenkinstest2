import os


class SettingKeys:
    DB_HOST = os.getenv("DB_HOST", "host.docker.internal")  # host.docker.internal -> host makine
    DB_PORT = int(os.getenv("DB_PORT", 3307))               # host'taki MySQL portu
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
    DB_DATABASE = os.getenv("DB_DATABASE", "bootcampDB")


class Settings:
    def __init__(self):
        self.db_host = SettingKeys.DB_HOST
        self.db_port = SettingKeys.DB_PORT
        self.db_user = SettingKeys.DB_USER
        self.db_password = SettingKeys.DB_PASSWORD
        self.db_database = SettingKeys.DB_DATABASE
