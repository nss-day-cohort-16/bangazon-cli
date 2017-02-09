# import sqlite3

class Payment():

    def __init__(self, payment_type, account_number, full_name):
        self.__payment_type = payment_type
        self.__account_number = account_number
        self.__full_name = full_name

    def get_payment_type(self):
        return self.__payment_type

    def get_account_number(self):
        return self.__account_number

    def get_full_name(self):
        return self.__full_name





