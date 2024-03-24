# Using Puppet, create a file in /tmp.

$file_name = '/tmp/school'

file { $file_name:
  ensure  => 'present',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
