import unittest
import test1

class testForTests(unittest.TestCase):

    def test_q1(self):
        self.assertEqual(test1.q1("world"), "Hello,world!")
    def test_sum(self):
        self.assertEqual(test1.sum([1,2,3,4]), 10)
    def test_multiply(self):
        self.assertEqual(test1.multiply([1,2,3,4]), 24)
    def test_reverse(self):
        self.assertEqual(test1.reverse("grut"), "turg")
    def test_isPalindrome(self):
        self.assertTrue(test1.reverse("lol"), "lol")
    def test_histogram(self):
        self.assertEqual(test1.histogram([1,2,3]), ['*','**','***'])
    def test_CaesarCipher(self):
        self.assertEqual(test1.CaesarCipher("abc",1), "bcd")
    def test_diagonalReverse(self):
        self.assertEqual(test1.diagonalReverse([[1,2,3],[4,5,6],[7,8,9]]), [[1,4,7],[2,5,8],[3,6,9]])
    def test_game(self):
        self.assertTrue(test1.game(1,2), 1)
    def test_balance(self):
        self.assertTrue(test1.balance("[][]"))
    def test_charFreq(self):
        self.assertEqual(test1.charFreq("aabbcc"), {"a":'2',"b":'2',"c":'2'})
    def test_decToBin(self):
        self.assertEqual(test1.decToBin(5), '101')           
                 
if __name__ == '__main__':
    unittest.main()           
            

    