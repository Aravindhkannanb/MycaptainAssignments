y = range(0,10)
answer =[]               
for i in y:
    x = list(map(float, input().split(',')))
    for number in x:
            if number >=0:
                answer.append(number)
                print("Input:List{}  is {}".format(i,x))
                print("Output of list{} is {}".format(i,(answer[i])))
               

