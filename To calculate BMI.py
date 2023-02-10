a=float(input("ENTER THE Weight IN KG : "))
b=float(input("ENTER THE HEIGHT IN meters : "))
c=a/(b*b)
if c<18.5:
    print("Underweight")
elif c<25:
    print("Normal")
else:
    print("Overweight")
