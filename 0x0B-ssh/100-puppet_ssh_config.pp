# Set up my client SSH configuration file
file_line { 'ssh_config':
  ensure => present,
  path   => '/etc/ssh/sshd_config',
  line   => '    IdentityFile ~/.ssh/school',
}

file_line { 'ssh_config':
  ensure => present,
  path   => '/etc/ssh/sshd_config',
  line   => '    PasswordAuthentication no',
}
