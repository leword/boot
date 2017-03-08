if re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("W")
    keyboard.send_keys("<ctrl>+a")
    keyboard.send_keys("]")                      
else:
    keyboard.send_keys("<alt>+<down>")