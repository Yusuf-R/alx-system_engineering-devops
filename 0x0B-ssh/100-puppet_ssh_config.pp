# Client configuration file using puppet
file { '/etc/ssh/ssh_config':
        ensure  => 'present'
        content => '
        Include /etc/ssh/ssh_config.d/*.conf
        Host *
	        IdentityFile ~/.ssh/school
	        PasswordAuthentication no
                SendEnv LANG LC_*
                HashKnownHosts yes
                GSSAPIAuthentication yes
                '
}
