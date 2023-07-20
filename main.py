def checkPalindrome(string,start=0,end=-1):
    if end==-1:
        end=len(string)-1
    if start>=end:
        return "Palindrome"
    if string[start]!=string[end]:
        return "Not Palindrome"
    return checkPalindrome(string,start+1,end-1)

print(checkPalindrome(input()))