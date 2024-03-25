# Using Puppet, install flask from pip3.


exec {'apt-get update':
  command => '/user/bin/apt-get update'
}
package { 'flask':
  ensure  => 'installed'
  require => Exec [apt-get flask]
}
