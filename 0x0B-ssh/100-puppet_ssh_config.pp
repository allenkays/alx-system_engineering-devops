# using Puppet to make changes to our configuration file
# SSH client configuration must be configured to use the private key ~/.ssh/school
# SSH client configuration must be configured to refuse to authenticate using a password

file_line {'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
file_line{'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
