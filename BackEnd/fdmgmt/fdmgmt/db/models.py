import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.dialects import mssql

Base = sa.orm.declarative_base()

class LoaiMonAn(Base):
    __tablename__ = 'LoaiMonAn'
    MaLoaiMA = sa.Column(
        sa.Integer, primary_key=True, autoincrement=True
    )
    TenLoaiMA = sa.Column(sa.String(100), nullable=False)

class MonAn(Base):
    __tablename__ = 'MonAn'
    MaMA = sa.Column(
        sa.Integer, primary_key=True, autoincrement=True
    )
    TenMA = sa.Column(sa.String(100), nullable=False)
    ChiTietMA = sa.Column(sa.String(500), nullable=False)
    Gia = sa.Column(sa.Integer, nullable=False)
    AnhMA = sa.Column(sa.String(1024), nullable=False)
    SoLuongMA = sa.Column(sa.Integer, nullable=False)
    Active = sa.Column(sa.Integer, default=0)
    isDeleted = sa.Column(sa.Integer, default=0)
    MaLoaiMA = sa.Column(sa.Integer, sa.ForeignKey('LoaiMonAn.MaLoaiMA'))

class TaiKhoan(Base):
    __tablename__ = 'TaiKhoan'
    id_user = sa.Column(
        sa.Integer, primary_key=True, autoincrement=True
    )
    username = sa.Column(sa.String(30), nullable=False)
    password = sa.Column(sa.String(30), nullable=False)
    sdt = sa.Column(sa.String(20))
    email = sa.Column(sa.String(30), nullable=False)
    loai = sa.Column(sa.String(20))
    AnhKH = sa.Column(sa.String(1024))
    TenKH = sa.Column(sa.String(100))
    DiaChi = sa.Column(sa.String(100))
    isDeleted = sa.Column(sa.Integer, default=0)

class HoaDon(Base):
    __tablename__ = 'HoaDon'
    MaHD = sa.Column(
        sa.Integer, primary_key=True, autoincrement=True
    )
    MaMA = sa.Column(sa.Integer, sa.ForeignKey('MonAn.MaMA'))
    id_user = sa.Column(sa.Integer, sa.ForeignKey('KhachHang.id_user'))
    NgayTao = sa.Column(sa.Date, default=sa.func.current_date())
    SoLuong = sa.Column(sa.Integer)
    TongTien = sa.Column(sa.Integer)
    isDeleted = sa.Column(sa.Integer, default=0)


class DonDatHang(Base):
    __tablename__ = 'DonDatHang'
    MaDDH = sa.Column(
        sa.Integer, primary_key=True, autoincrement=True
    )
    MaKH = sa.Column(
        sa.Integer, 
        sa.ForeignKey('KhachHang.id_user'), 
        nullable=False
    )
    NgayDat = sa.Column(sa.Date, default=sa.func.current_date())
    TongTien = sa.Column(sa.Integer)
    isDeleted = sa.Column(sa.Integer, default=0)

class ChiTietDonDatHang(Base):
    __tablename__ = 'ChiTietDonDatHang'
    MaCTDDH = sa.Column(
        sa.Integer, primary_key=True, autoincrement=True
    )
    MaDDH = sa.Column(
        sa.Integer,
        sa.ForeignKey('DonDatHang.MaDDH'),
        nullable=False
    )
    MaMA = sa.Column(
        sa.Integer,
        sa.ForeignKey('MonAn.MaMA'),
        nullable=False
    )
    SoLuong = sa.Column(sa.Integer)
    Gia = sa.Column(sa.Integer)
    TongTien = sa.Column(sa.Integer, nullable=False)
    isDeleted = sa.Column(sa.Integer, default=0)

class GioHang(Base):
    __tablename__ = 'GioHang'
    MaGioHang = sa.Column(
        sa.Integer, primary_key=True, autoincrement=True
    )
    id_user = sa.Column(
        sa.Integer, 
        sa.ForeignKey('TaiKhoan.id_user'), 
        nullable=False
    )
    MaMA = sa.Column(
        sa.Integer,
        sa.ForeignKey('MonAn.MaMA'),
        nullable=False
    )
    SoLuong = sa.Column(sa.Integer, nullable=False)
    TongTien = sa.Column(sa.Integer)
    NgayThemGioHang = sa.Column(sa.Date, default=sa.func.current_date())
