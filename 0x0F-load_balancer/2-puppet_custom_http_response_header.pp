# custom http request header
package {'nginx':
  ensure  => 'installed',
}

file_line { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;'
  require => Package['nginx']
}
# to applaya restart
service { 'nginx':
  ensure => running,
  enable => true,
}
