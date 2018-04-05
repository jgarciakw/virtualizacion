import os
import time
import json
from subprocess import call

def ejecutar(paths):
    #print("Borrando copias antiguas......")
    #call(['mysqldump', '-uroot', '-pcapitantrueno', '--opt', '--all-databases', '>', path])
    os.system('find ' + paths[0]['rutaDb'] +' -type f -mmin +120 -exec rm {} \;')

    #print("Desmontado particion.........")
    call(['umount', paths[0]['rutaBack']])


def cargarJson():
    with open('data.json') as f:
        config = json.load(f)

    return config


paths = cargarJson()

while True:

    time.sleep(paths[1]['tiempo_rm']*3600)

    if os.path.exists(paths[0]["rutaBack"]):
        #print("Montando particion --> /mnt/backup")
        call(['mount', '-t', 'nfs', paths[0]["rutaDisk"], paths[0]["rutaBack"]])

        if os.path.ismount(paths[0]["rutaBack"]):
            ejecutar(paths)

    else:
        #print("Creando directorio --> /mnt/backup")
        os.mkdir(paths[0]["rutaBack"])

        #print("Montando particion --> /mnt/backup")
        call(['mount', '-t', 'nfs', paths[0]['rutaDisk'], paths[0]['rutaBack']])

        if os.path.ismount(paths[0]["rutaBack"]):
            #print("Creando directorio --> /mnt/backup/rbpj")
            os.mkdir(paths[0]["rutaRbpj"])

            #print("Creando directorio --> /mnt/backup/rbpj/code")
            os.mkdir(paths[0]["rutaCode"])

            #print("Creando directorio --> /mnt/backup/rbpj/db")
            os.mkdir(paths[0]["rutaDb"])

            ejecutar(paths)