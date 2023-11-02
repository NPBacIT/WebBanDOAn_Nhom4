import pyodbc
from fdmgmt.common import conf as cfg
from fdmgmt.common import log as logging

CONF = cfg.CONF
LOG = logging.getLogger(__name__)

class Connector(object):

    def __init__(self, driver, server, port,
                database, username, password):
        self.driver = driver 
        self.server = server
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.conn, self.curs = self.create_connection()
    
    def create_connection(self):
        connection_string = 'DRIVER={%(driver)s};SERVER=%(server)s,%(port)s;DATABASE=%(database)s;UID=%(username)s;PWD=%(password)s;' %{
                'driver': self.driver,
                'server': self.server,
                'port': self.port,
                'database': self.database,
                'username': self.username,
                'password': self.password
        }
        try:
            conn = pyodbc.connect(connection_string)
            if conn:
                curs = conn.cursor()
                return conn, curs 
        except Exception as e:
            LOG.error('Cannot not connect to sql server: %s' %e)
