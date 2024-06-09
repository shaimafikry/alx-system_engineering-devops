# debugging #3

strace:
	walk with you step by step to execute a command
	it take the process id and trace it, shows every file it visit and every line it execute
	it also show errors, so it make it easier to debug something.

# how to trace using an pid ?
	sudo strcae -p process_id

# why using tmux in this task?
	to make it easy to run more than one window at the same time as strace works Simultaneously
	with the process while tracing it

# how puppet would solve it ?
	 after know which file is causing the error we use puppet to  get the file location
	 and chaage the error found earlier

# what is the error here?
	the extension of "php" is "phpp" in the file located in var/www/html
	so we use the file path in puppt and change the extension using sed command

# note :
	the colon (:) in the path here is to  to include both directories.
	/usr/locate/bin/ and /bin/
