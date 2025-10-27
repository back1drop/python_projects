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
    checky=Checker(year)
    month=input("Enter the month you were born in(1-12): ").strip()
    date=input("Enter the date: ").strip()
    
    check=Monthy(month,date)
    nmonth=check[1]
    ndate=check[0]
    current_d=datetime.datetime.now().day
    current_m=datetime.datetime.now().month

    rem_years=current_year-int(checky)
    rem_months=current_m-int(nmonth)
    if rem_months<0:
        rem_months+=12
        rem_years-=1
    
    rem_days=current_d-int(ndate)
    if rem_days<0:
        if nmonth in ['1','3','5','7','8','10','12']:
            rem_days+=31
            rem_months-=1
        elif nmonth in['4','6','9','11']:
            rem_days+=30
            rem_months-=1

    print(f"{rem_years} {rem_months} {rem_days} old")
    
calculator()







    



