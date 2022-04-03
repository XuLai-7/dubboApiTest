from dubboclient import DubboClient

# 创建 dobboclient 实例
dubboclt = DubboClient("211.103.136.244", 6502)

# 先准备findMemberCountByMonths 方法所需数据
months = ["2022.3", "2021-5"]
# months = [213123]
# 调用 invoke 方法 服务名,方法名,实参(方法使用的)
resp = dubboclt.invoke("MemberService", "findMemberCountByMonths", months)
# 显示响应结果
print("resp =", resp)
