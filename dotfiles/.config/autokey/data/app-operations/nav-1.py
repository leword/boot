import app
if app.chrome(window):
    keyboard.send_keys("<ctrl>-l") 
else:
    keyboard.send_keys("<alt>+e")