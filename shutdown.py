def shutdown(p1,p2):
    diff = p1.find('B')-p2.find('B')
    print(p1)
    print(p2)
    if diff<0:
        return 'Gunfighter 1 wins!'
    elif diff>0:
        return 'Gunfighter 2 wins!'
    else:
        return 'Tie'
   
print(shutdown('                Bang!  ', '          Bang!'))