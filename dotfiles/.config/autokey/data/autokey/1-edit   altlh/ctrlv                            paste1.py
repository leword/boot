# Enter script code
if re.match('.*chrome.*', window.get_active_class()):
    keyboard.send_keys("<ctrl>+<shift>+v")
elif re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<shift>+<ctrl>+v")
else:
    keyboard.send_keys("<ctrl>+v")

