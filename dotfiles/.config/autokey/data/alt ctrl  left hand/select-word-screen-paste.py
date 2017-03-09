if re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("b")
    keyboard.send_keys(" ")
    keyboard.send_keys("w")
    keyboard.send_keys("h")
    keyboard.send_keys("h")
    keyboard.send_keys("<enter>")
    keyboard.send_keys("<ctrl>+b")
    keyboard.send_keys("]")  
else:
    keyboard.send_keys("<ctrl>+<left>")
    keyboard.send_keys("<ctrl>+<shift>+<right>")
    keyboard.send_keys("<ctrl>+c")

    