if re.match('.*Proxy.*',window.get_active_class()):
    keyboard.send_keys("<ctrl>+y")
elif re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<ctrl>+u") 
    keyboard.send_keys("<ctrl>+k") 
else:
    keyboard.send_keys("<end>")
    keyboard.send_keys("<shift>+<home>")
    keyboard.send_keys("<shift>+<home>")
    keyboard.send_keys("<delete>")
    keyboard.send_keys("<backspace>")
    keyboard.send_keys("<home>")
    

    