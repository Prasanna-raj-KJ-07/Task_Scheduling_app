import unittest
def facto(n):
    if n==1 or n==0:
        return 1
    else:
        return n*facto(n-1)
class test(unittest.TestCase):
    def test1(self):
        a=facto(5)
        self.assertTrue(a==120)
unittest.main()