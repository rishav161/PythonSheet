class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        li=[]
        cnt=0
        for c in s:
            if c=='(':
                li.append(c)
                cnt+=1
            elif c==')' and cnt>0:
                li.append(c)
                cnt-=1
            elif c!=")":
                li.append(c)
        filt=[]
        for i in li[::-1]:
            if i=="(" and cnt>0:
                cnt-=1
            else:
                filt.append(i)
        return "".join(filt[::-1])
