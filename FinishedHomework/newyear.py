from datetime import datetime

while True: 
    year = datetime.now().year # год текущий
    try:
        day = int(input("day>>")) 
        month = int(input("month>>"))
        start_date = datetime(year,month,day)
        end_date = datetime(year,12,31)
    except ValueError as err:
        print(err)
    else:
        break
 
print((end_date - start_date).days)
