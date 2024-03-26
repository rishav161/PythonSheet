class Solution:
    def compress(self, chars):
        n=len(chars)
        ind=0
        i=0
        while i<n:
            curr_char=chars[i]
            c=0

            while(i<n and chars[i]==curr_char):
                c+=1
                i+=1
            chars[ind]=curr_char
            ind+=1
            if c>1:
                str_count=str(c)

                for ch in str_count:
                    chars[ind]=ch
                    ind+=1
        return ind