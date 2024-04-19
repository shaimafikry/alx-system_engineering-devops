# Using Puppet, create a file in /tmp.
# use a file_name as a variable
$file_name = '/tmp/school'

file { $file_name:
  ensure  => 'present',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
