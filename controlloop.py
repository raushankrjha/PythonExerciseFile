from _operator import index
def main():
    print("For Loop")
    
    value=[1,2,3,4,5,6]
    
    for index,charac in enumerate(value):
        print(index ,charac)
if __name__=="__main__":main()