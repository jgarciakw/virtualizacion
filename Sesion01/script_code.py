import os
import time
from subprocess import call

rutaDisk="158.49.112.72:/volume2/pve73"
rutaRbpj="/mnt/backup/rbpj"
rutaBack="/mnt/backup"
rutaCode="/mnt/backup/rbpj/code"
rutaDb="/mnt/backup/rbpj/db"
rutaSql="/mnt/backup/rbpj/db/ruben"
baseDatos="/var/lib/mysql/ruben"


def ejecutar():
    print("Creando copia del directorio /etc.......")
    call(['rsync', '-avz', '--delete', '--backup', '/etc', rutaCode])

    print("Creando copia del directorio /var/www.........")
    call(['rsync', '-avz', '--delete', '--backup', '/var/www', rutaCode])

    print("Desmontado particion.........")
    call(['umount', rutaBack])



if os.path.exists(rutaBack):
    print("Montando particion --> /mnt/backup")
    call(['mount', '-t', 'nfs', rutaDisk, rutaBack])

    if os.path.ismount(rutaBack):
        ejecutar()

else:
    print("Creando directorio --> /mnt/backup")
    os.mkdir(rutaBack)

    print("Montando particion --> /mnt/backup")
    call(['mount', '-t', 'nfs', rutaDisk, rutaBack])

    if os.path.ismount(rutaBack):
        print("Creando directorio --> /mnt/backup/rbpj")
        os.mkdir(rutaRbpj)

        print("Creando directorio --> /mnt/backup/rbpj/code")
        os.mkdir(rutaCode)

        print("Creando directorio --> /mnt/backup/rbpj/db")
        os.mkdir(rutaDb)

        ejecutar()









