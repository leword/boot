keyboard.send_keys("<ctrl>+<left>")
keyboard.send_keys("<ctrl>+<shift>+<right>")
if re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<shift>+<ctrl>+x")
else:
    keyboard.send_keys("<ctrl>+x")

