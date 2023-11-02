from fdmgmt.common import conf as cfg
from fdmgmt.common import log as logging

from fdmgmt.utils import connector
CONF = cfg.CONF
LOG = logging.getLogger(__name__)

class DatabaseUtils(connector.Connector):
    
    def __init__(self):
        super(DatabaseUtils, self).__init__(
            driver = CONF['mssql']['driver'],
            server = CONF['mssql']['server'],
            port = CONF['mssql']['port'],
            database = CONF['mssql']['database'],
            username = CONF['mssql']['username'],
            password = CONF['mssql']['password'])

    def create_record(self, table_name, data):
        query = f'INSERT INTO {table_name} ({", ".join(data.keys())}) VALUES ({", ".join(["?"] * len(data))})'
        self.cursor.execute(query, list(data.values()))
        self.db_connection.commit()

    def get_all_items(self, table_name):
        self.curs.execute('SELECT * FROM %s' %table_name)
        items = self.curs.fetchall()

        result = []
        column_names = [column[0] for column in self.curs.description]
        for item in items:
            item_dict = {}
            for i, value in enumerate(item):
                item_dict[column_names[i]] = value
            result.append(item_dict)
        return result

    def get_item(self, table_name, item_id):
        self.curs.execute('SELECT * FROM {table_name} WHERE  = ?', item_id)
        item = self.curs.fetchone()

        if not item:
            return None
        else:
            column_names = [column[0] for column in self.curs.description]
            item_dict = {}
            
            for i, value in enumerate(item):
                item_dict[column_names[i]] = value
            return item_dict

    def update_record(self, table_name, record_id, data):
        set_values = ", ".join([f'{key} = ?' for key in data.keys()])
        query = f'UPDATE {table_name} SET {set_values} WHERE id = ?'
        self.cursor.execute(query, list(data.values()) + [record_id])
        self.db_connection.commit()

    def delete_record(self, table_name, record_id):
        self.cursor.execute(f'DELETE FROM {table_name} WHERE id = ?', record_id)
        self.db_connection.commit() 
