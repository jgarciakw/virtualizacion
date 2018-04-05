#!/bin/bash
#eol=lf
path=`pwd`
sudo cp $path/db.service  /lib/systemd/system/db.service
sudo cp $path/script_db.py  /lib/systemd/system/script_db.py

sudo cp $path/code.service  /lib/systemd/system/code.service
sudo cp $path/script_code.py  /lib/systemd/system/script_code.py

sudo cp $path/rm.service  /lib/systemd/system/rm.service
sudo cp $path/script_rm.py  /lib/systemd/system/script_rm.py



sudo chmod 644 /lib/systemd/system/db.service
sudo chmod 644 /lib/systemd/system/script_db.py
sudo chmod +x /lib/systemd/system/script_db.py

sudo chmod 644 /lib/systemd/system/code.service
sudo chmod 644 /lib/systemd/system/script_code.py
sudo chmod +x /lib/systemd/system/script_code.py

sudo chmod 644 /lib/systemd/system/rm.service
sudo chmod 644 /lib/systemd/system/script_rm.py
sudo chmod +x /lib/systemd/system/script_rm.py


sudo systemctl daemon-reload

sudo systemctl enable db.service
sudo systemctl start db.service

sudo systemctl enable code.service
sudo systemctl start code.service

sudo systemctl enable rm.service
sudo systemctl start rm.service




