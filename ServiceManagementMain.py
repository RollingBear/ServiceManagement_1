from tkinter import *
import ServiceButton

'''文件存储地址'''
NameListAddress = "ServiceNameList.txt"
ConfigAddress = "config.txt"
RedPicAddress = "pic\RED.png"
GreenPicAddress = "pic\GREEN.png"
NotInstallPicAddress = "pic\YELLOW.png"
LogoPicAddress = "pic\LOGO.png"

'''全局变量'''
START = "启动"
STOP = "停止"
RE_START = "重启"
SET_START_STATE_AUTO = "设置自启"
SET_START_STATE_DISABLED = "取消自启"
OPEN_LOG_FILE = "日志"
START_ALL = "全部启动"
STOP_ALL = "全部停止"
OPEN_LOG_LIST = "日志目录"
RE_FRESH_STATE = "刷新状态"
SET_START_STATE_AUTO_ALL = "全部自启"
SET_START_STATE_DISABLED_ALL = "关闭全部自启"

BLANK_1 = " "
BLANK_2 = "  "
BLANK_3 = "   "
BLANK_4 = "    "

MESSSAGE_TEXT = "绿色 = 已启动，红色 = 未启动， 黄色 = 未安装"
SERVICE_NOT_INSTALL = "服务未安装"
'''从文件中读取'''


def readFromTxt(address, type):
    if type == 1:
        File = open(address)
        result = File.read()
        File.close()
        return result
    elif type == 2:
        File = open(address)
        result = File.readlines()
        for count in range(len(result)):
            result[count] = result[count].replace("\n", "")
        File.close()
        return result


'''绘图函数'''


def printGreen(count):
    label_G = Label(image=photo_G)
    label_G.image = photo_G
    label_G.grid(row=count, column=3)


def printYellow(count):
    label_Y = Label(image=photo_Y)
    label_Y.image = photo_Y
    label_Y.grid(row=count, column=3)


def printRed(count):
    label_R = Label(image=photo_R)
    label_R.image = photo_R
    label_R.grid(row=count, column=3)


def printLogo(count, columnspan):
    label_LOGO = Label(image=photo_LOGO)
    label_LOGO.image = photo_LOGO
    label_LOGO.grid(row=count, column=1, columnspan=columnspan)


'''绘制按钮'''


def printStartButton(count, ServiceName):
    btnStart = Button(myGui, text=START, width=8, height=1, relief=FLAT,
                      command=lambda index=count, mes=ServiceName: appearStart(index, mes))
    btnStart.bind("<Enter>", lambda event: event.widget.config(fg="BLUE"))
    btnStart.bind("<Leave>", lambda event: event.widget.config(fg="BLACK"))
    btnStart.grid(row=count, column=5)


def printStopButton(count, ServiceName):
    btnStart = Button(myGui, text=STOP, width=8, height=1, relief=FLAT,
                      command=lambda index=count, mes=ServiceName: appearStop(index, mes))
    btnStart.bind("<Enter>", lambda event: event.widget.config(fg="blue"))
    btnStart.bind("<Leave>", lambda event: event.widget.config(fg="black"))
    btnStart.grid(row=count, column=5)


def printReStartButton(count, ServiceName):
    btnReStart = Button(myGui, text=RE_START, width=8, height=1, relief=FLAT,
                        command=lambda index=count, mes=ServiceName: appearReStart(index, mes))
    btnReStart.bind("<Enter>", lambda event: event.widget.config(fg="blue"))
    btnReStart.bind("<Leave>", lambda event: event.widget.config(fg="black"))
    btnReStart.grid(row=count, column=7)


def printSetStartStateButton(count, column, ServiceName, value):
    STATE = ""
    if value == "auto":
        STATE = SET_START_STATE_AUTO
    elif value == "disable":
        STATE = SET_START_STATE_DISABLED
    btnSetStartState = Button(myGui, text=STATE, width=8, height=1, relief=FLAT,
                              command=lambda index=count, mes=ServiceName, state=value: appearSetStartState(index, mes,
                                                                                                            state))
    btnSetStartState.bind("<Enter>", lambda event: event.widget.config(fg="blue"))
    btnSetStartState.bind("<Leave>", lambda event: event.widget.config(fg="black"))
    btnSetStartState.grid(row=count, column=column)


def printOpenLogFileButton(count, ServiceName):
    btnOpenLogFile = Button(myGui, text=OPEN_LOG_FILE, width=8, height=1, relief=FLAT,
                            command=lambda index=count, mes=ServiceName: appearOpenLogFile(index, mes))
    btnOpenLogFile.bind("<Enter>", lambda event: event.widget.config(fg="blue"))
    btnOpenLogFile.bind("<Leave>", lambda event: event.widget.config(fg="black"))
    btnOpenLogFile.grid(row=count, column=9)


