# firewalls installation

# to allow incoming and outgoing connections
sudo ufw default deny incoming
sudo ufw default allow outgoing

# to know the available application
sudo ufw app list

# to add new ports and domain
sudo uwf allow from [doamin ip]

sudo uwf allow [port or sevice name or port ranges 00:00/tcp]

# how to redirect from port1 to port2
1- first we make the ports allowed on the ufw

	sudo ufw allow (port1)

	sudo ufw allow (port2)

2-  edit the file <b>/etc/ufw/sysctl.conf</b>

	* add or uncomment (if exist) the sentence that says

		net.ipv4.ip_forward=1

4- write " sudo sysctl -p " to refresh the server

5- open <b>/etc/ufw/before.reules</b> and add before the filter section
	
	*nat
	:PREROUTING ACCEPT [0:0]
	-A PREROUTING -p tcp --dport port1 -j REDIRECT --to-port port2
	COMMIT
	


6- we write " sudo systemctl restart ufw"


done 
