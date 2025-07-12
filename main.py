from TermuxWebServer import *
printBanner("Termux  WebServer")
tempBool = True
while (tempBool):
    printFeatures()
    print("\n")
    featureCode = int(input("Select an Option : "))
    tempBool = redirectToFeature(featureCode=featureCode)