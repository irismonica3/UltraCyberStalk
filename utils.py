import platform
import os
import datetime
import json
from colorama import *
import sys
from random import randint
import modules
init(autoreset=True)

os.environ['logfile'] = "none"

stylelist = [
    Style.DIM,
    Style.BRIGHT,
    Style.NORMAL,
    '\033[1m',
    '\033[3m',
    '\033[4m'
]

colorlist = [
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.RED,
    Fore.LIGHTBLACK_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.MAGENTA,
    Fore.WHITE
]

def getRandomColor():
    return colorlist[randint(0,len(colorlist)-1)]

def getRandomStyle():
    return stylelist[randint(0,len(stylelist)-1)]

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

def clearscreen():
    if "windows" in platform.platform().lower():
        os.system("cls")
    else:
        os.system("clear")

def createlogs():
    logfile = str(datetime.datetime.now().second)+"-"+str(datetime.datetime.now().minute)+"_"+str(datetime.datetime.now().hour)+"_"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().year)
    open("LOGS/"+logfile+".log", "w").write("--- UltraCyberStalk log file")
    os.environ['logfile'] = logfile+".log"

def executeallmodules():
    cmds = json.loads(str(open("CONFIG/commands.json", "r").read()))
    dontexecute = ["all", "dellogs", "bye", "cls", "target"]
    for command in cmds:
        c = cmds[command][1]
        if command not in dontexecute:
            try:
                c = c.replace("dork.main('normal')", "dork.main('all')")
            except:
                pass
            exec(c)

def betterprint(text):
    print(getRandomColor()+getRandomStyle()+text)
    open("LOGS/"+os.getenv('logfile'), "a").write("\n"+text)

def set_target():
    if isnotargetselected():
        gettarget()

def currenttarget():
    return open("CONFIG/target.txt", "r").readline()

def isnotargetselected():
    return currenttarget() == "NULL"

def gettarget():
    betterprint("Current target: "+currenttarget())
    newtarget = input("Insert new target ('no_target' to skip): ")
    if newtarget != "no_target":
        open("CONFIG/target.txt", "w").write(newtarget)
    betterprint("New target: "+currenttarget())

def printseparator():
    print("\n----------------\n")

def goodbye():
    betterprint("GoodBye!")
    os.system("rm -rf __pycache__")
    exit()

