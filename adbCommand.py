# python 3.6.x

import os

devices = "adb devices"
brevent = "adb -d shell sh /data/data/me.piebridge.brevent/brevent.sh"
shizuku = "adb shell sh /storage/emulated/0/Android/data/moe.shizuku.privileged.api/start.sh"

devices_num = os.popen(devices).read()
if "successful" in devices_num:
	print("连接成功")
else:
    print("连接失败")
    os.system("pause")
    os._exit(0)
    
print(devices_num)
print("开启shizuku服务")
os.popen(shizuku).read()
print("开启黑阈服务")
result = os.popen(brevent).read()
if "error" in result:
	print("黑阈服务开启失败")
print(result)
os.system("pause")