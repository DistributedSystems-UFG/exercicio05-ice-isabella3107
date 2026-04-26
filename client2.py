import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 98.90.53.6 -p 11000")
base2 = communicator.stringToProxy("SimplePrinter2:tcp -h 98.90.53.6 -p 11000")
printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)
if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy")

printer1.printString("Hello from printer1")
printer2.printString("Hello from printer2")

print(printer1.toUpper("teste"))
print(printer2.toUpper("teste"))

print(printer1.concat("A", "B"))
print(printer2.concat("A", "B"))

communicator.waitForShutdown()
