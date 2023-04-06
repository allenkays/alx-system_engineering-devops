# Setup nginx server
include stdlib
class nginx_server {
  package { 'nginx':
    ensure => 'installed',
  }

  file { '/etc/nginx/html/index.html':
    content => 'Hello World!',
  }

  file { '/etc/nginx/sites-available/default':
    content => template('/etc/puppet/code/modules/nginx/default.conf.erb'),
    notify  => Service['nginx'],
  }
  file_line { 'redirect':
    ensure => 'present',
    path   => '/etc/nginx/sites-available/default',
    after  => 'listen 80 default_server;',
    line   => 'rewrite ^/redirect_me https://www.google.com/ permanent;',
  }

  exec { 'enable-default-site':
    command => '/bin/ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default',
    creates => '/etc/nginx/sites-enabled/default',
    require => [File['/etc/nginx/sites-available/default'], File_line['redirect']],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => [Package['nginx'], Exec['enable-default-site']],
  }
}

include nginx_server
