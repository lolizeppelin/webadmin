from simpleservice.ormdb.tools.utils import init_database

from webadmin.models import TableBase


def init_webadmin(db_info):
    init_database(db_info, TableBase.metadata)
