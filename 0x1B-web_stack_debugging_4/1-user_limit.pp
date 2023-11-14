# Update the OS configuration so that it is posible to login with
#   the holberton user and open a file without any error message.


# Soft nofile limit : user receives warnings when reaching this limit 
#      but can exceed it temporarily (up to the hard limit).

exec {'update the soft number of file descriptors limit for holberton user':
command  => 'sudo sed -i "s/holberton\ssoft.*/holberton\tsoft\tnofile\t1024/" /etc/security/limits.conf',
provider => shell,
before   => Exec['update the hard number of file descriptors limit for holberton user'],
}

# Hard nofile limit : maximum value that a user or process cannot exceed. 

exec {'update the hard number of file descriptors limit for holberton user':
command  => 'sudo sed -i "s/holberton\shard.*/holberton\tsoft\tnofile\t4096/" /etc/security/limits.conf',
provider => shell
}
