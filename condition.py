
#this is an  file
def main():  
    ScroeKevin =100
    #condition example
    defaultHighScore =100
#     if ScroeKevin > defaultHighScore:
#         print("kevin you did that congrats")
#     elif ScroeKevin  < defaultHighScore:
#         print("Try Harder kevin")
#     else: 
#          print("score equals to the defaulscore")
#     
    
    msg ="You did it" if ScroeKevin > defaultHighScore else "You didn't made it"
    print(msg)
    
    
if __name__=="__main__": main()