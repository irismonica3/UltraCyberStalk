import os, json
import modules
import utils
import sys

class mainclass:

    version = "1.1 production"

    def processcommand(self, cmd):

        cmds = json.loads(str(open("CONFIG/commands.json", "r").read()))

        if cmd == "help":
            utils.printseparator()
            for command in cmds:
                utils.betterprint("? "+command+" -> "+cmds[command][0])
            utils.printseparator()
        else:
            try:
                exec(cmds[cmd][1])
            except KeyError:
                pass

    def shell(self):
        while True:
            mainclass.processcommand(input("? "))

    def logo(self):
        print(f"""
       ____                                   
 __ __/ / /________ _                         
/ // / / __/ __/ _ `/                         
\_,_/_/\__/_/  \_,_/        __       ____     
 ______ __/ /  ___ _______ / /____ _/ / /__   
/ __/ // / _ \/ -_) __(_-</ __/ _ `/ /  '_/   
\__/\_, /_.__/\__/_/ /___/\__/\_,_/_/_/\_\    
   /___/                                       
        
[{mainclass.version} by github.com/kl3sshydra]

        """)

    def main(self):
        utils.createlogs()
        utils.clearscreen()
        mainclass.logo()
        mainclass.shell()

mainclass = mainclass()
mainclass.main()