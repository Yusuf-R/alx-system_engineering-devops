# create a file using puppet
$path = '/tmp/school'
$text = 'I love Puppet'
$ow_grp = 'www-data'
$name = 'school_ins'

file { $name:
  mode    => '0744',
  owner   => $ow_grp,
  group   => $ow_grp,
  content => $text,
  path    => $path,
}
