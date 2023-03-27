# Kill process using exec puppet resource

exec {'pkill':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
