# to reduce repetation of data, we will save the changable data in config.ini file and
# to read those data in our testcases we need utilities file to call those data
# So whatever the data we will add in config.ini, we need to creat its corresponding code in utility to fetch it.

# Read common value from ini

import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class readconfig():

    @staticmethod
    def getURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getuseremail():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getuserpassword():
        password = config.get('common info','password')
        return password