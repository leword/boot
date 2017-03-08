if re.match('.*Proxy.*',window.get_active_class()):
    keyboard.send_keys("<alt>+<delete>")
elif re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<ctrl>+k") 
else:
    keyboard.send_keys("<shift>+<end>")
    keyboard.send_keys("<delete>")
    

    