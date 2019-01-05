import re
from test.test_decimal import file
def main():
    print("Hello")
    
    file=open("google.txt")
    
    for i in file:
        patternMatch =re.search("google",i)
        if patternMatch:
            print(patternMatch.group())
            
if __name__=="__main__": main()