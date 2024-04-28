# updte app list
exec {"update":
  command => 'apt-get -y update',
}

Package {"nginx":
  ensure  => "installed",
  provider=> 'apt',
  require => Exec ['update'],
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Hello World!\n",
  require => Package ['nginx']
}

file { "port_congfig":
  ensure  => "present "
  path    => '/etc/nginx/sites-available/default',
  content => 'server {
                listen 80 default_server;
                server_name _;
				location /redirect_me {
					return 301;
				}
                location / {
                    root /var/www/html;
                    index index.html;
                }
              }',
  require => Package ['nginx']
}

server nginx restart
