# -*- coding:utf-8 -*-
import sqlalchemy as sa
from sqlalchemy.ext import declarative

from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.dialects.mysql import INTEGER

from simpleservice.ormdb.models import TableBase
from simpleservice.ormdb.models import InnoDBTableBase


TableBase = declarative.declarative_base(cls=TableBase)



class LogEntity(TableBase):
    """日志"""
    id = sa.Column(INTEGER(unsigned=True), nullable=False,
                    primary_key=True, autoincrement=True)                        # 漫画ID
    ip = sa.Column(VARCHAR(128), nullable=False)                               # 漫画名
    atime = sa.Column(INTEGER(unsigned=True), nullable=False)                 # 注册时间
    path = sa.Column(VARCHAR(256), nullable=False)                               # 漫画名
    status = sa.Column(INTEGER, nullable=False)          # 用户状态
    size = sa.Column(INTEGER(unsigned=True), nullable=False)          # 用户状态
    host = sa.Column(VARCHAR(256), nullable=False)
    client = sa.Column(VARCHAR(256), nullable=False)

    __table_args__ = (
        sa.Index('time', atime),
        InnoDBTableBase.__table_args__
    )


class KeyWord(TableBase):
    """关键字"""
    kid = sa.Column(INTEGER(unsigned=True), nullable=False, primary_key=True)
    value = sa.Column(VARCHAR(128), nullable=False)

    __table_args__ = (
        InnoDBTableBase.__table_args__
    )