def printStartAllButton(ServiceNameList):
    btnStartAll = Button(myGui, text=START_ALL, width=8, height=1, relief=FLAT,
                         command=lambda: ServiceStartAll(ServiceNameList))
    btnStartAll.bind("<Enter>", lambda event: event.widget.config(fg="blue"))
    btnStartAll.bind("<Leave>", lambda event: event.widget.config(fg="black"))
    btnStartAll.grid(row=len(ServiceName) + 4, column=5, columnspan=1)


def printStopAllButton(ServiceNameList):
    btnStopAll = Button(myGui, text=STOP_ALL, width=8, height=1, relief=FLAT,
                        command=lambda: ServiceStopAll(ServiceNameList))
    btnStopAll.bind("<Enter>", lambda event: event.widget.config(fg="blue"))
    btnStopAll.bind("<Leave>", lambda event: event.widget.config(fg="black"))
    btnStopAll.grid(row=len(ServiceName) + 4, column=7, columnspan=1)


def printOpenLogFileListButton():
    btnOpenLogList = Button(myGui, text=OPEN_LOG_LIST, width=8, height=1, relief=FLAT, command=lambda: openLogList())
    btnOpenLogList.bind("<Enter>", lambda event: event.widget.config(fg="blue"))
    btnOpenLogList.bind("<Leave>", lambda event: event.widget.config(fg="black"))
    btnOpenLogList.grid(row=len(ServiceName) + 4, column=9, columnspan=1)


def printSetStartStateAllButton(ServiceNameList, state, column):
    STATE = ""
    if state == "auto":
        STATE = SET_START_STATE_AUTO_ALL
    elif state == "disable":
        STATE = SET_START_STATE_DISABLED_ALL
    btnSetStartStateAll = Button(myGui, text=STATE, width=8, height=1, relief=FLAT,
                                 command=lambda NameList=ServiceNameList, value=state: ServiceSetStartAuto(NameList,
                                                                                                           value))
    btnSetStartStateAll.bind("<Enter>", lambda event: event.widget.config(fg="blue"))
    btnSetStartStateAll.bind("<Leave>", lambda event: event.widget.config(fg="black"))
    btnSetStartStateAll.grid(row=len(ServiceNameList) + 4, column=column)


'''打印标签'''


def printLable(row, column, mes, columnspan=0):
    Label(myGui, text=mes).grid(row=row, column=column, columnspan=columnspan)


'''启动时加载服务状态'''


def ServiceState(count, ServiceName):
    FLAG = ServiceButton.getServiceState(ServiceName)
    if FLAG == 1:
        printGreen(count)
    elif FLAG == 0:
        printRed(count)
    elif FLAG == -1:
        printYellow(count)


'''lambda挂载button合集'''
buttons = []


def appearStart(index, mes):
    ServiceButton.sysOptStart(mes)
    FLAG = ServiceButton.getServiceState(mes)
    ServiceState(index, mes)
    if FLAG == -1:
        ServiceButton.createResultWindows("错误", "服务未安装")
        printStartButton(index, mes)
    elif FLAG == 1:
        printStopButton(index, mes)
    elif FLAG == 0:
        printStartButton(index, mes)
    buttons[index].config(state="disable")


def appearStop(index, mes):
    ServiceButton.sysOptStop(mes)
    FLAG = ServiceButton.getServiceState(mes)
    ServiceState(index, mes)
    if FLAG == -1:
        ServiceButton.createResultWindows("错误", "服务未安装")
        printStopButton(index, mes)
    elif FLAG == 0:
        printStartButton(index, mes)
    elif FLAG == 1:
        printStopButton(index, mes)
    buttons[index].config(state="disable")


def appearReStart(index, mes):
    ServiceButton.sysOptReStart(mes)
    FLAG = ServiceButton.getServiceState(mes)

    if FLAG == -1:
        ServiceButton.createResultWindows("错误", "服务未安装")
    elif FLAG == 1:
        ServiceState(index, mes)
    elif FLAG == 0:
        ServiceButton.createResultWindows("错误", "服务重启失败")
        ServiceState(index, mes)
        printStartButton(index, mes)
    buttons[index].config(state="disable")


def appearSetStartState(index, mes, state):
    if ServiceButton.sysServiceStartAuto(mes, state):
        if state == SET_START_STATE_AUTO:
            ServiceButton.createResultWindows("", "")
        elif state == SET_START_STATE_DISABLED:
            ServiceButton.createResultWindows("", "")
    buttons[index].config(state="disable")


