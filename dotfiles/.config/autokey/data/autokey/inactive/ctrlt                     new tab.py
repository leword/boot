if re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<ctrl>+<shift>+t")
else:
    keyboard.send_keys("<ctrl>+t")

