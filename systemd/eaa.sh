#route add default gw 192.168.7.2
#echo "nameserver 8.8.8.8" > etc/resolv.conf
rm /home/debian/EAA/eaa/db.sqlite3
sleep 1
/usr/bin/python3 /home/debian/EAA/eaa/manage.py migrate --run-syncdb
sleep 1
<<<<<<< HEAD
/usr/bin/python3 /home/debian/EAA/eaa/manage.py runserver 192.168.7.2:8081 --noreload
=======
/usr/bin/python3 /home/debian/EAA/eaa/manage.py runserver 192.168.7.2:8081
>>>>>>> 7ea9d474c8671663bbc5024172449607fbfa7c2d
