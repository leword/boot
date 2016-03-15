import app

if app.chrome(window):
  keyboard.send_keys("<shift>+<end>")
  keyboard.send_keys("<delete>")
else:
  keyboard.send_keys("<ctrl>+k")
