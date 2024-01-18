# Fix the typo in /var/www/html/wp-settings.php
exec { 'fix-wp-settings-typo':
  command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
}
