import datetime
fun = input(
"""
Enter a number to select a function:
1: seconds -> hours:minutes:seconds
2: hours:minutes:seconds -> seconds
"""
)
fun=2
if fun == 1:
    time = int(input("Enter time like 1000   :"))
    print(datetime.timedelta(seconds=time))

elif fun == 2:
    time = input("Enter time like 10:10:10   :")
    h,m,s = time.split(':')
    print(int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds()))