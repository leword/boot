import app
if app.terminal(window):
    keyboard.send_keys("<alt>+d")
else:
    keyboard.send_keys("<ctrl>+<delete>")

