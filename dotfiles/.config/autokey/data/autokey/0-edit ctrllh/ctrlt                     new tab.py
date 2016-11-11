if re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<alt>+t")
else:
    keyboard.send_keys("<ctrl>+t")

