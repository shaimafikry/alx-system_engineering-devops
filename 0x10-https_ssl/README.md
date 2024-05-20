<b>What is HTTPS SSL 2 main roles? </b>

	- authentication
	- encrypt decrypt
<b>What is the purpose encrypting traffic</b>

	- keep the connection secure

<b>What SSL termination means</b>

	- end way communication

when we configure haproxy file we have to add the fullchain.pem and the privte key.pem together at one file 
and name it after the domain name.pem

and then add this file to haproxy.cfg as ssl crt path_to_the_new_file ==> see 1-haproxy_ssl_termination
