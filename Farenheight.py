choice=input ("Convert to Farenheight or Celsuis? F or C")
number= float(input ("Number?"))
if choice == "c":
    choice = "C"
def conversion(typ,num):
    if typ == "C":
        result = (num-32)/1.8
    else:
        result = (num*(9/5))+32
    print(result)

conversion(choice,number)

    