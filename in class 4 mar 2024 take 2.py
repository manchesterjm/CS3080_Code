def a_func(a, b) :
    try:
        a / b
    except Exception as e :
        print('we found an exception')
    
a_func(1, 0)
    