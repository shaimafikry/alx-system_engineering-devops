# updte app list
exec {'update':
  command => 'apt-get -y update',
}

Package {'nginx':
  ensure  => 'installed',
  provider=> 'apt',
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
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        # applyin redirect
        location /redirect_me {
                return 301;
        }
        location / {
             root /var/www/html;
        }
        }',
  require => Package ['nginx']
}

exec { 'nginx_restart':
  command => 'service nginx restart',
  require => File['/etc/nginx/sites-available/default'],
}
