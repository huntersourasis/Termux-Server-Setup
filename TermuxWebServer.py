import os
import subprocess
import pyfiglet
from termcolor import colored
import configparser

def printBanner(text):
    ascii_format = pyfiglet.figlet_format(text, font="doom", width=100)
    styledText = colored(ascii_format, 'blue')
    print(styledText)

def createDefaultWebDir():
    os.makedirs(os.path.expanduser("~/termux-server/"), exist_ok=True)
    src = "./web/index.php"
    dst = os.path.expanduser("~/termux-server/index.php")
    try:
        with open(src, "rb") as srcContent, open(dst, "wb") as dstContent:
            dstContent.write(srcContent.read())
    except FileNotFoundError:
        print("⚠️ Default index.php not found in ./web/")

def changeServerPath(newPath):
    config = configparser.ConfigParser()
    config['server'] = {
        'path': os.path.expanduser(newPath),
        'port': getDefaultServerPort()
    }
    with open('./config.ini', 'w') as configFile:
        config.write(configFile)
    return "✅ Server Path Successfully Changed."

def changeServerPort(newPort):
    config = configparser.ConfigParser()
    config['server'] = {
        'path': getDefaultServerPath(),
        'port': str(newPort)
    }
    with open('./config.ini', 'w') as configFile:
        config.write(configFile)
    return "✅ Server Port Successfully Changed."

def printFeatures():
    print("\nAvailable Features:")
    print("[1] Start Server")
    print("[2] Update Tool")
    print("[3] Change Server Path")
    print("[4] Change Server Port")
    print("[5] Exit")

def getDefaultServerPath():
    config = configparser.ConfigParser()
    config.read("./config.ini")
    return config['server'].get('path', os.path.expanduser("~/termux-server/"))

def getDefaultServerPort():
    config = configparser.ConfigParser()
    config.read("./config.ini")
    return config['server'].get('port', '8080')

def redirectToFeature(featureCode):
    if featureCode == 1:
        startServer(os.path.expanduser(getDefaultServerPath()), getDefaultServerPort())
    elif featureCode == 2:
        updateTool()
    elif featureCode == 3:
        newPath = input("Enter new Path: ")
        print(changeServerPath(newPath))
    elif featureCode == 4:
        newPort = input("Enter new Port: ")
        if newPort.isdigit():
            print(changeServerPort(newPort))
        else:
            print("⚠️ Invalid port number.")
    elif featureCode == 5:
        return False
    else:
        print("⚠️ Invalid option.")
    return True

def getAvailableWebs(serverPath):
    try:
        dir_names = [entry.name for entry in os.scandir(serverPath) if entry.is_dir()]
        return dir_names
    except FileNotFoundError:
        return []

def generateWebsBanner(serverPath):
    webList = getAvailableWebs(serverPath)
    print("\nWeb Directories:")
    print("[1] All")
    for i, name in enumerate(webList, start=2):
        print(f"[{i}] {name}")
    print(f"[{len(webList) + 2}] Exit")

def startServer(path, port):
    if not os.path.isdir(path):
        print("⚠️ Server path not found. Creating default...")
        createDefaultWebDir()
        changeServerPath("~/termux-server/")
        path = os.path.expanduser("~/termux-server/")

    while True:
        webDirs = getAvailableWebs(path)
        generateWebsBanner(path)
        try:
            usrInp = int(input("Select Option: "))
        except ValueError:
            print("⚠️ Enter a valid number.")
            continue

        if usrInp == 1:
            selected_path = path
        elif usrInp == len(webDirs) + 2:
            break
        elif 2 <= usrInp <= len(webDirs) + 1:
            selected_path = os.path.join(path, webDirs[usrInp - 2])
        else:
            print("⚠️ Invalid selection.")
            continue

        print(f"🚀 Starting server on {selected_path} at port {port}...")
        try:
            subprocess.Popen(["php", "-S", f"0.0.0.0:{port}", "-t", selected_path])
            print(f"🌐 Visit http://localhost:{port} to access.")
        except Exception as e:
            print(f"❌ Failed to start server: {e}")
        break

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
        print("✅ Update successful:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("❌ Update failed:\n", e.stderr)

# Entry Point
if __name__ == "__main__":
    printBanner("Termux Server")
    running = True
    while running:
        printFeatures()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("⚠️ Please enter a number.")
            continue
        running = redirectToFeature(choice)