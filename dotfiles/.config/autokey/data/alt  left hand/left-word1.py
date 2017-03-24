if re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<alt>+b")
else:
    keyboard.send_keys("<ctrl>+<left>")

