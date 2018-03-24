#!/bin/bash
#eol=lf
path=`pwd`
sudo cp $path/db.service  /lib/systemd/system/db.service
sudo cp $path/db.service  /lib/systemd/system/db.timer
sudo cp $path/script_db.py  /lib/systemd/system/script_db.py

sudo cp $path/code.service  /lib/systemd/system/code.service
sudo cp $path/code.service  /lib/systemd/system/code.timer
sudo cp $path/script_code.py  /lib/systemd/system/script_code.py

sudo cp $path/rm.service  /lib/systemd/system/rm.service
sudo cp $path/rm.service  /lib/systemd/system/rm.timer
sudo cp $path/script_rm.py  /lib/systemd/system/script_rm.py



sudo chmod 644 /lib/systemd/system/db.service
sudo chmod 644 /lib/systemd/system/script_db.py
sudo chmod +x /lib/systemd/system/script_db.py
sudo chmod 644 /lib/systemd/system/db.timer

sudo chmod 644 /lib/systemd/system/code.service
sudo chmod 644 /lib/systemd/system/script_code.py
sudo chmod +x /lib/systemd/system/script_code.py
sudo chmod 644 /lib/systemd/system/code.timer

sudo chmod 644 /lib/systemd/system/rm.service
sudo chmod 644 /lib/systemd/system/script_rm.py
sudo chmod +x /lib/systemd/system/script_rm.py
sudo chmod 644 /lib/systemd/system/rm.timer


sudo systemctl daemon-reload

sudo systemctl enable db.timer
sudo systemctl start db.timer

sudo systemctl enable code.timer
sudo systemctl start code.timer

sudo systemctl enable rm.timer
sudo systemctl start rm.timer




