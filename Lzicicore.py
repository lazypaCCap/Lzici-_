#!/usr/bin/env python3
import subprocess
import os
import json
#定义目录
目录 = os.path.expanduser("~/.config/Lzici")
设置文件 = os.path.expanduser("~/.config/Lzici/设置.json")
#判断，创建，写默认
if os.path.isdir(目录):
    引导 = False
else:
    os.makedirs(目录, exist_ok=True)
    日志目录 = os.path.expanduser("~/.config/Lzici/log")
    os.makedirs(日志目录, exist_ok=True)
    默认数据 = {"温度": "0.6","重复惩罚": "1.1","最大生成长度": "8192","上下文长度": "16384","top_k": "40","top_p": "0.9","停止词": "","存活时间": "120"}
    with open(设置文件, "w", encoding="utf-8") as f:
        json.dump(默认数据, f, indent=4, ensure_ascii=False)
    引导 = True
#读设置
with open(设置文件, "r", encoding="utf-8") as f:
    数据 = json.load(f)
#写变量
globals().update(数据)
class core:
    def gety(self):
        return 引导
    def getm(self,模型名):
        global 数据
        数据["模型名"] = 模型名
        with open(设置文件, "w", encoding="utf-8") as f:
            json.dump(数据, f, indent=4, ensure_ascii=False)
    def askn(self,问题):
        种子 = str(int.from_bytes(os.urandom(4), "big") % 1000000 + 1)
        结果 = subprocess.run(
            ["./LziciCLI.py", 问题, 温度,重复惩罚,种子,最大生成长度,上下文长度,top_k,top_p,停止词,存活时间,模型名,"False"],
            capture_output=True,
            text=True
        )
        if 结果.stdout == None:
            错误="error"
            return 错误
        else:
            return 结果.stdout
    
