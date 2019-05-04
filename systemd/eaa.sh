#route add default gw 192.168.7.2
#echo "nameserver 8.8.8.8" > etc/resolv.conf
rm /home/debian/EAA/eaa/db.sqlite3
sleep 1
/usr/bin/python3 /home/debian/EAA/eaa/manage.py makemigrations
/usr/bin/python3 /home/debian/EAA/eaa/manage.py migrate --run-syncdb
sqlite3 /home/debian/EAA/eaa/db.sqlite3 "INSERT INTO sounds_sound values (1, 2, 3, 4, 5)"
sqlite3 /home/debian/EAA/eaa/db.sqlite3 "INSERT INTO configuration_configuration values (1, 440, 10, 0)"
sleep 1
/usr/bin/python3 /home/debian/EAA/eaa/manage.py runserver 192.168.7.2:8081 --noreload
