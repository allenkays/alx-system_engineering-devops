#create a file using puppet in /tmp

file {'/tmp/school':
  ensure  => 'present',
  owner   => 'www-data',
  mode    => '0744',
  group   => 'www-data',
  content => 'I love Puppet',
}
