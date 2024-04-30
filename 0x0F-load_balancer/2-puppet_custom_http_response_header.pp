# custom http request header
package {'nginx':
  ensure  => 'installed',
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Hello World!\n",
  require => Package['nginx']
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => 'server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                try_files / =404;
                add_header X-Served-By $(hostname);
        }
        # applyin redirect
        location /redirect_me {
                return 301;
        }
}',
  require => Package['nginx']
}
# to applaya restart
service { 'nginx':
  ensure => running,
  enable => true,
}
