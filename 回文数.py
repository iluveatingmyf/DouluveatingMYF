class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=x
        if x<0:
            return False
        elif x==0:
            return True
        elif x%10==0:
            return False
        elif x/10==0:
            return True

        else:
            flag=1
            sum1=1
            while(x>0):
                temp1=x%10
                if(flag==1):
                    ten=0
                else:
                    ten=10
                sum1=sum1*ten+temp1
                flag=0
                x=x/10
               
            if sum1 == y:
                return True
            else:
                return False
                
                