# Set up my client SSH configuration file
file { '/root/.ssh/config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => '# My school server configuration
Host school
  HostName 54.197.78.222
  User ubuntu
  IdentityFile ~/.ssh/school
  PasswordAuthenticatio no
'
}
