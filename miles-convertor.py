def calcMiles (kilometers1, kilometers2, kilometers3, kilometers4, kilometers5):

mile1 = kilometers1 *   0.6214
mile2 = kilometers2 * 0.6214
mile3 = kilometers3 * 0.6214
mile4 = kilometers4 * 0.6214
mile5 = kilometers5 * 0.6214

return mile1, mile2, mile3, mile4, mile5,\

def askfordistance():
kilometers1 = float(input("Please enter distance in kilometers: "))
kilometers2 = float(input("Please eneter distance in Kilometers:"))
kilometers3 = float(input("Please enter distance in Kilometers:"))
kilometers4 = float(input("Please enter distance in Kilometers:"))
kilometers5 = float(input("Please enter distance in Kilometers:"))

return kilometer1, kilometer2, kilometer3, kilometer4, kilometer5

def printconvertedresults(kilometer1, kilometer2, kilometer3, kilometer4, kilometer5)

print("kilometers\tMiles")
print( str( Kilometer1)+ "\t"+calcMiles( kilometers1),
     (str(Kilometer2) + "\t" + calcMiles(kilometers2),
     (str(Kilometer3 + "\t" + calcMiles(kilometers3),
     (str(Kilometer4 + "\t" + calcMiles(kilometers4),
     (str(Kilometer5 + "\t" + calcMiles(kilometers5),


def main():
  kilometer1, kilometer2, kilometer3, kilometer4, kilometer5,\ = askForDistance()
  print("")
  printconvertedresults(kilometer1, kilometer2, kilometer3, kilometer4, kilometer5,\
  print( askfordistance, "kilometers converted to miles is", printconvertedresults(kilomters1, kilometers2, kilometers3, kilometers4, kilometers5)\
  
  main()
