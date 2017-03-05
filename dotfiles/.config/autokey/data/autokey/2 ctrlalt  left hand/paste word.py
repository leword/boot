keyboard.send_keys("<ctrl>+<left>")
keyboard.send_keys("<ctrl>+<shift>+<right>")
if re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<shift>+<ctrl>+v")
else:
    keyboard.send_keys("<ctrl>+v")

