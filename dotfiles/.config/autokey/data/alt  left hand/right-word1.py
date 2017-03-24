if re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<alt>+f")
else:
    keyboard.send_keys("<ctrl>+<right>")

