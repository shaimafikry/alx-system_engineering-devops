# Using Puppet, create a manifest that kills a process named killmenow.
# using pkill the get the process by name

exec { 'kill_killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
