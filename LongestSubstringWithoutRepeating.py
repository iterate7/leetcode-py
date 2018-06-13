class Solution(object):
    def lengthOfLongestSubstringMy(self, s):
        #定义map，结果，起始
        dic, res, start,substr = {}, 0, 0,""
        for i,ch in enumerate(s):
            print(i,ch)
            if ch in dic:
                res = max(res,i-start)
                start = max(dic[ch]+1,start)
            dic[ch] = i
            substr = s[start:start + res]
        maxt =  max(res,len(s)-start)
       # print("substr:",s[start:start+maxt])
        return maxt




    def lengthOfLongestSubstring(self, s):
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            # when char already in dictionary
            if ch in dic:
                # check length from start of string to index
                res = max(res, i - start)
                # update start of string index to the next index
                start = max(start, dic[ch] + 1)
            # add/update char to/of dictionary
            dic[ch] = i
        # answer is either in the begining/middle OR some mid to the end of string
        return max(res, len(s) - start)

#私有化部分
if __name__ == "__main__":
    s = "abcabcbb"
    s = "bbb"
    s = "pwwkew"
    instance = Solution()
    len1 = instance.lengthOfLongestSubstringMy(s)
    print(len1)
    len2 = instance.lengthOfLongestSubstring(s)
    print(len2)