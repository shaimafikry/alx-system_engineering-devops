# updte app list
exec {'update':
  command => 'apt-get -y update',
}

Package {'nginx':
  ensure  => 'installed',
  provider=> 'pip3',
  require => Exec ['update'],
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Hello World!\n",
  require => Package ['nginx']
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
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

exec { 'nginx_restart':
  command => 'sudo service nginx restart',
  require => File['port_config'],
}
