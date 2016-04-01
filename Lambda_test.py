lambda_test = lambda x, y: x + y

li = [x**2 for x in xrange(10)]
print(map(lambda x: x**2, li))