if re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<ctrl>+<shift>+v")
else:
    keyboard.send_keys("<ctrl>+v")