def appearOpenLogFile(index, mes):
    FLAG = ServiceButton.getServiceState(mes)

    if FLAG == -1:
        ServiceButton.createResultWindows("错误", "服务未安装")
    else:
        ServiceButton.openNotepadByName(LogFileAddress + "\\" + mes)
    buttons[index].config(state="disable")


'''启动全部服务'''


def ServiceStartAll(ServiceNameList):
    for count in range(len(ServiceNameList)):
        FLAG = ServiceButton.getServiceState(ServiceNameList[count])
        if FLAG != -1:
            if ServiceButton.sysOptStart(ServiceNameList[count]):
                ServiceState(count, ServiceNameList[count])
                printStopButton(count, ServiceNameList[count])


'''停止全部服务'''


def ServiceStopAll(ServiceNameList):
    for count in range(len(ServiceNameList)):
        FLAG = ServiceButton.getServiceState(ServiceNameList[count])
        if FLAG != -1:
            if ServiceButton.sysOptStop(ServiceNameList[count]):
                ServiceState(count, ServiceNameList[count])
                printStartButton(count, ServiceNameList[count])


'''全部设置自动启动'''


def ServiceSetStartAuto(ServiceNameList, state):
    for count in range(len(ServiceNameList)):
        ServiceButton.sysServiceStartAuto(ServiceNameList[count], state)


'''刷新状态'''


def ServiceReFreshState():
    for count in range(len(ServiceName)):
        FLAG = ServiceButton.getServiceState(ServiceName[count])
        if FLAG == 1:
            printGreen(count)
            printStopButton(count, ServiceName[count])
        elif FLAG == 0:
            printRed(count)
            printStartButton(count, ServiceName[count])
        elif FLAG == -1:
            printYellow(count)
    myGui.after(3000, ServiceReFreshState)


'''打开日志文件目录'''


def openLogList():
    ServiceButton.openFile(LogFileAddress)


'''构造窗口'''
myGui = Tk(className="服务管理")
# 设置窗口大小不可变
myGui.resizable(width=False, height=False)
ServiceName = readFromTxt(NameListAddress, 2)
LogFileAddress = readFromTxt(ConfigAddress, 1)

photo_G = PhotoImage(file=GreenPicAddress)
photo_R = PhotoImage(file=RedPicAddress)
photo_Y = PhotoImage(file=NotInstallPicAddress)
photo_LOGO = PhotoImage(file=LogoPicAddress)

'''for循环创建应用界面'''
for count in range(len(ServiceName)):
    '''打印服务名'''
    Label(myGui, text=ServiceName[count], anchor=NW).grid(row=count, column=1, sticky=W)

    '''打印状态图片，设置图片和两侧组件的距离'''
    ServiceState(count, ServiceName[count])

    '''设置启动，停止，重启按钮'''
    FLAG = ServiceButton.getServiceState(ServiceName[count])
    if FLAG == 0:
        printStartButton(count, ServiceName[count])
        printReStartButton(count, ServiceName[count])
        printOpenLogFileButton(count, ServiceName[count])
        printSetStartStateButton(count, 10, ServiceName[count], "auto")
        printSetStartStateButton(count, 11, ServiceName[count], "disable")
    elif FLAG == 1:
        printStopButton(count, ServiceName[count])
        printReStartButton(count, ServiceName[count])
        printOpenLogFileButton(count, ServiceName[count])
        printSetStartStateButton(count, 10, ServiceName[count], "auto")
        printSetStartStateButton(count, 11, ServiceName[count], "disable")
    elif FLAG == -1:
        printLable(count, 5, SERVICE_NOT_INSTALL, columnspan=100)

'''打印状态提示'''
printLable(row=len(ServiceName) + 1, column=1, mes=BLANK_2, columnspan=1)
printLable(row=len(ServiceName) + 2, column=1, mes=MESSSAGE_TEXT, columnspan=100)
printLable(row=len(ServiceName) + 3, column=1, mes=BLANK_2, columnspan=1)

printLogo(len(ServiceName) + 4, 3)
'''设置全部启动，全部停止，打开日志目录按钮'''
printStartAllButton(ServiceName)
printStopAllButton(ServiceName)
printOpenLogFileListButton()
printSetStartStateAllButton(ServiceName, "auto", 10)
printSetStartStateAllButton(ServiceName, "disable", 11)

'''调用自动刷新'''
ServiceReFreshState()

'''开启界面循环'''
myGui.mainloop()
