from dubboclient import DubboClient

dubboclt = DubboClient("211.103.136.244", 6502)

# 准备add 方法所需数据
info = {"id": 4, "name": "xwh2", "phoneNumber": "1380001112"}
# 新增一组元素到字典中
# 如果传递的参数不是Java内置的数据类型, 需要在传参的时候, 加上一串class:包名.类名 的数据
info["class"] = "com.itheima.pojo.Member"
resp = dubboclt.invoke("MemberService", "add", info)
print("resp =", resp)
