# -*- coding:utf-8 -*-
from simpleutil.utils import singleton
from simpleservice.wsgi import router
from simpleservice.wsgi.middleware import controller_return_response

from webadmin import common
from webadmin.api.wsgi.controllers import keyword
from webadmin.api.wsgi.controllers import logentity


@singleton.singleton
class KeywordRouters(router.ComposableRouter):


    def add_routes(self, mapper):
        _controller = controller_return_response(keyword.KeywordRequest(), keyword.FAULT_MAP)
        collection = mapper.collection(collection_name='keywords',
                                       resource_name='keyword',
                                       controller=_controller,
                                       path_prefix='/%s' % common.NAME,
                                       member_prefix='/{id}',
                                       collection_actions=['index'],
                                       member_actions=[])

@singleton.singleton
class LogsRouters(router.ComposableRouter):

    def add_routes(self, mapper):

        _controller = controller_return_response(logentity.LogsRequest(), logentity.FAULT_MAP)

        collection = mapper.collection(collection_name='logs',
                          resource_name='log',
                          controller=_controller,
                          path_prefix='/%s' % common.NAME,
                          member_prefix='/id}',
                          collection_actions=['index'],
                          member_actions=['show'])



class Routers(router.RoutersBase):

    def append_routers(self, mapper, routers=None):
        # mapper.redirect("/%s/manager/login/{username:.*}" % common.NAME,
        #                 "/goperation/login/{username}")
        KeywordRouters(mapper)
        LogsRouters(mapper)

