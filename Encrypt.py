def Encrypt():
    import string
    a = string.ascii_lowercase
    code = raw_input("Please enter your code: ")
    plus_num = int(raw_input("How many do you want your code of text to move forward? "))
    while plus_num > 25:
            plus_num = int(raw_input("You move too much! Please retype the step: "))        
    code_new = ""
    for i in code:
        if i in string.ascii_lowercase:
            code_new += a[a.index(i)+plus_num]
        else:
            code_new += i
    print "Your new code is: %s" %code_new
