import sqlalchemy as sa
from sqlalchemy import orm

from fdmgmt.common import conf as cfg
from fdmgmt.common import log as logging
from fdmgmt.db import models

CONF = cfg.CONF
LOG = logging.getLogger(__name__)

class DatabaseConnector(object):

    def __init__(self):
        self._engine = self.create_engine()
        self._session = self.get_session()

    def create_engine(self):
        return sa.create_engine(CONF['database']['connection'])

    def get_session(self):
        try:
            Session = orm.sessionmaker(bind=self._engine)
            session = Session()
            return session
        except Exception as e:
            LOG.error('Cannot connect to mssql server: %s' %e)
        finally:
            if session:
                session.close()
