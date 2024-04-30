# custom http request header
package {'nginx':
  ensure  => 'installed',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                try_files / =404;
                add_header X-Served-By $(hostname);
        }
}",
  require => Package['nginx']
}
# to applaya restart
service { 'nginx':
  ensure => running,
  enable => true,
}
