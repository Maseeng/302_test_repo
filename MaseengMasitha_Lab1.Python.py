Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Maseeng Masitha
#24 January 2020
#Python 3.4
#IDCE 302 Lab 1: Calculating agricultural land and rain runoff in Kenya

#Volume of water run-off on area = 50 ft by 20 ft = 100 sq ft
#Volume of water run-off on 1000 sq ft during a rainfall event of 1 inch precipitation

plot_length = 600
plot_width = 240
area = plot_length * plot_width #Area of plot of land in Kenya in sq inches

print (plot_length)
print (plot_width)
print (area)

rainfall_inches = 1
print (rainfall_inches)

cubic_inches = plot_length * plot_width * rainfall_inches #volume of run-off in cubic inches
print (cubic_inches)

#Ratio of cubic inches to gallons is 231 cubic inches to 1 gallon
divisor = 231
runoff_gallons = cubic_inches / divisor
print (runoff_gallons)

Area2 = 144000 #Area of 1000 sq ft converted to sq inches
runoff_gallons2 = Area2 * rainfall_inches

print (runoff_gallons2) #volume of run-off for 1000 sq feet or 144000 sq inches in gallons

# Summary:
print "Plot length is :", plot_length
print "Plot width is :", plot_width
print "Rainfall in inches is :", rainfall_inches
print "Run-off in gallons for 100 sq ft or 14400 sq inches is :", runoff_gallons
print "Run-off in gallons for 1000 sq ft or 144000 sq inches is :", runoff_gallons2
