import os
import time
import json
from subprocess import call


def ejecutar(paths):
    nombre = time.strftime("%d-%m-%Y-%H:%M",time.localtime())
    #print("Creando copia de la base de datos.........")
    #call(['mysqldump', '-uroot', '-pcapitantrueno', '--opt', '--all-databases', '>', path])
    os.system('mysqldump -uroot -pcapitantrueno --opt --all-databases > /mnt/backup/rbpj/db/' + nombre + '.sql')

    #print("Desmontado particion.........")
    call(['umount', paths[0]['rutaBack']])


def cargarJson():
    with open('/home/alumno/sesion4/data.json') as f:
        config = json.load(f)

    return config


paths = cargarJson()

while True:

    time.sleep(paths[1]['tiempo_db']*3600)

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