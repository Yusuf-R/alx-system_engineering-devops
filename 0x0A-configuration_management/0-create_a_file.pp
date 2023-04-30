# create a file using puppet
$ow_grp = 'www-data'
$text = 'I love Puppet'

# Create /tmp directory if it does not exist
file { '/tmp':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

# Create school file in /tmp directory
file { '/tmp/school':
  content => $text,
  owner   => $ow_grp,
  group   => $ow_grp,
  mode    => '0744',
}

