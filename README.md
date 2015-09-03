# Vagrant

Vagrant is a virtual machine manager that can be shared across platforms.

1. Download and install [Vagrant](https://www.vagrantup.com/downloads.html).
2. Download and install [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
3. Download the vagrant box named ```vm.box``` which can be found under the "Releases" tab of this repository.
4. Open your command line (cmd for windows, Terminal.app for mac) and run the following commands
5. Add the box to vagrant your local vagrant. 
```bash
vagrant box add --name adsa/python [path to vagrant box]
```
6. Create the proper vagrant file by either:
 - Using the given vagrant file OR
 - Running ``` vagrant init ``` and editing the Vagrantfile line
```ruby
config.vm.box = "base"
```
to be
```ruby
config.vm.box = "adsa/python"
```
7. In the folder that holds the Vagrantfile, run
```bash
vagrant up
vagrant ssh
```

This will log you in to the virtual machine and give you console access. 
### Notes
 - Files in the folder containing the Vagrantfile will be shared to the ```/vagrant``` folder in the 
virtual machine, so you can edit files in your normal OS with your text editor of choice 
(Sublime Text, Atom, etc.).
 - Run scripts in the virtual machine on the command line via 
```bash
python myscript.py
```
