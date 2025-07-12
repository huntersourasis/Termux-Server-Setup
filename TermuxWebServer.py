import os
import subprocess
import pyfiglet
from termcolor import colored
import configparser
def printBanner(text):
    ascii_format = pyfiglet.figlet_format(text , font="doom" , width=100)
    styledText = colored(ascii_format , 'blue')
    print(styledText)
def createDefaultWebDir() :
    os.makedirs(os.path.expanduser("~/termux-server/") , exist_ok=True) # exist_ok=True Pervents the already exist Error
    src = "./web/index.php"
    dst = os.path.expanduser("~/termux-server/index.php")
    with open(src , "rb") as srcContent , open(dst , "wb") as dstContent :
        dstContent.write(srcContent.read())
def changeServerPath(newPath):
    config = configparser.ConfigParser()
    config['server'] = {
        'path' : os.path.expanduser(newPath),
        'port' : getDefaultServerPort()
    }
    with open('./config.ini' , 'w') as configFile:
        config.write(configFile)
        return "Server Path Successfully Changed."
def changeServerPort(newPort):
    config = configparser.ConfigParser()
    config['server'] = {
        'path' : getDefaultServerPath(),
        'port' : newPort
    }
    with open('./config.ini' , 'w') as configFile:
        config.write(configFile)
        return "Server Port Successfully Changed."
def printFeatures():
    print("[1] Start Server")
    print("[2] Update Tool")
    print("[3] Change Server Path")
    print("[4] Change Server Port")
    print("[5] Exit")
def getDefaultServerPath():
    config = configparser.ConfigParser()
    config.read("./config.ini")
    return config['server']['path']
def getDefaultServerPort():
    config = configparser.ConfigParser()
    config.read("./config.ini")
    return config['server']['port']
def redirectToFeature(featureCode):
    if featureCode == 1 :
        startServer(os.path.expanduser(getDefaultServerPath()) , getDefaultServerPort())
        return True
    elif featureCode == 2:
        updateTool()
        return True
    elif featureCode == 3:
        newPath = str(input("Enter new Path : "))
        res = changeServerPath(newPath)
        print(res)
        return True
    elif featureCode == 4 :
        newPort = int(input("Enter new Port Name : "))
        res = changeServerPort(newPort)
        print(res)
        return True
    elif featureCode == 5:
        return False
    else :
        return True
def getAvailableWebs(serverPath):
    return os.listdir(os.path.expanduser(serverPath))

def startServer(path , port):
    if os.path.isdir(path) == False:
        createDefaultWebDir()
        changeServerPath(os.path.expanduser("~/termux-server/"))
        path = os.path.expanduser("~/termux-server/")
    try:
        output = subprocess.check_output(["php" , "-S"  , f"0.0.0.0:{port}" , "-t" , path], text=True)
        return output 
    except subprocess.CalledProcessError as e:
        return f"Command failed with return code {e.returncode}\nOutput: {e.output}"
def updateTool():
    repo_path = "./"
    try:
        result = subprocess.run(
            ["git", "pull", "origin", "main"],
            cwd=repo_path,
            check=True,
            capture_output=True,
            text=True
        )
        print("Output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:\n", e.stderr)