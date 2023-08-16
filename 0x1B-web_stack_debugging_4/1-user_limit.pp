# Change the OS configuration user limit
# `holberton` user can now open a file without any error message.

# increase the hard limits for the `holberton` user
exec { 'increase-hard-file-limit':
  command => 'sed -i "/holberton hard/s/5/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# increase the soft limits for the `holberton` user
exec { 'incrase-soft-file-limit':
  command => 'sed -i "/holberton soft/s/4/4000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
