# This Puppet manifest sets the file descriptor limits for the holberton user
# to avoid "Too many open files" errors during login and file operations.

exec { 'set_file_limits_for_holberton':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'echo "holberton soft nofile 4096" >> /etc/security/limits.conf && echo "holberton hard nofile 8192" >> /etc/security/limits.conf && grep -q "session required pam_limits.so" /etc/pam.d/common-session || echo "session required pam_limits.so" >> /etc/pam.d/common-session && grep -q "session required pam_limits.so" /etc/pam.d/common-session-noninteractive || echo "session required pam_limits.so" >> /etc/pam.d/common-session-noninteractive',
  provider => 'shell',
}

