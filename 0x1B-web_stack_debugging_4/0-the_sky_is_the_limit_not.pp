# Edit stack user limit
exec { 'user limit':
  onlyif   => 'test -e /etc/default/nginx',
  command  => 'sed -i "5s/[0-9]\+/$( ulimit -n )/" /etc/default/nginx; service nginx restart',
  provider => shell,
}
