#!pyhthon3
# coding:utf8
# Copyright (c) 2020 oatsu
from pprint import pprint
project_path = RPR_GetProjectPath()
print(project_path)
print(RPR_GetLastMarkerAndCurRegion())

t = RPR_GetPlayPosition2() # 遅延補正なし
