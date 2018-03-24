import os
import time
import json
from subprocess import call


def ejecutar(paths):
    print("Creando copia del directorio /etc.......")
    call(['rsync', '-avz', '--delete', '--backup', '/etc', paths['rutaCode']])

    print("Creando copia del directorio /var/www.........")
    call(['rsync', '-avz', '--delete', '--backup', '/var/www', paths['rutaCode']])

    print("Desmontado particion.........")
    call(['umount', paths['rutaBack']])



def cargarJson():
    with open('data.json') as f:
        config = json.load(f)

    return config


paths = cargarJson()

if os.path.exists(paths["rutaBack"]):
    print("Montando particion --> /mnt/backup")
    call(['mount', '-t', 'nfs', paths["rutaDisk"], paths["rutaBack"]])

    if os.path.ismount(paths["rutaBack"]):
        ejecutar(paths)

else:
    print("Creando directorio --> /mnt/backup")
    os.mkdir(paths["rutaBack"])

    print("Montando particion --> /mnt/backup")
    call(['mount', '-t', 'nfs', paths['rutaDisk'], paths['rutaBack']])

    if os.path.ismount(paths["rutaBack"]):
        print("Creando directorio --> /mnt/backup/rbpj")
        os.mkdir(paths["rutaRbpj"])

        print("Creando directorio --> /mnt/backup/rbpj/code")
        os.mkdir(paths["rutaCode"])

        print("Creando directorio --> /mnt/backup/rbpj/db")
        os.mkdir(paths["rutaDb"])

        ejecutar(paths)
