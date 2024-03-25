# Using Puppet, install flask from pip3

exec { 'install_flask':
  command => 'pip3 install Flask==2.1.0',
  path    => '/usr/bin',
  unless  => 'pip3 show Flask | grep "Version: 2.1.0"',
}
