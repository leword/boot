if re.match('.*chrome.*', window.get_active_class()):
    keyboard.send_keys("<ctrl>+f")
else:
    keyboard.send_keys("<alt>+s")

