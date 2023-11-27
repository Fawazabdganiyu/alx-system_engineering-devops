# Manifest to manage SSH configuration using augeas
augeas { 'ssh_config':
  incl    => '/etc/ssh/ssh_config',
  lens    => 'Ssh.lns',
  context => '/etc/ssh/ssh_config',
  changes => [
    'set Host 54.197.78.222',
    'set Host[.="54.197.78.222"]/HostName 54.197.78.222',
    'set Host[.="54.197.78.222"]/User ubuntu',
    'set Host[.="54.197.78.222"]/IdentityFile ~/.ssh/school',
    'set Host[.="54.197.78.222"]/PasswordAuthentication no',
  ],
}
