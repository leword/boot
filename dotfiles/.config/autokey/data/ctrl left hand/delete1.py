if re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<ctrl>+d") 
else:
    keyboard.send_keys("<delete>")
    

    