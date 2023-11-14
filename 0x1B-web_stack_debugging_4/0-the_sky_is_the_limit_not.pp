# Update nginx file descriptor's limit from the default to the
#    max to handle fulfill more connection

exec { 'Update nginx file descriptors limit to the max to handle more connection':
    command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx && sudo service nginx restart',
    provider => shell,
}
