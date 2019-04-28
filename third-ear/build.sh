modprobe -r uio_pruss
modprobe uio_pruss extram_pool_sz=0x800000
gcc -Wall -o third-ear third-ear.c -lpruio
./third-ear
