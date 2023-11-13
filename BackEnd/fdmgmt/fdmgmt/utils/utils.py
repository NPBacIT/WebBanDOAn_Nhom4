import json

from fdmgmt.db import models
from fdmgmt.db import database as db
from fdmgmt.utils import mapping
from fdmgmt.common import log as logging

LOG = logging.getLogger(__name__)

class DatabaseUtils(db.DatabaseConnector):
    
    def __init__(self):
        super(DatabaseUtils, self).__init__()

    def get_all_items(self, table_name, order_by_column,
                    page, items_per_page=None):
        if table_name in mapping.tables:
            Model = mapping.tables[table_name]
        try:
            LOG.debug('Getting all items from %s' %Model)
            if items_per_page:
                offset = (page - 1) * items_per_page
                LOG.debug(offset)
                results = (self._session.query(Model).order_by(getattr(Model, order_by_column)).
                            offset(offset).limit(items_per_page).all())
            vals = [{k: v for k, v in result.__dict__.items() 
                    if k != '_sa_instance_state'} for result in results]
            return vals
        except Exception as e:
            LOG.error('Cannot get column names from tables: %s' %e)
        finally:
            self._session.close()
        return None

    def filter_items(self, table_name, table_key, value):
        if table_name in mapping.tables:
            Model = mapping.tables[table_name]
        try:
            results = self._session.query(Model).filter_by(**{table_key: value}).all()
            vals = [{k: v for k, v in result.__dict__.items() 
                    if k != '_sa_instance_state'} for result in results]
            return vals
        except Exception as e:
            LOG.error('Cannot get items: %s' %e)
        finally:
            self._session.close()

    def get_item(self, table_name, table_key, value):
        """table_key has to be uniq like ID"""
        if table_name in mapping.tables:
            Model = mapping.tables[table_name]
        try:
            LOG.debug('Getting item from %s' %Model)
            result = self._session.query(Model).filter_by(**{table_key: value}).one()
            val = result.__dict__
            val.pop('_sa_instance_state', None)
            return val
        except Exception as e:
            LOG.error('Cannot get items: %s' %e)
        finally:
            self._session.close()
        return None

    def _mon_an_model_add(self, TenMA, ChiTietMA, Gia,
                        AnhMA, SoLuongMA, MaLoaiMa):
        item_values = {
            'TenMA': TenMA,
            'ChiTietMA': ChiTietMA,
            'Gia': Gia,
            'AnhMA': AnhMA,
            'SoLuongMA': SoLuongMA,
            'MaLoaiMA': MaLoaiMa
        } 

        try:
            LOG.debug('Inserting new items')
            mon_an = models.MonAn(**item_values)
            self._session.add(mon_an)
            self._session.commit()
            return True
        except Exception as e:
            LOG.error('Insert failed: %s' %e)
        finally:
            self._session.close()

    def _gio_hang_model_add(self, MaGioHang, MaKH, MaMA, 
                            SoLuong, TongTien, NgayThemGioHang):
        item_values = {
            'id_user': MaKH,
            'MaMA': MaMA,
            'SoLuong': SoLuong,
            'TongTien': TongTien,
            'NgayThemGioHang': NgayThemGioHang
        } 

        try:
            LOG.debug('Inserting new items')
            mon_an = models.GioHang(**item_values)
            self._session.add(mon_an)
            self._session.commit()
            return True
        except Exception as e:
            LOG.error('Insert failed: %s' %e)
        finally:
            self._session.close()

    def _mon_an_model_udapte(self, MaMA, Gia, SoLuong):
        try:
            mon_an = self._session.get(models.MonAn, MaMA)
            if not mon_an:
                LOG.info('Item did not exist')
                return False
            else:
                LOG.debug('Updating new item')
                mon_an.Gia = Gia
                mon_an.SoLuong = SoLuong
                self._session.commit()
                update_record = self.get_item('MonAn', 'MaMA', MaMA)
                return update_record
        except Exception as e:
            LOG.error('Update failed: %s' %e)
        finally:
            self._session.close()
    
    def _mon_an_model_delete(self, MaMA):
        try:
            mon_an = self._session.get(models.MonAn, MaMA)
            if not mon_an:
                LOG.info('Item did not exist')
                return False
            else:
                LOG.debug('Deleting item')
                mon_an.isDeleted = 1
                self._session.commit()
                return True
        except Exception as e:
            LOG.error('Delete failed: %s' %e)
        finally:
            self._session.close()

    def _gio_hang_model_delete(self, MaMA):
        try:
            mon_an = self._session.get(models.GioHang, MaGioHang)
            if not mon_an:
                LOG.info('Item did not exist')
                return False
            else:
                LOG.debug('Deleting item')
                mon_an.isDeleted = 1
                self._session.commit()
                return True
        except Exception as e:
            LOG.error('Delete failed: %s' %e)
        finally:
            self._session.close()
