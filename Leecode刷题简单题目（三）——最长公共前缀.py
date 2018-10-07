class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        "选择输入字符串数组当中，长度最短的字符串作为标志"
        a=''        
        length=len(strs)
        if length==0:
            return ''
        minimum=strs[0]
        length_minimum=len(strs[0])
        account=-1  
        flag=0
        "注意，如果这里所有的元素长度是顺次的，如果不先定义flag"
        for x in strs:
            if x=="":
                return ""
            account=account+1
            if len(x)>=length_minimum:
                continue
                "不要忘记，continue会直接跳出循环，不会做循环最后的迭代加操作"
            else:
                minimum=x
                flag=account

                
        
        j=0
        for i in minimum:
            k=0
            length2=length
            while (k<length2):
                if k==flag:               
                    "多个循环结构，最内层的循环是， k→数组内元素的循环"
                    k=k+1
                    continue                 
                    "外层循环式作为 作为标志的最短字符串内字符的循环"
                temp=strs[k]
                if i!=temp[j]:
                    if j==0:
                        return '' 
                    else:
                        return a
                elif i==temp[j]:
                    k=k+1
                    continue
            a=a+i
            j=j+1

        return a
                