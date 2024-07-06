import easygui as ea,pyperclip
import tkinter
import os
import sys
from tkinter import messagebox
import subprocess
import win32gui
import win32con
root = tkinter.Tk()
root.withdraw()
window=ea.msgbox('欢迎使用反极域软件v3.5',root=root)
def find_file_connect(start_dir, target_file):
    for root, dirs, files in os.walk(start_dir):
        if target_file in files:
            file_path = os.path.join(root, target_file)
            messagebox.showinfo("提示", "找到极域文件")
            return file_path
def check_process_running(process_name):
    cmd = f"tasklist | findstr {process_name}"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.stdout:
        return True
    return False
def check_running():
    if check_process_running("StudentMain.exe"):
        messagebox.showinfo("提示", "极域正在运行")
        yunxin=True
    else:
        messagebox.showinfo("提示", "极域没有运行")
        yunxin=False

def outofcontrol():
    if check_process_running("StudentMain.exe"):
        yunxin = True
    else:
        yunxin = False
    if yunxin:
        os.system('taskkill /f /im StudentMain.exe')
        messagebox.showinfo("提示", "脱控成功")
        return True
    else:
        return False
def small():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
def Main():
    msg ="请问你要做什么操作呢？"
    title = "操作"
    choices = ["结束监管","复制极域密钥","检测极域是否运行",'最小化极域',"退出极域脱控系统","高级版","更新日志"]#
    choice =ea.choicebox(msg, title, choices)
    if choice=="结束监管":
        s=outofcontrol()
    elif choice=="复制极域密钥":
        pyperclip.copy("mythware_super_password")
    elif choice=="检测极域是否运行":
            check_running()
    elif choice=="最小化极域":
            small()
    elif choice=="退出极域脱控系统":
        return 'exit'
    elif choice=="更新日志":
        messagebox.showinfo("更新日志",
'''
        v1.0 初始化UI
        v1.2 增加功能-结束监管
        v1.5 增加功能-复制极域密钥
        v1.8 增加功能-检测极域是否运行
        v2.0 增加功能-退出极域脱控系统-使系统可以退出
        v3.0 设置窗口始终置顶
        v3.4 增加通用密钥
        v3.5 增加高级版
        ''')
while True:
    try:
        if Main() =='exit':
            break
    except:
        pass
root.destroy()