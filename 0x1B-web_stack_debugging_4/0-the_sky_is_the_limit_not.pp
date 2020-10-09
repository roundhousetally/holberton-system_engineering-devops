# change open file limit

exec { 'fix':
  command => "sed -i 's/15/3000/g' /etc/default/nginx; service nginx restart",
  path    => ['/bin', '/usr/bin']
}