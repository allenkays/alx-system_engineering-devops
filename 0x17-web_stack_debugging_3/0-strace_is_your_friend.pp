# Change phpp extension typo to php in the WordPress file wp-settings.php.

exec { 'Edit-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
