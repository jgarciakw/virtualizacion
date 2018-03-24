rutaDisk="158.49.112.72:/volume2/pve73"
rutaRbpj="/mnt/backup/rbpj"
rutaBack="/mnt/backup"
rutaCode="/mnt/backup/rbpj/code"
rutaDb="/mnt/backup/rbpj/db"
rutaSql="/mnt/backup/rbpj/db/ruben"
baseDatos="/var/lib/mysql/ruben"


if [ -d $rutaBack ]
then
echo "Montando particion --> /mnt/backup"
mount -t nfs $rutaDisk $rutaBack
else
echo "Creando directorio --> /mnt/backup"
mkdir "/mnt/backup"
echo "Montando particion --> /mnt/backup"
mount -t nfs $rutaDisk $rutaBack
echo "Creando directorio --> /mnt/backup/rbpj"
mkdir $rutaRbpj
fi



if [ -d  $rutaRbpj ]
then

if [ ! -d  $rutaCode ]
then
echo "Creando directorio --> /mnt/backup/rbpj/code"
mkdir $rutaCode
fi

if [ ! -d  $rutaDb ]
then
echo "Creando directorio --> /mnt/backup/rbpj/db"
mkdir $rutaDb
fi
nombre=$(date +%Y-%m-%d.%H.%M)
echo "Ruta detectada..........."
echo "Creando copia del directorio /etc........."
rsync -avz --delete --backup /etc $rutaCode
echo "Creando copia del directorio /var/www........."
rsync -avz --delete --backup /var/www $rutaCode
echo "Desmontado particion........."
umount "/mnt/backup"

else
echo "Error directorio........."
fi
