# Using Puppet, install flask from pip3
# using ensure to get a specific version
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

package {'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}
