#!/usr/bin/pup
# Puppet: install Flask using pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
require  => Package['python3-pip'],
}
