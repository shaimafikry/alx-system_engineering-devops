Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

Requirements:

file {'edit_config_file':
  ensure => 'present'
  path => '/usr/root/.ssh/config'
  content => 'Host *
IdentityFile "~/.ssh/school"
PasswordAuthentication no',
}
