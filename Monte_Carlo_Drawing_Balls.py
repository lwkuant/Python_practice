def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    import random
    same = 0
    for i in range(numTrials):
        balls = ["r","r","r","g","g","g"]
        draw = []
        while len(balls)>3:
            drawn_ball = random.choice(balls)
            draw.append(balls.pop(balls.index(drawn_ball)))
        for j in range(len(draw)):
            check = True
            if j != (len(draw)-1) and draw[j] != draw[j+1]:
                check = False
                break
        if check:
            same+=1
    return float(same)/numTrials            
