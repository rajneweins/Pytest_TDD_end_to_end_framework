import pyodbc
import pandas as pd
from test.utils.cluster_utils import Cluster


class DatabricksDBUtils(Cluster):
    def __init__(self, workspace_url, api_token, cluster_id):
        super().__init__(workspace_url, api_token, cluster_id)
        self.connection = None
        self.ssl_mode = None
        self.http_path = None
        self.ssl_ca = None
        self.ThriftTransport = None
        self.password = None
        self.username = None
        self.AuthMech = None
        self.SparkServerType = None
        self.schema = None
        self.port = None
        self.server_hostname = None
        self.driver = None

    def conn_param(self, server_hostname, http_path, username, password, driver, port, ssl_ca):
        self.driver = driver
        self.server_hostname = server_hostname
        self.port = port
        self.schema = 'default'
        self.SparkServerType = 3
        self.AuthMech = 3
        self.username = username
        self.password = password
        self.ThriftTransport = 2
        self.ssl_ca = ssl_ca
        self.ssl_mode = 1
        self.http_path = http_path

    def connect(self):
        connection_string = (
            f'Driver={self.driver};'
            f'HOST={self.server_hostname};'
            f'PORT={self.port};'
            f'Schema={self.schema};'
            f'SparkServerType={self.SparkServerType};'
            f'AuthMech={self.AuthMech};'
            f'UID={self.username};'
            f'PWD={self.password};'
            f'ThriftTransport={self.ThriftTransport};'
            f'SSL={self.ssl_mode};'
            f'HTTPPath={self.http_path};'
        )

        if self.ssl_mode == 1 and self.ssl_ca:
            connection_string += f'SSLCA={self.ssl_ca};'

        self.connection = pyodbc.connect(connection_string, autocommit=True)

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def fetch_data_as_dataframe(self, query):
        if not self.connection:
            raise Exception("Connection not established. Call 'connect()' first.")

        return pd.read_sql(query, self.connection)

    def fetch_data(self, query):
        if not self.connection:
            raise Exception("Connection not established. Call 'connect()' first.")

        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def truncate_table(self, query):
        if not self.connection:
            raise Exception("Connection not established. Call 'connect()' first.")

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            cursor.close()
            self.connection.commit()
            return True
        except Exception as e:
            return str(e)
