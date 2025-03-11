import sqlite3
from passlib.context import CryptContext
from random import randint

pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
                          default="pbkdf2_sha256",
                          pbkdf2_sha256__default_rounds=30000)

def encrypt_password(user_password):
    return pwd_config.hash(user_password)

def check_password(hashed_password, user_password):
    return pwd_config.verify(user_password, hashed_password)

def random_days():
    return randint(2,12)

class DatabaseManager:
    def __init__(self, name: str):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def close(self):
        self.connection.close()


    def run_save(self,query):
        self.cursor.execute(query)
        self.connection.commit()




