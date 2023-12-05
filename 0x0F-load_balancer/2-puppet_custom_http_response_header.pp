# Install and configure `Nginx` web server to have a custome header
exec { 'apt_update':
  command => 'apt-get update',
  path    => '/usr/bin:/usr/sbin'
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt_update']
}

exec { 'custom_header':
  command => "sudo sed -i '/server_name _;/a \\ \n\tadd_header X-Served-By \"${hostname}\";' /etc/nginx/sites-available/default",
  path    => '/usr/bin:bin'
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx']
}
