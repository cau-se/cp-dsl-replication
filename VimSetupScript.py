import os
import getpass
from os import path
from pathlib import Path

gitRepo = "https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-replication"
nameOfRelease = "org.oceandsl.configuration.ide-1.3.0-SNAPSHOT-ls.jar"
pathToJar = "/home/" + getpass.getuser() + "/bin/" + nameOfRelease


os.system("sudo apt install vim")
Path(path.expanduser("~/temp")).mkdir(parents=True, exist_ok=True)
#print(path.expanduser("~/bin"))
Path(path.expanduser("~/bin")).mkdir(parents=True, exist_ok=True)
os.system("wget -O " + "~/bin/" + nameOfRelease + " " + gitRepo + "/-/raw/master/" + nameOfRelease)


os.system("wget -O ~/temp/example.vimrc " + gitRepo + "/-/raw/master/example.vimrc")

#Wenn .vimrc schon existiert müssen wir entweder mergen oder der entsprechende Code ist auch schon vorhanden dann müssen wir nichts tun
if(os.path.exists(path.expanduser("~/.vimrc"))):
	newData = Path(path.expanduser("~/temp/example.vimrc")).read_text().replace(nameOfRelease, pathToJar)
	oldData = Path(path.expanduser("~/.vimrc")).read_text()
	if(newData not in oldData):
		os.system("sudo chown " + getpass.getuser() + " ~/.vimrc")
		Path(path.expanduser("~/.vimrc")).write_text(oldData + newData)
else:
	os.system("mv ~/temp/example.vimrc ~/.vimrc")
	os.system("sudo chown " + getpass.getuser() + " ~/.vimrc")
	data = Path(path.expanduser("~/.vimrc")).read_text().replace(nameOfRelease, pathToJar)
	Path(path.expanduser("~/.vimrc")).write_text(data)
	
	
	

Path(path.expanduser("~/.vim")).mkdir(parents=True, exist_ok=True)

#Die Plugins werden installiert
os.system("vim +slient +PlugInstall +qall")


os.system("wget -O ~/temp/filetype.vim " + gitRepo + "/-/raw/master/filetype.vim")
if(os.path.exists(path.expanduser("~/.vim/filetype.vim"))):
	newData = Path(path.expanduser("~/temp/filetype.vim")).read_text()
	oldData = Path(path.expanduser("~/.vim/filetype.vim")).read_text()
	if(newData not in oldData):
		Path(path.expanduser("~/.vim/filetype.vim")).write_text(oldData + newData)
else:
	os.system("mv ~/temp/filetype.vim ~/.vim/filetype.vim")
	
os.system("rm ~/temp -r")