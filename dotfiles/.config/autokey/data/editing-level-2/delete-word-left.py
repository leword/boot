import app
if app.terminal(window):
    keyboard.send_keys("<alt>+<backspace>")
else:
    keyboard.send_keys("<ctrl>+<backspace>")

