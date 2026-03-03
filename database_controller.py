import pymysql

from settings import SettingKeys, Settings


def connect():
    return pymysql.connect(
        host=SettingKeys.DB_HOST,
        user=SettingKeys.DB_USER,
        password=SettingKeys.DB_PASSWORD,
        database=SettingKeys.DB_DATABASE
    )


class Database:
    def __init__(self):
        self.settings = Settings()


class DataBaseController(Database):
    def __init__(self):
        Database.__init__(self)

    @staticmethod
    def insert_data(data=""):
        db = connect()
        cursor = db.cursor()
        query = "INSERT INTO bootcampDB.case_reports (case_status) VALUES ('{}')".format(data)
        cursor.execute(query)
        db.commit()
        db.close()
