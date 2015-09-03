



# Vagrant

Vagrant is a virtual machine manager that can be shared across platforms.

Download and install vagrant from [Vagrant's website](https://www.vagrantup.com/downloads.html).

The vagrant box can be found under the "Releases" tab of this repository. Download it and follow the Usage instructions

### Usage
To add the vagrant box to local vagrant:
```bash
vagrant box add --name adsa/python [path to vagrant box]
```
Now the box will be available locally. You can use it by copying the Vagrantfile in this repository 
or by running
```bash
vagrant init
```
and changing the generated Vagrantfile line
```ruby
config.vm.box = "base"
```
to
```ruby
config.vm.box = "adsa/python"
```


Now, in the folder that contains the Vagrantfile, run
```bash
vagrant up
vagrant ssh
```

This will log you in to the virtual machine and give you console access. Files in the folder containing
the Vagrantfile will be shared to the ```/vagrant``` folder in the virtual machine, so you can edit
files in your normal OS with your text editor of choice (Sublime Text, Atom, etc.).
