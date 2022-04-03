from dubboclient import DubboClient

"""
    基础服务对象 创建 dubbo_client 实例属性, 给其他 服务对象 继承
"""


class BaseService(object):
    # 实例方法, 属性都放到 __init__ 中
    def __init__(self):
        self.dubbo_client = DubboClient("211.103.136.244", 6502)

