# Manifest to manage SSH configuration using file_line
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/root/.ssh/config',
  line   => '    PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/root/.ssh/config',
  line   => '    IdentityFile ~/.ssh/school',
  }
