# create a file using puppet
$name = '/temp/school'
$text = 'I love Puppet'
$ow_grp = 'www-data'

file { $name:
  mode    => '0744',
  owner   => $ow_grp,
  group   => $ow_grp,
  content => $text,
}
