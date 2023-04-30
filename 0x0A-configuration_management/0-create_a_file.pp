# create a file using puppet
$path = '/temp/school'
$text = 'I love Puppet'
$ow_grp = 'www-data'

file { $path:
  mode    => '0744',
  owner   => $ow_grp,
  group   => $ow_grp,
  content => $text,
}
