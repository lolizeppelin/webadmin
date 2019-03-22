# -*- coding:utf-8 -*-
import webob.exc



from sqlalchemy.orm.exc import NoResultFound

from simpleutil.log import log as logging
from simpleutil.utils import singleton

from simpleutil.common.exceptions import InvalidArgument

from simpleservice.wsgi.middleware import MiddlewareContorller

from goperation.manager.utils import resultutils

from webadmin import common
from webadmin.models import KeyWord
from webadmin.api import endpoint_session




LOG = logging.getLogger(__name__)

FAULT_MAP = {
    InvalidArgument: webob.exc.HTTPClientError,
    NoResultFound: webob.exc.HTTPNotFound,
}


@singleton.singleton
class KeywordRequest(MiddlewareContorller):


    def index(self, req, body=None):
        session = endpoint_session()
        ret_dict = resultutils.bulk_results(session,
                                            model=KeyWord,
                                            columns=[KeyWord.kid,
                                                     KeyWord.value,
                                                     ],
                                            counter=KeyWord.kid,
                                            order=KeyWord.kid, desc=True,
                                            limit=100000)
        return ret_dict


    def create(self, req, body=None):
        raise NotImplementedError

    def show(self, req, mid, body=None):
        """列出用户信息"""
        raise NotImplementedError

    def update(self, mid, body=None):
        raise NotImplementedError

    def delete(self, mid, body=None):
        raise NotImplementedError
