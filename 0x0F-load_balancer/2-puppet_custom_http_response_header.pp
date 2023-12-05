# Install and configure `Nginx` web server to have a custome header
exec { 'apt_update':
  command => 'apt-get update',
  path    => '/usr/bin:/usr/sbin',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt_update'],
}

file_line { 'add_custom_header':
  path  => '/etc/nginx/sites-available/default',
  line  => "\n\tadd_header X-Served-By ${hostname};",
  after => 'server_name _;',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
