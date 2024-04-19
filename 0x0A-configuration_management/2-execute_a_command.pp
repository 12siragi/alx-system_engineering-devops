# This Puppet manifest kills a process named "killmenow" using the exec resource and pkill command.

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  refreshonly => true,
}
