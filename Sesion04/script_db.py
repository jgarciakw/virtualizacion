import os
import time
import json
from subprocess import call


def ejecutar(paths):
    nombre = time.strftime("%d-%m-%Y-%H:%M",time.gmtime())
    print("Creando copia de la base de datos.........")
    #call(['mysqldump', '-uroot', '-pcapitantrueno', '--opt', '--all-databases', '>', path])
    os.system('mysqldump -uroot -pcapitantrueno --opt --all-databases > /mnt/backup/rbpj/db/' + nombre + '.sql')

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
