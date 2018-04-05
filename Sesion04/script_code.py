import os
import time
import json
from subprocess import call


def ejecutar(paths):
    print("Creando copia del directorio /etc.......")
    call(['rsync', '-avz', '--delete', '--backup', '/etc', paths[0]['rutaCode']])

    print("Creando copia del directorio /var/www.........")
    call(['rsync', '-avz', '--delete', '--backup', '/var/www', paths[0]['rutaCode']])

    print("Desmontado particion.........")
    call(['umount', paths[0]['rutaBack']])



def cargarJson():
    with open('data.json') as f:
        config = json.load(f)

    return config


paths = cargarJson()

while True:

    if os.path.exists(paths[0]["rutaBack"]):
        print("Montando particion --> /mnt/backup")
        call(['mount', '-t', 'nfs', paths[0]["rutaDisk"], paths[0]["rutaBack"]])

        if os.path.ismount(paths[0]["rutaBack"]):
            ejecutar(paths)

    else:
        print("Creando directorio --> /mnt/backup")
        os.mkdir(paths[0]["rutaBack"])

        print("Montando particion --> /mnt/backup")
        call(['mount', '-t', 'nfs', paths[0]['rutaDisk'], paths[0]['rutaBack']])

        if os.path.ismount(paths[0]["rutaBack"]):
            print("Creando directorio --> /mnt/backup/rbpj")
            os.mkdir(paths[0]["rutaRbpj"])

            print("Creando directorio --> /mnt/backup/rbpj/code")
            os.mkdir(paths[0]["rutaCode"])

            print("Creando directorio --> /mnt/backup/rbpj/db")
            os.mkdir(paths[0]["rutaDb"])

            ejecutar(paths)

    time.sleep(paths[1]['tiempo_code']*3600)