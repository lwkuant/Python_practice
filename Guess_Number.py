def guess_num():
    import random
    num = random.randrange(1, 101)
    
    check = False
    count = 0
    
    while check == False:
        guess = int(raw_input("Guess a number between 1 and 100: "))                                                                
        count += 1
        
        if guess > num:
            print("Too big!")
        elif guess < num:
            print("Too small!")
        else:
            check = True
            print("Bravo!")
            print("You've made "+str(count)+" guesses!")                                    