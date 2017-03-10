if re.match('.*Proxy.*', window.get_active_class()):
    keyboard.send_keys("<alt>+w")
else:
    keyboard.send_keys("<ctrl>+<left>")
    keyboard.send_keys("<ctrl>+<shift>+<right>")
    

    