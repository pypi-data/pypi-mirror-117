from pmanager.res import *
from subprocess import run

def initialize(namespace):
    
    module_name = namespace.module_name[0]

    with open("config/default_ide.conf","r") as f:
        cmd = f.read()+f" \"pmanager/modules/{module_name}.xml \" \"pmanager/modules/{module_name}.py\""
        f.close()
        pinfo(f"running :\n{cmd}")
        run(cmd,shell=True)