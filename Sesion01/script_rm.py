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
    print("Borrando copias antiguas......")
    #call(['mysqldump', '-uroot', '-pcapitantrueno', '--opt', '--all-databases', '>', path])
    os.system('find ' + rutaDb +' -type f -mmin +120 -exec rm {} \;')

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
