keyboard.send_keys("<home>")
keyboard.send_keys("<shift>+<end>")
if re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<shift>+<ctrl>+x")
else:
    keyboard.send_keys("<ctrl>+x")

