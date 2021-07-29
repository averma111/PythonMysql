# Python program to connect to mysql using

# Importing packages
from configparser import ConfigParser


# Function to create the database object
def read_db_config(filename='config.ini', section='mysql'):
    # Create the parser and read the ini file

    parser = ConfigParser()
    parser.read(filename)

    # Get section and default to mysql
    database = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            database[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return database
