# Using Puppet, install flask from pip3

exec { 'pip3_update':
  command => '/usr/bin/pip3 update'
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  require => Exec['pip3_update']
}
