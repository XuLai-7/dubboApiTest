from dubboclient import DubboClient

# 创建 dobboclient 实例
dubboclt = DubboClient("211.103.136.244", 6502)
# 调用 invoke 方法 服务名,方法名,实参(方法使用的)
resp = dubboclt.invoke("UserService", "findByUsername","admin")
# 显示响应结果
print("resp =", resp)
