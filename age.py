import datetime
current_year=datetime.datetime.now().year

def Checker(year):
    while True:
        if not year.isdigit():
            print("Year should be numerical ")
            break 
        elif int(year)>current_year and int(year)<1940:
            print("Invalid year")
            break
        else:
            return year
       
    
def Monthy(month,day):
    
    if month not in['1','2','3','4','5','6','7','8','9','10','11','12']:
        print("Invalid month")
        return False
    elif month in['1','3','5','7','8','10','12']:
        days=31
        if not month.isdigit():
            print("Month should be numerical ")
        elif int(day)>days or int(day)<0:
            print("Invalid day")
            return False
        else:
            return day,month
       
    elif month in['4','6','9','11']:
        days=30
        if not month.isdigit():
            print("Month should be numerical ")
        elif int(day)>days or int(day)<0:
            print("Invalid day")
            return False
        else:
            return day,month
        

def calculator():
    year=input("Enter your birth year: ").strip()
    while True:
        if not year.isdigit():
            print("Year should be numerical ")
            year=input("Enter your birth year: ").strip()
             
        elif int(year)>current_year or int(year)<1940:
            print("Invalid year")
            year=input("Enter your birth year: ").strip()
        else:
            break 
    
    
    month=input("Enter the month you were born in(1-12): ").strip()
    while month not in['1','2','3','4','5','6','7','8','9','10','11','12'] or not month.isdigit():
        print("Invalid month")
        month=input("Enter the month you were born in(1-12): ").strip()
    date=input("Enter the date: ").strip()
    while not date.isdigit():
        print("Date should be numerical ")
        date=input("Enter the date: ").strip()
    if month in['1','3','5','7','8','10','12']:
        days=31
        while int(date)>days or int(date)<0:
            print("Invalid day")   
            date=input("Enter the date: ").strip()
    elif month in['4','6','9','11']:
        days=30
        while int(date)>days or int(date)<0:
            print("Invalid day")   
            date=input("Enter the date: ").strip()
    elif month=='2':
        diff=current_year-int(year)
        dive=diff/2
        mod=diff%2
        if dive%2!=0 or mod!=0:
            days=28
            while int(date)>days or int(date)<0:
                print("Invalid day")   
                date=input("Enter the date: ").strip()
        else:
            days=29
            while int(date)>days or int(date)<0:
                print("Invalid day")   
                date=input("Enter the date: ").strip()
            
    current_d=datetime.datetime.now().day
    current_m=datetime.datetime.now().month

    rem_years=current_year-int(year)
    rem_months=current_m-int(month)
    if rem_months<0:
        rem_months+=12
        rem_years-=1
    
    rem_days=current_d-int(date)
    if rem_days<0:
        if month in ['1','3','5','7','8','10','12']:
            rem_days+=31
            rem_months-=1
        elif month in['4','6','9','11']:
            rem_days+=30
            rem_months-=1

    print(f"{rem_years} years {rem_months} months {rem_days} days old")
    
calculator()







    



