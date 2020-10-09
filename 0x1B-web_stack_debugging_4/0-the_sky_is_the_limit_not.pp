# change open file limit

exec { 'fix':
  command => "sed -i 's/15/2000/g' /etc/default/nginx",
  path    => '/bin'
}