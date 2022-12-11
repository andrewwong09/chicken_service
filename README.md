**Chicken Service**

***Setup Python Environment***
```
pip3 install virtualenv virtualenvwrapper
nano ~/.bashrc
```
Add below to bottom of .bashrc
```
#Virtualenvwrapper settings:
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh
export VIRTUALENVWRAPPER_ENV_BIN_DIR=bin

```
```
source .bashrc
mkvirtualenv chicken_door
workon chicken_door
```
***Labjack Setup***
- install libusb-1.0 and libusb-1.0-dev
- build and install the LabJack exodriver (https://github.com/labjack/exodriver.git)
- install LabJacKPython (https://github.com/labjack/LabJackPython.git)


***Service Instructions***
- copy chicken.service file to: /home/andrew/.config/systemd/user/

```
chmod 777 chicken_service.sh
systemctl --user enable chicken.service
systemctl --user start chicken.service 
sudo loginctl enable-linger andrew
```
- confirm andrew exists in linger dir:
```
ls /var/lib/systemd/linger/
```   
