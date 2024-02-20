import sqlite3
from sqlite3 import Error
from dotenv import load_dotenv
import os

from typing import Dict, List

def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """

    load_dotenv()
    PROJECT_PATH = os.getenv('PROJECT_PATH')

    db_file = PROJECT_PATH + r"\backend\db.sqlite3"

    conn = None
    try:

        conn = sqlite3.connect(db_file)

    except Error as e:

        print(e)

    return conn


def get_table_column_names(database_table):
    conn = create_connection()

    with conn:

        cursor = conn.cursor()

        query = "PRAGMA table_info({})".format(database_table)

        cursor.execute(query)

        column_data = cursor.fetchall()

    column_names = [column[1] for column in column_data]

    return column_names


def check_if_record_exists(config, database_table):

    # compare config data to database data

    # Gets the name of the columns in the input table
    table_columns = get_table_column_names(database_table)

    where_clause = ["""{} = '{}'""".format(column_name, config[column_name]) for column_name in table_columns if column_name != "id"]

    where_clause = " AND ".join(where_clause)

    query = """SELECT id FROM {} WHERE {};""".format(database_table, where_clause)

    conn = create_connection()
    with conn:
        cur = conn.cursor()

        cur.execute(query)

        response = cur.fetchall()

    
    if response == []:
        return upload_record(config, database_table)

    else:
        return response[0][0]


def upload_record(record: Dict, database_table):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    conn = create_connection()

    table_columns = get_table_column_names(database_table)

    with conn:

        # tasks
        #record = ('test_model', "test_seed", "test_samp", "test-denoise", 'cfg', 'sca', 'upscale')
        insert_values = [record[column_name] for column_name in table_columns if column_name != "id"]

        insert_fields = ",".join(table_columns[1:])

        field_quantity = "?,"*(len(table_columns) - 1)

        query = ''' INSERT INTO {}({})
                VALUES({}) '''.format(database_table, insert_fields, field_quantity[:-1])

        cur = conn.cursor()

        cur.execute(query, insert_values)

        conn.commit()

        print(cur.lastrowid)

        return cur.lastrowid


# upload_record("", "image_api_imageconfigs")
txt2img_settings = {
    "seed": "test_seed",
    "sampler": "test_samp",
    'sampler_steps': "test",
    "cfg_scale": "cfg",
    "denoising_strength": "test-denoise",
    "hr_scale": "1234",
    "hr_upscaler": '4326346',
    "model": "234325"
}

# upload_record(txt2img_settings, "image_api_imageconfigs")
#print(check_if_record_exists(txt2img_settings, "image_api_imageconfigs"))