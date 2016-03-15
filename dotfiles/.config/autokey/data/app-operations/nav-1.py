import app
if app.chrome(window):
    keyboard.send_keys("<ctrl>-L") # url bar
else
    keyboard.send_keys("<alt>+e")