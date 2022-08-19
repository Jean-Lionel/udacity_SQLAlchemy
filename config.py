import psycopg2
import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
#SQLALCHEMY_DATABASE_URI= '<Put your local database url>'


DB_NAME = "exemple"
DB_USER = "postgres"
DB_PASS = "lion"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    SQLALCHEMY_DATABASE_URI = psycopg2.connect(database=DB_NAME,
                                               user=DB_USER,
                                               password=DB_PASS,
                                               host=DB_HOST,
                                               port=DB_PORT)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    print("Database connected successfully")
except:
    print("Database not connected successfully")
