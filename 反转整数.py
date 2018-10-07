class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y=x
        if (x>0):
            x=x
        if (x<0):
            x=-x
        if (x==0):
            return 0
        i=1
        sum=1
        while (x>0):
            j=i
            temp1=x%10
            if j>1:
                ten=10
            if (j==1):
                ten=0
            temp2=ten*sum 
            sum=temp1+temp2
            i=i+1
            x=x/10  
        if sum > 2147483650:
            return 0
        elif y>0:
            return sum
        elif y<0:
            return -sum
        else:
            return 0
   