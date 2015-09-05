# Vagrant

1. Download and install [Vagrant](https://www.vagrantup.com/downloads.html).
2. Download and install [Virtualbox](https://www.virtualbox.org/wiki/Downloads).
3. Download the vagrant box named ```vm.box``` which can be found under the "Releases" tab of this repository.
4. Install [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).
5. Change directory to the location of the box that you downloaded
6. Add the box to vagrant your local vagrant in your terminal
```bash
vagrant box add --name adsa/python [path to downloaded box]
```

7. Open a terminal (cmd.exe for windows, Terminal.app), cd to the directory where you cloned this repo 
and run:
```bash
vagrant up
```
8. Login to the vagrant box

For windows:
 - Run putty.exe
 - Connect edit the connection with
  - Hostname: 127.0.0.1
  - Port: 2222
  - Connection Type: ssh
  - Username: vagrant
  - Password: vagrant

For Linux/Mac OSX
 - Open your terminal (Terminal.app on Mac)
 - cd to the folder containing this git repo
 - Run: ```vagrant ssh```

This will log you in to the virtual machine and give you console access. 

### Notes
 - Files in the folder containing the Vagrantfile will be shared to the ```/vagrant``` folder in the 
virtual machine, so you can edit files in your normal OS with your text editor of choice 
(Sublime Text, Atom, etc.).
 - Run scripts in the virtual machine on the command line via ```python myscript.py```
 - Search for python packages via ```pip search [package name]```
 - Install packages on the virtual machine via ```sudo pip install [package name]```
 - Files in the box's ```/vagrant``` folder will be shared with your computer. So you can edit files
 on your computer and run it on the box.
