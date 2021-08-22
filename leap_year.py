print("此為判斷閏年/平年的程式")
year = input("請輸入年份: ")
year = int(year)

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0 and year % 3200 != 0:
        return True
    else:
        return False
leap = is_leap(year)
if leap == True:
    print(year, '年是閏年')
else:
    print(year, '年是平年')