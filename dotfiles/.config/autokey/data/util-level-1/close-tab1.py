import app

if app.rubymine(window):
  keyboard.send_keys("<alt>+w")
else:
  keyboard.send_keys("<ctrl>+w")
  