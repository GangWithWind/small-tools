echo python `pwd`/netlogin.py "&" > run2.sh
chmod 770 run2.sh
sudo cp run2.sh /etc/init.d/
sudo update-rc.d -f run2.sh remove
