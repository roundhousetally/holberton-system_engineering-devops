# change open file limit

exec { 'fix':
  command => "sed -i 's/15/30000/g' /etc/default/nginx",
  path    => '/bin'
}