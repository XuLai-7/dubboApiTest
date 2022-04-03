from dubboclient import DubboClient

# 创建 dobboclient 实例
dubboclt = DubboClient("211.103.136.244", 6502)

# 先准备editNumberByDate 方法所需数据, 字典列表
# 自定义包下的 OrderSetting
info = {"orderDate": "2022-05-11 12:00:00", "number": 777, "class": "com.itheima.pojo.OrderSetting"}
# 这种方式可以在列表之上,添加一组数据
# info["class"] = "com.itheima.pojo.OrderSetting"
# 调用 invoke 方法 服务名,方法名,实参(方法使用的)
# com.itheima.pojo.OrderSetting
resp = dubboclt.invoke("OrderSettingService", "editNumberByDate", info)
# 显示响应结果
print("resp =", resp)
