modprobe -r uio_pruss
modprobe uio_pruss_extram_pool_sz=0x800000
sleep 30
/usr/bin/python /home/debian/EAA/localizer/localizer.py
