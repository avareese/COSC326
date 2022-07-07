'''''
Author Ava Reese
Dates
'''''
import re


#Function which checks against various rules of the date format for seperators, day, month and year
def validateDate (date):
        
    date = date.strip('\n')
    date1 = re.split(r"[-|/|\s]", date)
    separators = re.sub(r'[^-|\s|/]', '', date)
    
    if (len(separators) != 2):
        print(date, "- INVALID: Please use two seperators to split d-m-y")
        return
        
    if (len(date1) != 3):
        print(date, "- Invalid: please enter three values for d m y ")
        return
        
    if not (len(set(separators))== 1):
        print(date, "- Invalid: Please use the same seperator")
        return
         
    
    day = date1[0]
    month = date1[1]
    year = date1[2]
    
    #format year 
    
    if not (year.isdigit()):
        print(date, "- INVALID: Please enter a digit for the year")
        return
    
    if(len(year) != 2 and len(year) != 4): 
        print(date, "- Invalid: year length entered is not yy or yyyy")
        return
     
    if(len(year)== 2):
        year = yearFormat(year)   
      
           
    year = int(year)
    if ((year > 3000) | (year  < 1753)): 
        print(date, "- Invalid: year out of range")
        return
      
    
    
    #format month
    
    mon = [ 'jan', 'feb', 'mar', 'apr', 'may', 'jun',
               'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    days_mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if(month.isdigit()):
        if((int(month) < 0 or (int(month) > 12 ))): 
            print(date, "- Invalid: Please enter month as 0m or m or mm and between 1-12")
            return    
    else:
        monthCheck = monthAlpha(month)
        if(monthCheck[0]):
            print(date, monthCheck[1])
            return
    
    if(month.isdigit and month == '0'):
        print(date, "- Invalid: 0 is not a month")
        return 
    
    month = month.lower()       
    if(month.isdigit()):
        month_index = int(month)-1
        month = mon[month_index]  
    else:
        month_index = mon.index(month)
        
                  
            
    #format day
    
    if not(day.isdigit()):
        print(date, "- Invalid: Please enter a day as a digit")
        return
    
    if(len(day) > 2):
        print(date, "- Invalid: Please enter day as dd or 0d")
        return
    
    if(day.isdigit and day == '0'):
        print(date, "- Invalid: 0 is not a day")
        return 
    
    if len(day) == 1:
        day = "0" + day
        
    
    months = {'jan':31,'feb':28,'mar':31,'apr':30,'may':31,'jun':30,
              'jul':31,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}
    
    if(isLeapYear(year)):
        months['feb'] = 29
    if not ((int(day) <= months[month]) & (int(day) > 0)):
        print(date, "-Invalid: Please enter the correct days for the month")
        return
    
    print(day, month.capitalize(), year)

# function which checks if it is a leap year, if it is it returns true else return false    
def isLeapYear(year):
    
    if ((int(year) % 4 == 0) & (int(year) % 100 != 0) or (int(year) % 400 ==0)):
        return True
    else:
        return False
        
    
# function which formats the year so if the input is yy it prints as yyyy  
def yearFormat(year):
    
    year = int(year)
    if year <= 99 and year >= 50: 
        year += 1900
        return year
    else:
        year += 2000
        return year 
                
                
 #  function which checks against month rules if they are inputted as letters  
def monthAlpha (month):
    mon = [ 'jan', 'feb', 'mar', 'apr', 'may', 'jun',
               'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    
    if((not month.isupper()) and (not month.islower()) and (not month.istitle())):
        return [True, "- Invalid: Please use all captials or all lowercase " ]
    
    if not ((month.lower() in mon)): 
        return [True, "- Invalid: Please enter a valid month between Jan-Dec"]     
    
    return [False]
           
          
# main method which asks for user inputs and calls validateDate function
if __name__ == "__main__":
   
    while(True):
        try: 
            date = input("Enter a date:  ")
            validateDate(date)
        except EOFError as e:
            print("\n Ending program")
            quit()
        