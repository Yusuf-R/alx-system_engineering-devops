# Increase the base limit of demon process to handle high volume request
exec { 'Incrase-nginx-daemon-limit':
        command  => "sed -i 's/LIMIT=\"-n 15\"/LIMIT=\"-n 4096\"/g' /etc/default/nginx",
        path     => '/bin',
        provider => 'shell'
}
# Restart Nginx service
-> exec { 'Restart Nginx':
        command => 'sudo nginx restart',
        path    => '/etc/init.d/',
}
