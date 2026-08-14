class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        target={}
        window={}
        start=0
        bestLen=float('inf')
        formed=0
        for ch in t:
            target[ch]=target.get(ch,0)+1
        required=len(target)
        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1

            if s[r] in target and target[s[r]]==window[s[r]]:
                formed+=1
            while formed==required:
                if (r-l+1) < bestLen:
                    bestLen=r-l+1
                    start=l
                window[s[l]]-=1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    formed-=1
                l+=1
        if bestLen==float('inf'):
            return ""
        return s[start : start+bestLen]