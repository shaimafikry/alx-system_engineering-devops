# using Puppet to make changes to our configuration file.
# Just as in the previous configuration file task
# we’d like you to set up your client SSH configuration file
# so that you can connect to a server without typing a password.

file {'edit_config_file':
  ensure  => 'present'
  path    => '/usr/vagrant/.ssh/config'
  content => 'Host *
IdentityFile "/usr/vagrant/.ssh/school"
PasswordAuthentication no',
}
