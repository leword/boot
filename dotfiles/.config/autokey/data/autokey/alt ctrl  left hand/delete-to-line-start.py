if re.match('.*Proxy.*',window.get_active_class()):
    keyboard.send_keys("<alt>+<backspace>")
elif re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<ctrl>+u") 
else:
    keyboard.send_keys("<shift>+<home>")
    keyboard.send_keys("<delete>")
    

    