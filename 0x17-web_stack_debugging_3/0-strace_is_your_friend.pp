# Using strace to resolve the internal server Error (500)
exec { 'fixed-phpp':
        command  => 'sed -i "s//class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php"',
        path     => '/bin',
        provider => 'shell',
}
