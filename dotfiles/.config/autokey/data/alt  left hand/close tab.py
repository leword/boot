if re.match('.*chrome.*', window.get_active_class()):
    keyboard.send_keys("<ctrl>+w")
else:
    keyboard.send_keys("<alt>+w")

