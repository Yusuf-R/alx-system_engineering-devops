# kills a process named killmenow.

exec { 'killmenow':
  command => 'pkill -9 $(ps aux | grep "killmenow"',
  }
