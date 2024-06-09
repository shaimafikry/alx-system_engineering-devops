# Using Puppet, to change extension of files
# the proplem is that extensions of php is phpp

exec { 'fix the extension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
}
