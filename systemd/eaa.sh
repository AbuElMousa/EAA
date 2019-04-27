route add default gw 192.168.7.2
echo "nameserver 8.8.8.8" > etc/resolv.conf
/usr/bin/python3 /home/debian/EAA/eaa/manage.py runserver 192.168.7.2:8081
