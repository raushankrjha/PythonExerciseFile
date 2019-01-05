def main():
    print("loop")
    #fibonacci series
    first=0
    second=1
    print(first)
    while second<200:
        print(second ,end=' ')
        first,second=second,first+ second 
    
if __name__=="__main__":main()