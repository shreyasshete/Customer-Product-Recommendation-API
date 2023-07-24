from configparser import ConfigParser
from app.utils import config
import mysql.connector

# Connect to DB
def connect_to_database():
    # Establish a connection to the MySQL database
    # config = ConfigParser(interpolation=None)
    # config.read("app\config.ini")
    # dict_DB = get_dbDetails()


    #Connect to DB using details provided in config file
    connection = mysql.connector.connect(
        host=config.host,
        user = config.userID,
        password = config.password,
        database = config.databaseName
        # host=config['dbDetails']['Host'],
        # user=config['dbDetails']['User ID'],
        # password=config['dbDetails']['Password'],
        # database=config['dbDetails']['Database Name']
    )
    return connection

# Executing Query
def execute_query(connection, query):
    # Execute a SQL query on the database using the provided connection
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

