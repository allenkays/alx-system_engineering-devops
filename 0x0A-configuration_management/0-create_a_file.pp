file { 'school':
path    => '/tmp/school'
owner   => 'www-data'
mode    => '0744'
group   => 'www-data'
content => "I love puppet"
}
