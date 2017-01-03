import datetime
import unittest


class DatePattern:

    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    def matches(self, date):
        return self.date == date


class FooTests(unittest.TestCase):

    def testFoo(self):
        self.failUnless(False)

    def testMatches(self):
        p = DatePattern(2004, 9, 28)
        d = datetime.date(2004, 9, 28)
        self.failUnless(p.matches(d))

def main():
    unittest.main()

if __name__ == '__main__':
    main()