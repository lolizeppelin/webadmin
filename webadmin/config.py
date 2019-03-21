from simpleutil.config import cfg


def list_server_opts():
    from simpleservice.ormdb.config import database_opts
    from goperation.manager.wsgi.config import route_opts
    # from webadmin.api.wsgi.config import webadmin_opts
    cfg.set_defaults(route_opts,
                     routes=['webadmin.api.wsgi.routers'])
    # return route_opts + resource_opts + database_opts
    return route_opts + database_opts
