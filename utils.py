import platform
import os
import datetime
import json
import modules

os.environ['logfile'] = "none"

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
    print(text)
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
    open("CONFIG/target.txt", "w").write(input("Insert target: "))
    betterprint("New target: "+currenttarget())

def printseparator():
    print("\n----------------\n")

def goodbye():
    print("GoodBye!")
    exit()

