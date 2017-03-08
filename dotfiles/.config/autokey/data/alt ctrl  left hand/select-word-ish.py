if re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("W")
else:
    keyboard.send_keys("<ctrl>+<left>")
    keyboard.send_keys("<ctrl>+<shift>+<right>")
    keyboard.send_keys("<ctrl>+c")

    