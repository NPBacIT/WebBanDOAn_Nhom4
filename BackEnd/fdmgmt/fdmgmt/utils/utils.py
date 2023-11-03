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

    def get_column_names(self, table_name):
        try:
            self.curs.execute('SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME=\'%s\';' %table_name)
            column_names = self.curs.fetchall()
            return [column[0] for column in column_names]
        except Exception as e:
            LOG.error('Cannot get column names from tables: %s' %e)
        return None

    def get_all_items(self, table_name):
        try:
            LOG.debug('Getting all items from %s' %table_name)
            self.curs.execute('SELECT * FROM %s' %table_name)
            items = self.curs.fetchall()

            result = []
            column_names = self.get_column_names(table_name)
            for item in items:
                item_dict = {}
                for i, value in enumerate(item):
                    item_dict[column_names[i]] = value
                result.append(item_dict)
            return result
        except Exception as e:
            LOG.error('Get all items failed, something went wrong: %s' %e)

    def get_item(self, table_name, item_key, item_value):
        try:
            LOG.debug('Getting item from %s' %table_name)
            self.curs.execute('SELECT * FROM %s WHERE %s=%s' %(table_name, item_key, item_value))
            item = self.curs.fetchone()
            
            if not item:
                return None
            else:
                column_names = self.get_column_names(table_name)
                item_dict = {}
            
                for i, value in enumerate(item):
                    item_dict[column_names[i]] = value
                return item_dict
        except Exception as e:
            LOG.error('Get items failed: %s' %e)

    def create_record(self, table_name, item):
        column_names = self.get_column_names(table_name)
        
        for key in item.keys():
            if key not in column_names:
                raise ValueError(f'Column "{key}" does not exist in the table.')
        
        columns_name = ', '.join(item.keys())
        vals = tuple(data_to_insert.values())
        query = f"INSERT INTO %s (%s) VALUES %s" %(table_name, columns_name, vals)
        print(query)
        self.curs.execute(query)
#        self.db_connection.commit()

    def update_record(self, table_name, record_id, data):
        set_values = ", ".join([f'{key} = ?' for key in data.keys()])
        query = f'UPDATE {table_name} SET {set_values} WHERE id = ?'
        self.cursor.execute(query, list(data.values()) + [record_id])
        self.db_connection.commit()

    def delete_item(self, table_name, item_key, item_value):
        try:
            LOG.warning('Starting to delete items')
            self.cursor.execute('DELETE FROM %s WHERE %s=%s' %(table_name, item_key, item_value))
            self.db_connection.commit()
        except Exception as e:
            LOG.error('Deleted failed: %s' %e)
