import json

from fdmgmt.db import models
from fdmgmt.db import database as db
from fdmgmt.utils import mapping
from fdmgmt.common import log as logging

LOG = logging.getLogger(__name__)

class DatabaseUtils(db.DatabaseConnector):
    
    def __init__(self):
        super(DatabaseUtils, self).__init__()

    def get_all_items(self):
#        if table_name in mapping.tables:
#            Model = mapping.tables[table_name]
        try:
            results = self._session.query(models.LoaiMonAn).all()
            print(results)
            vals = [result.__dict__ for result in results]
            return vals
        except Exception as e:
            LOG.error('Cannot get column names from tables: %s' %e)
        return None

a = DatabaseUtils()
b = a.get_all_items()
print(b)
