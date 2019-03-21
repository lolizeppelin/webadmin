# -*- coding:utf-8 -*-
import webob.exc



from sqlalchemy.orm.exc import NoResultFound

from simpleutil.log import log as logging
from simpleutil.utils import singleton

from simpleutil.common.exceptions import InvalidArgument

from simpleservice.wsgi.middleware import MiddlewareContorller

from simpleservice.ormdb.api import model_query

from goperation.manager.utils import resultutils

from webadmin import common
from webadmin.models import LogEntity
from webadmin.api import endpoint_session




LOG = logging.getLogger(__name__)

FAULT_MAP = {
    InvalidArgument: webob.exc.HTTPClientError,
    NoResultFound: webob.exc.HTTPNotFound,
}


@singleton.singleton
class LogsRequest(MiddlewareContorller):

    ADMINAPI = False

    def index(self, req, body=None):
        session = endpoint_session()
        ret_dict = resultutils.bulk_results(session,
                                            model=LogEntity,
                                            columns=[LogEntity.id,
                                                     LogEntity.ip,
                                                     LogEntity.atime,
                                                     LogEntity.path],
                                            counter=LogEntity.id,
                                            order=LogEntity.atime, desc=True,
                                            limit=1000)
        return ret_dict


    def create(self, req, body=None):
        raise NotImplementedError

    def show(self, req, id, body=None):
        session = endpoint_session(readonly=True)
        id = int(id)
        query = model_query(session, LogEntity, filter=LogEntity.id == id)
        log = query.one()
        return resultutils.results(result='show log success',
                                   data=[dict(name=log.id,
                                              ip=log.ip,
                                              atime=log.atime,
                                              path=log.path,
                                              status=log.status,
                                              size=log.size,
                                              host=log.host,
                                              client=log.client,
                                              )])

    def update(self, mid, body=None):
        raise NotImplementedError

    def delete(self, mid, body=None):
        raise NotImplementedError
