import os
import time
from tkinter.messagebox import showinfo

'''启动服务'''


def sysOptStart(serName):
    result = os.popen("sc start " + serName)

    # createResultWindows(result.read())

    if "START_PENDING" or "RUNNING" in result.read():
        return True
    else:
        return False


'''停止服务'''


def sysOptStop(serName):
    result = os.popen("sc stop " + serName)

    # createResultWindows(result.read())

    if "STOP_PENDING" or "STOPPED" in result.read():
        return True
    else:
        return False


'''重启服务'''


def sysOptReStart(serName):
    flag = 0

    resultSTOP = os.popen("sc stop " + serName)

    if "STOP_PENDING" or "STOPPED" in resultSTOP.read():
        flag += 1

    time.sleep(1)

    resultSTART = os.popen("sc start " + serName)

    if "START_PENDING" or "RUNNING" in resultSTART.read():
        flag += 2

    if flag == 3:
        return True
    else:
        return False


'''设置服务自启动状态'''


def sysServiceStartAuto(ServiceName, Value):
    result = os.popen("sc config " + ServiceName + " start=" + Value)
    if "成功" in result.read():
        return True
    else:
        return False


'''弹窗'''


def createResultWindows(type, result):
    showinfo(title=type, message=result)


'''读取服务状态'''


def getServiceState(ServiceName):
    result = os.popen("sc query " + ServiceName).read()
    if "RUNNING" in result:
        # return result.read()
        return 1
    elif "START_PENDING" in result:
        return 1
    elif "STOPPED" in result:
        # return result.read()
        return 0
    elif "STOP_PENDING" in result:
        return 0
    elif "1060" in result:
        # return result.read()
        return -1


'''调用外部程序打开记事本'''


def openNotepadByName(ServiceName):
    os.system("notepad " + ServiceName + ".txt")


'''打开文件夹'''


def openFile(DirectoryAddress):
    os.popen("start " + DirectoryAddress)
