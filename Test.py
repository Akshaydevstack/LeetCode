
srt = "malayalm"
def palindrome(s):
    cleaned_text = "".join(char.lower() for char in s if char.isalpha())

    left = 0
    right = len(s)-1

    while left< right:
        if cleaned_text[left] != cleaned_text[right]:
            return False
        
        return True

print(palindrome(srt))