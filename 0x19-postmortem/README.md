<h1>Based on 0x17. Web stack debugging #3</h1>


# Postmortem Report: Apache 500 Error Incident


# Issue Summary:

from the time Fri, 24 Mar 2017  07:33 to 7:35 GMT An unexpected 500 Internal Server Error occurred on our Apache web server, it affected 100% of users who tried to reach the server. the root cause was the presence of a configuration file with incorrect file extension (.phpp) instead (.php).

# Timeline :

07:32: we noticed that curl requests to the server return 500 type error

07:32:  we used to tmux to run curl and strace  simultaneously to diagnose the issue concurrently.

7:33:  we used strace to find the problem and watched the whole process behind the request and searched for the incorrect file extension using grep

7:34:  we used the puppet method to apply changes into files in an automated way and fix the problem

7:35: we restarted the server and tried a new curl and requests returned 200 ok

# Root cause :

the root cause of the outage was an unrecognized file extension (.phpp) in place of the standard.php extension.<br> This led to Apache failing to load the intended configuration properly, resulting in the 500 error.
# Corrective and preventative measures :
we traced the process from the beginning and found the path of the incorrect extension file.<br> We used  puppet to automatedly change the extension to "php" instead of "phpp" and fix the problem

# Preventive Measures:
<b>Mointering </b>: using strace to monitor what behind a process and find the broken point

<b>Configuration Management</b>: using automated methods like puppet and checking the server status every time after editing to reduce the human errors

<b>Testing</b>: test connection before deploying
