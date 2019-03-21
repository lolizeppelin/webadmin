from simpleutil.config import cfg
from simpleservice.ormdb.config import database_opts
from webadmin import common

CONF = cfg.CONF

group = CONF.find_group(common.NAME)
CONF.register_opts(database_opts, group)