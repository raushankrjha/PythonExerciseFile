def main():
    
    
    print("Complex")
    
    tup=(3,4,5,6)
    #fixed #immutable
    print(tup)
    
    list=[3,4,5,6]
    list.append(7)
    list.insert(1, 9)
    print(list)
   
   
    dict1={'one':1,2:'two'}
    
    dict2=dict([('one',1),('two',2)])
    print(dict2)
    
    dict3=dict(one=1 ,two=2)
    print(dict3)
    
if __name__=="__main__":main()