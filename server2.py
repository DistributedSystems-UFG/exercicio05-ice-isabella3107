import sys, Ice
import Demo

class Printer1I(Demo.Printer):
    def __init__(self, t):
        self.t = t

    def printString(self, s, current=None):
        print(self.t, s)

    def toUpper(self, s, current=None):
        return s.upper()

    def concat(self, a, b, current=None):
        return a + b


class Printer2I(Demo.Printer):
    def __init__(self, t):
        self.t = t

    def printString(self, s, current=None):
        print(self.t, s)

    def toUpper(self, s, current=None):
        return "[P2] " + s.upper()

    def concat(self, a, b, current=None):
        return "[P2] " + a + b


with Ice.initialize(sys.argv) as communicator:

    adapter = communicator.createObjectAdapterWithEndpoints(
        "SimpleAdapter", "default -p 11000"
    )

    object1 = Printer1I("Object1 says:")
    object2 = Printer2I("Object2 says:")

    adapter.add(object1, communicator.stringToIdentity("SimplePrinter1"))
    adapter.add(object2, communicator.stringToIdentity("SimplePrinter2"))

    adapter.activate()
    communicator.waitForShutdown()
