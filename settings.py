import os


class SettingKeys:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "Sananabanana.1")
    DB_DATABASE = os.getenv("DB_DATABASE", "roadmapDB")


class Settings:
    def __init__(self):
        self.db_host = SettingKeys.DB_HOST
        self.db_user = SettingKeys.DB_USER
        self.db_password = SettingKeys.DB_PASSWORD
        self.db_database = SettingKeys.DB_DATABASE
