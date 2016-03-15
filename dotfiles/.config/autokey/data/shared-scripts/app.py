import re

def rubymine(w):
  return re.match('.*Proxy.*',w.get_active_class())

def chrome(w):
  return re.match('.*chrome.*',w.get_active_class())

def terminal(w):
  return re.match('.*terminal.*',w.get_active_class())


