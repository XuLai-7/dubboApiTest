from dubboclient import DubboClient

# 创建 DubboClient 实例
dubboclt = DubboClient("211.103.136.244", 6502)

# 调用 invoke() 方法
resp = dubboclt.invoke("MemberService", "findByTelephone", "13020210001")
# 打印响应结果
print("resp=", resp)
print("resp=", type(resp))
