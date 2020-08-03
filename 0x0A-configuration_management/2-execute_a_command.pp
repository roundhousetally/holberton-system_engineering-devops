# This manifest kills a process names killmenow
exec { 'killest' :
  command  => "pkill killmenow",
  provider => 'shell',
}