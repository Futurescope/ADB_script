# python 3.6.x

import os

devices = "adb devices"
brevent = "adb -d shell sh /data/data/me.piebridge.brevent/brevent.sh"
shizuku = "adb shell sh /storage/emulated/0/Android/data/moe.shizuku.privileged.api/start.sh"

devicesIds = os.popen(devices).read().splitlines(False)
if devicesIds[1] == '':
    print("连接失败")
    os.system("pause")
    os._exit(0)
else:
	print("连接成功")
    
print("已连接" + devicesIds[1])
print("开启shizuku服务")
os.popen(shizuku).read()
print("开启黑阈服务")
result = os.popen(brevent).read()
if "error" in result:
	print("黑阈服务开启失败")
print(result)
os.system("pause")