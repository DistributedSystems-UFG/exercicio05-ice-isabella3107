import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv) as communicator

base = communicator.stringToProxy("SimplePrinter:default -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

printer.printString("Hello World!")

res1 = printer.toUpper("test")
print("Upper:", res1)

res2 = printer.concat("Hello ", "World")
print("Concat:", res2)
