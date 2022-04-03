from dubboclient import DubboClient

# 创建 dobboclient 实例
dubboclt = DubboClient("211.103.136.244", 6502)

# 先准备add 方法所需数据, 字典列表
# 所有的自定义类型, 传字典类型的数据
ordersetting=[{"orderDate":"2022-04-23 13:08:34","number":33}]
# months = [213123]
# 调用 invoke 方法 服务名,方法名,实参(方法使用的)
resp = dubboclt.invoke("OrderSettingService", "add", ordersetting)
# 显示响应结果
print("resp =", resp)
