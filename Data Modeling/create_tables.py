import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries



def create_database():
    """
    Creates the database and connects to it
    Returns: the connection and cursor to the created database (sparkifydb)
    """

    # connect to default database
    config = configparser.ConfigParser()
    config.read('db.cfg')
    conn = psycopg2.connect("host={} dbname={} user={} password={}".format(*config['CLUSTER'].values()))    
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to sparkify database
    # conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=postgres password=admin"
    )

    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    The function
    - Drops (if exists) and creates the sparkify database.
    - Establishes connection with the sparkify database and gets
    cursor to it.
    - Drops all the tables.
    - Creates all tables needed.
    - Finally, closes the connection.
    """
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
