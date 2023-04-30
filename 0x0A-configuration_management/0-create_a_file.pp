# create a file using puppet
$path = '/tmp/school'
$text = 'I love Puppet'
$ow_grp = 'www-data'

file { 'school':
  mode    => '0744',
  owner   => $ow_grp,
  group   => $ow_grp,
  content => $text,
  path    => $path,
}
