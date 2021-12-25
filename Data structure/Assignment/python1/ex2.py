print(" *** Wind classification ***")
inputall = float(input("Enter wind speed (km/h) : "))

if(inputall >= 0.0 and inputall <=51.99):
    print("Wind classification is Breeze.")
elif(inputall >= 52.00 and inputall <=55.99):
    print("Wind classification is Depression.")
elif(inputall >= 56.00 and inputall <=101.99):
    print("Wind classification is Tropical Storm.")
elif(inputall >= 102.00 and inputall <=208.99):
    print("Wind classification is Typhoon.")
elif( inputall >= 209):
    print("Wind classification is Super Typhoon.")

