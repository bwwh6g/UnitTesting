import datetime

while True:
    #Collect dates from user and split into three different fields
    try:
        begin_date = input('Enter a beginning date in YYYY-MM-DD format: ')
        begin_year, begin_month, begin_day = map(int, begin_date.split('-'))
        date1 = datetime.date(begin_year, begin_month, begin_day)
        

        end_date = input('Enter a end date in YYYY-MM-DD format: ')
        end_year, end_month, end_day = map(int, end_date.split('-'))
        date2 = datetime.date(end_year, end_month, end_day)

        #Compare the dates to make sure they are valid
        if (begin_year > end_year):
            print("Enter valid dates")
            continue
        elif (begin_year == end_year):
            if (begin_month > end_month):
                print("Enter valid dates")
                continue
            elif (end_month > begin_month):
                break
            elif (end_month == begin_month):
                if (begin_day >= end_day):
                    print("Enter valid dates")
                    continue
                else:
                    break
        else:
            break
        
    #Using Try/Except to easily restart if an error occurs 
    except:
        print("Enter valid dates!")
        continue

#Prints out the dates to make sure everything worked the way it's supposed to    
print("Start date: " + str(date1))
print("End date: " + str(date2))

userChoicelist = []

userInput1 = input("Enter the stock symbol you are looking for: ")
userChoicelist.append(userInput1)

print("\nChart Types\n---------------")

print("1.Bar \n2.Chart\n")

# Function two to get input on what chart they want.
userInput2 = int(input("Enter the type of chart you want (1, 2): "))

while (True):
    if (userInput2 == 1):
        userChoicelist.append(userInput2)
        break

    elif (userInput2 == 2):
        userChoicelist.append(userInput2)
        break

    else:
        print("\nThat is not a valid input your choices are 1.Bar or Line. Please try again.\n")
        userInput2 = int(input("Enter the type of chart you want:"))

print("\nSelect the Time Series of the chart you want to Generate")
print("---------------------------------------------------------")
print("1.Intraday\n2.Daily\n3.Weekly\n4.Monthly\n")

# Function Three to get input for the Time Series selection.
userInput3 = int(input("Enter the time series option (1, 2, 3, 4): "))

while (True):
    if (userInput3 > 0 & userInput3 < 5):
            userChoicelist.append(userInput3)
            break

    else:
        print("\nThat is not a valid input your choices are \n1.Intraday \n2.Daily \n3.Weekly \n4.Monthly\n")
        userInput3 = int(input("Enter the time series option you'd like:"))

