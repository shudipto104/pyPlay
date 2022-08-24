# A leap year is a calender year containing an additional day added to keep the calender year synchornized with the astronomical or seasonal year. In the gregorian Feb to 29 days rather than common 28. These extra days occure in years which are multiplies of four (with the exception of centenial years not divisible by 400). What ais the programe ask for a year and calculates, if this year is a leap year or  not.

year = int(input("Enter the year:"))
if year % 4 == 0:
  if year % 400 == 0:
    print(" It's not leap year.")
  else:
    print("It's leap year.")
else: 
    print("It's not leap year")