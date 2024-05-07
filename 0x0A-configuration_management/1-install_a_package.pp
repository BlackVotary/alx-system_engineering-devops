# Install an especific version of flask (2.1.0)
# Install Python3 and pip3
package { 'python3':
  ensure => present,
}

package { 'python3-pip':
  ensure => present,
}

# Install Flask and Werkzeug
exec { 'install Flask and Werkzeug via pip3':
  command => 'pip3 install Flask==2.1.0 Werkzeug==2.1.1',
  path    => ['/bin', '/usr/bin'],
  unless  => 'pip3 show Flask | grep -q "Version: 2.1.0"',
}
