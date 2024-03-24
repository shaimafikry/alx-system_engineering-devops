<h1>SSH</h1>
how to genreate ?
	ssh-kegen <br>
	ssh-keygen -b 4096 => with long number of bytes? <br>
	ssh-keygen -l => display the finger print <br>
	ssh-keygen -p => to change passphrase <br>
<h> how Copying your Public SSH Key to a Server ?</h>
	* with with SSH-Copy-ID <br>
		ssh-copy-id username@remote_host <br>
	* without  <br>
		cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys" <br>
<h> NOTE: If you do not have password-based SSH access available,<br> you will have to add your public key to the remote server manually. </h>
	* copy your public key and then go to the remote server and past it into the serever
	"""echo public_key_string >> ~/.ssh/authorized_keys"""


<h>HOW to connect ?</h>
	ssh username@remote_host<br>
	* using file?<br>
	ssh -i ~/.ssh/school ubuntu@8.8.8.8 => the -i flag specifies the path to the private key file <br>
	*why cant use  cat ~/.ssh/school | ssh ubento@8.8.8.8?<br>
		because ssh doesnt read the output from the stdin,it expects the private key to be specified directly using the -i flag. <br>
*NOTES: <br>
	* to create RSA key pair, putting the filename to be saved and the pssphrase in one command<br>
	"""ssh-keygen -b 4096 -N betty -f holberton""" => check man ssh-keygen
*config NOTES:
	in your local and in your server there is a file called config:
		local => nano ~/.ssh/config
		server => sudo nano /etc/ssh/sshd_config (after making a connection)
			=> sudo service ssh restart (to save the changes)
		-in those files you specify how the connection between server and localhost be:
			 - without passwords?
			 - for specific users?
			 - for specific servers?..etc
