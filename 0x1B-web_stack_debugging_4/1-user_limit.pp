# Change file limits for user holberton
class open_file_limit {
  $new_limit = 65535
  $username = 'holberton'
  $limits_conf = '/etc/security/limits.conf'
  $limits_line = "$username soft nofile $new_limit\n$username hard nofile $new_limit"

  package { 'sed':
    ensure => installed,
  }

  file_line { 'increase_file_limits':
    path    => $limits_conf,
    line    => $limits_line,
    match   => "^$username",
    ensure  => present,
    require => Package['sed'],
    notify  => Exec['reload_sysctl'],
  }

  exec { 'reload_sysctl':
    command     => '/sbin/sysctl -p',
    refreshonly => true,
  }

  user { $username:
    ensure => present,
  }
}
