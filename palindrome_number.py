class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string_x = str(x)
        reverted_x = string_x[::-1]

        if string_x == reverted_x:
            return True
        else:
            return False
        

if __name__ == "__main__":
    x = -121
    result = Solution().isPalindrome(x)
    print(result)
