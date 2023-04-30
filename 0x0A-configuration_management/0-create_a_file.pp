# create a file using puppet
$name = '/tmp/school'
$path = '/tmp'
$text = 'I love Puppet'
$ow_grp = 'www-data'

file { $name:
  ensure  => 'present',
  mode    => '0744',
  owner   => $ow_grp,
  group   => $ow_grp,
  content => $text,
}
