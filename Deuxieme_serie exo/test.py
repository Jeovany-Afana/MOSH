#tabulation = 6
#for i in range(1, 6):
   # print(tabulation * ' '+'* '*i+'\n')
    #tabulation -= 1
import time
tab = 10
for i in range(1, 10):
    print(tab*' ' + '* '*i)
    time.sleep(0.5)
    tab -= 1
    if i == 9:
        for new in range(1, 6):
            print(7*' ' + '* '*4)


