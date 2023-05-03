# configures server using puppet

# Update the apt manage list
exec {'Update the apt manager':
  command => '/usr/bin/env apt-get -y update',
}

# Install the Nginx server
exec { 'install nginx server':
  command =>'/usr/bin/env apt-get -y install nginx',
}

# Our custom default page
# Using nginx-debian html for our default landing in this instance
exec {'custom default page':
  command => '/usr/bin/env echo "Hello World" > /var/www/html/index.nginx-debian.html'
}

# Using holberton as the domain name rather than our own
# this setting up another server block for our nginx
exec {'performing a move to pemnanet':
  command => '/usr/bin/env sed -i "/server_name _;/ a\\\trewrite ^/redirect_me http://www.tavish.tech permanent;" /etc/nginx/sites-available/default',
}

# Handling our error page
exec {'Handle error page request':
  command => '/usr/bin/env sed -i "/server_name _;/ a\\\terror_page 404 /custom_404.html;" /etc/nginx/sites-available/default',
}

#Setting up our own default error 404 page
exec {'Our default error 404 page':
  command => 'usr/bin/env echo "Ceci n\'est pas une page" > /var/www/html/custom_404.html',
}

# Starting our nginx server after all the set up
exec {'Start the nginx service':
  command => '/usr/bin/env service nginx start'
}
