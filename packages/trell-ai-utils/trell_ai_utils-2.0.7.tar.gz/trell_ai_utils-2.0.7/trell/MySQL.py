import logging
import sqlalchemy 
import pandas as pd
from trell import aws
import mysql.connector

# from trell.utils import LogFormatter
# LogFormatter.apply()
 
class MySQL:

    """MySQL database utility functions"""

    @staticmethod
    def get_data(query, db_string):

        """
        Fetch data from mysql as a dataframe.
        :param string query: query for fetching data from table
        :param string db_string: mysql database connection string
        :return pd.DataFrame data
        """

        connection = sqlalchemy.create_engine(db_string)
        try:
            data = pd.read_sql(query + " ;", connection)
            return data
        except Exception as err:
            logging.error(err)
        finally:
            connection.dispose()

    @staticmethod
    def execute_query(query, db_string):

        """
        Execute a query in the mysql table
        :param string query: query for execution in the table
        :param string db_string: mysql database connection string
        :return None
        """

        connection = sqlalchemy.create_engine(db_string)
        try:
            connection.execute(query)
        except Exception as err:
            logging.error(err)
        finally:
            connection.dispose()

    @staticmethod
    def dump_data(data, table_name, db_string, mode="append"):

        """
        Execute a query in the mysql table
        :param string query: query for execution in the table
        :param string table_name: name of the the target table
        :param string db_string: mysql database connection string
        :param string mode: it can be either replace or append
        :return None
        """

        connection = sqlalchemy.create_engine(db_string)
        try:
            data.to_sql(name=table_name, con=connection, if_exists=mode, index=False)
        except Exception as err:
            logging.error(err)
        finally:
            connection.dispose()

    @staticmethod
    def get_prod_data_from_local(query):

        """
        Fetch data from production mysql from local machine via SSH tunnelling (or local port forwarding).
        :param string query: query for execution in the table
        :param string table_name: name of the the target table
        :param string db_string: mysql database connection string
        :param string mode: it can be either replace or append
        :return None
        """

        connection = mysql.connector.connect(user=aws.cred['DATA_USER'],
                                            password=aws.cred['DATA_PWD'],
                                            host="127.0.0.1",
                                            port=aws.cred['PORT_1'],
                                            database="trellDb")
        
        connection = sqlalchemy.create_engine(aws.cred['LOCAL_PROD_DB_CONNECTION_STRING'])
        try:
            df = pd.read_sql(query + " ;", connection)
            print("done")
        except Exception as err:
            logging.error(err)
        finally:
            # connection.close()       # for mysql.connector
            connection.dispose()   # for sqlalchemy

    @staticmethod
    def get_prod_data(query):

        """
        Fetch data from production mysql as a dataframe.
        :param string query: query for fetching data from table
        :param string db_string: mysql database connection string
        :return pd.DataFrame data
        """

        connection = sqlalchemy.create_engine(aws.cred['DATA_PROD_DB_CONNECTION_STRING'])
        try:
            return pd.read_sql(query + " ;", connection)
        except Exception as err:
            logging.error(err)
        finally:
            connection.dispose()

    @staticmethod
    def execute_query_in_prod(query):

        """
        Execute a query in the production mysql table
        :param string query: query for execution in the table
        :param string db_string: mysql database connection string
        :return None
        """


        connection = sqlalchemy.create_engine(aws.cred['DATA_PROD_DB_CONNECTION_STRING'])
        try:
            connection.execute(query)
        except Exception as err:
            logging.error(err)
        finally:
            connection.dispose()

    @staticmethod
    def dump_into_prod(data, table_name, mode="append"):

        """
        Execute a query in the production mysql table
        :param string query: query for execution in the table
        :param string table_name: name of the the target table
        :param string db_string: mysql database connection string
        :param string mode: it can be either replace or append
        :return None
        """

        connection = sqlalchemy.create_engine(aws.cred['DATA_PROD_DB_CONNECTION_STRING'])
        try:
            data.to_sql(name=table_name, con=connection, if_exists=mode, index=False)
        except Exception as err:
            logging.error(err)
        finally:
            connection.dispose()

