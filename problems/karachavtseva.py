def getNumbers():
    invalid = True
    while invalid:
        len = input("Enter length: ")
        wid = input("Enter width: ")
        invalid = False
        try:
            len = float(len)
            wid = float(wid)
        except ValueError:
            print("Error: that's not valid")
    return (len, wid)

def areaCalc(a, b):
    return a * b

len = input("What is the length? ")
width = input("What is the width? ")
area = areaCalc(int(len), int(width))
print(area)