# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(num):
        # Your code goes here
#     (153,True),(1000,False),(370,True),(371,True),(420,False),(407,True)
        temp = num
        power = len(num)
        res = 0
        while(temp > 0):
                temp1  = temp % 10
                res += temp1**power 
                temp = temp//10
        if(num == res):
                return True
        else:
                return False
