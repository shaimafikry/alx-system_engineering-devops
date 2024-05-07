<h1>0x0E. Web stack debugging #1</h1>


<b>kill "$(pgrep 'nginx' | head -1)" </b>==> this bring up the first occurance of nginx process and kill it by its id, 
		to achive the requirement (service (init) must say that nginx is not running ← for real)


<b>pkill -f "nginx" ==> </b>The pkill -f "nginx" command does not kill the first occurrence of the process it finds;
		instead, it sends a signal to terminate all processes that match the given pattern

ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

<b>ln </b>==> to make a symbolic link

<b>-f </b>  ==> to to force its creation

<b>-s </b>  ==> to make it symbolic not hard link
