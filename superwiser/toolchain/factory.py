import os

from superwiser.common.log import logger
from superwiser.toolchain.core import Orc
from superwiser.toolchain.utils import Conf, Supervisor


class OrcFactory(object):
    def make_orc(self, conf_path, zk_host, zk_port):
        logger.info('Making Orc')
        if conf_path is None:
            conf_path = os.path.join(os.getcwd(), 'supervisord.conf')
            conf = Conf.create(conf_path)
        else:
            conf = Conf(conf_path)
        if zk_host is None:
            zk_host = os.environ.get('zk_host', 'localhost')
        if zk_port is None:
            zk_port = os.environ.get('zk_port', 2181)
        supervisor = Supervisor(conf)
        return Orc(zk_host, zk_port, supervisor)
