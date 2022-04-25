import os
import getpass
from os import path
from pathlib import Path

gitRepo = "https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-replication"
nameOfRelease = "org.oceandsl.configuration.ide-1.3.0-SNAPSHOT-ls.jar"
pathToJar = "/home/" + getpass.getuser() + "/bin/" + nameOfRelease

#get the newest oceandsl lsp
os.system("sudo apt update && sudo apt install emacs")
Path(path.expanduser("~/temp")).mkdir(parents=True, exist_ok=True)
Path(path.expanduser("~/bin")).mkdir(parents=True, exist_ok=True)
os.system("wget -O " + "~/bin/" + nameOfRelease + " " + gitRepo + "/-/raw/master/" + nameOfRelease)

#get the newest oceandsl-mode for emacs
os.system("wget -O ~/bin/ " + gitRepo + "/-/raw/master/oceandsl-mode.el")
data = Path(path.expanduser("~/bin/oceandsl-mode.el")).read_text().replace("kali", getpass.getuser())
	Path(path.expanduser("~/bin/oceandsl-mode.el")).write_text(data)

#get latest emacs init file
os.system("wget -O ~/temp/init.el " + gitRepo + "/-/raw/master/init.el")

initfileConf = False
#check if the user already has an init emacs file
if(os.path.exists(path.expanduser("~/.emacs.d/init.el"))):
	initfileConf = True
	os.system("cp ~/.emacs.d/init.el ~/.emacs.d/init.el.backup")
	oldData = Path(path.expanduser("~/.emacs.d/init.el")).read_text()
	newData = Path(path.expanduser("~/temp/init.el")).read_text()
	if(not(oldData == newData or oldData in newData)):
		oldData = Path(path.expanduser("~/.emacs.d/init.el")).write_text(oldData + newData)
	
#check if user has an .emacs init file
if(os.path.exists(path.expanduser("~/.emacs"))):
	initfileConf = True
	os.system("cp ~/.emacs ~/.emacs.backup")
	oldData = Path(path.expanduser("~/.emacs")).read_text()
	newData = Path(path.expanduser("~/temp/init.el")).read_text()
	if(not(oldData == newData or oldData in newData)):
		oldData = Path(path.expanduser("~/.emacs")).write_text(oldData + newData)
	
if(not initfileConf):
	Path(path.expanduser("~/.emacs.d")).mkdir(parents=True, exist_ok=True)
	os.system("mv ~/temp/init.el ~/.emacs.d/init.el")
	
os.system("emacs -nw")

os.system("rm ~/temp -r")

		
