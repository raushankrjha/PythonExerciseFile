def main():
    
    
    print("Switch Case")
    days =dict(
               one="monday",
               two="tuesday",
               three="Wednesday"
               )
    day="four"
    print(days.get(day, 'No Match '))
    
if __name__=="__main__":main()