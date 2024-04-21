# using Puppet to make changes to our configuration file.
# Just as in the previous configuration file task
# we’d like you to set up your client SSH configuration file
# so that you can connect to a server without typing a password.
# (edit_config_file) is the name of process
file {'edit_config_file':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  content => 'Host *
IdentityFile "~/.ssh/school"
PasswordAuthentication no',
}
