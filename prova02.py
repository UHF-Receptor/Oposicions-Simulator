import random
examens =0
suspesos =0
for i in range(100000):
    examens +=1
    a = 1+ (70*random.random()) // 1
    b=a
    while b ==a:
        b =1+ (70*random.random()) // 1
    c=b
    while c == a or c ==b:
        c = 1+(70*random.random()) // 1

    d=b
    while d == a or d ==b or d==c:
        d = 1+(70*random.random()) // 1

    e=b
    while e == a or e ==b or e==c or e==d:
        e = 1+(70*random.random()) // 1

    Melse = {2,3,4,5,7,9,15,16,18,22,23,26,29,30,31,36,37,38,39,40,45,49,50,51,54,57,62,65}
    aprovo =5
    if a not in Melse:
        aprovo-=1
    if b not in Melse:
        aprovo-=1
    if c not in Melse:
        aprovo-=1
    if d not in Melse:
        aprovo-=1
    if e not in Melse:
        aprovo-=1
    if aprovo == 0:
        print('No aprovo')
        suspesos +=1
    else:
        print('Aprovo')

print('De un total de {} fets, en suspendria {} i ne aprovaria {}.'.format(examens,suspesos,examens-suspesos))
