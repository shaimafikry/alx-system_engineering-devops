# What is the main role of a database
	store all data needed by user with easy access and edit

# What is a database replica

# What is the purpose of a database replica
	to easy distribute it between servers when usinf load balancer
	Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data

Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed


Why database backups need to be stored in different physical locations
	to make sure its safe when servers a re broken

What operation should you regularly perform to make sure that your database backup strategy actually works
