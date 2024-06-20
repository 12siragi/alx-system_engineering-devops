# 0-strace_is_your_friend.pp
exec { 'fix-typo-in-wp-settings':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  onlyif  => 'grep phpp /var/www/html/wp-settings.php',
}
