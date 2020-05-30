import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cc = dict(collections.Counter(s))
        count = max_odd = 0
        for k,v in cc.items():
            if v % 2 == 0:
                count += v
            if v % 2 == 1 and v > max_odd:
                max_odd = v
        return max_odd + count


if __name__ == '__main__':
    s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefieml\
    doftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmig\
    htliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallow\
    thisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldads\
    wfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicated\
    heretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreatt\
    dafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasure\
    ofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffre\
    edomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    lp = Solution()
    lp.longestPalindrome(s)