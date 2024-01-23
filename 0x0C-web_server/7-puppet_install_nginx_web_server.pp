# Install Nginx package
package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/redirect_me':
  ensure  => file,
  content => "server {
    listen 80;

    server_name _;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}",
  notify => Service['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
