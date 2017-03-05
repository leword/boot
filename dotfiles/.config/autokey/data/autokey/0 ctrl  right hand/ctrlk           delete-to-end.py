# Enter script code
if re.match('.*Proxy.*',window.get_active_class()):
    keyboard.send_keys("<ctrl>+k")
elif re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<ctrl>+k") 
else:
    keyboard.send_keys("<shift>+<end>")
    keyboard.send_keys("<delete>")
    

    