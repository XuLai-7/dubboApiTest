"""
类名：BaseService
实例属性：
    dubbo客户端对象：dubbo_client，创建DubboClient()后给dubbo_client赋值
实例方法：
    def __init__(self)：
        # 添加实例属性 dubbo_client

会员服务类：继承于BaseService
    def __init__(self)：
        # 先调父类__init__()，再添加实例属性 service_name
"""
from dubboclient import DubboClient


class BaseService:
    # 实例属性写在 __init__ 方法中
    def __init__(self):
        self.dubbo_client = DubboClient("211.103.136.244", 6502)


class MemberService(BaseService):

    # 重写 父类 __init__ 方法
    def __init__(self):
        # super().父类方法名, 调用父类方法, 先拿到父类的属性
        # 扩展式重写
        super().__init__()
        # 服务名共用,写成属性, 方法名不共用, 就不写成属性
        # 不是公共的部分不适合放到属性中
        self.service_name = "MemberService"


if __name__ == '__main__':
    member = MemberService()
    months = ["2022.3", "2021-5"]
    resp =  member.dubbo_client.invoke(member.service_name, "findMemberCountByMonths", months)
    print("resp"+resp)
