package { 'nginx':
  ensure => 'present',
}

file { '/etc/nginx/html/index.html':
  content => 'Hello World!',
}

file_line { 'File':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.google.com/ permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
