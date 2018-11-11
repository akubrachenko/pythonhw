import unittest
import test1

class testForTests(unittest.TestCase):
    """Test1(hw1) tests"""

    @classmethod
    def setUpClass(cls):
        """Start Tests"""
        print("Start tests")
        print("========================================")

    @classmethod
    def tearDownClass(cls):
        """Finish Tests"""
        print("========================================")
        print("Finish tests")

    def setUp(self):
        print("Start test: " + self.shortDescription() + "")

    def tearDown(self):
        print("Finish test: " + self.shortDescription() + "")
        print("")


    def test_q1(self):
        """q1 test"""
        print("id: " + self.id())
        self.assertEqual(test1.q1("world"), "Hello,world!")
    def test_sum(self):
        """Sum test"""
        print("id: " + self.id())
        self.assertEqual(test1.sum([1,2,3,4]), 10)
    def test_multiply(self):
        """Multiply test"""
        print("id: " + self.id())
        self.assertEqual(test1.multiply([1,2,3,4]), 24)
    def test_reverse(self):
        """Reverse test"""
        print("id: " + self.id())
        self.assertEqual(test1.reverse("grut"), "turg")
    def test_isPalindrome(self):
        """isPalindrome test"""
        print("id: " + self.id())
        self.assertTrue(test1.reverse("lol"), "lol")
    def test_histogram(self):
        """Histogram test"""
        print("id: " + self.id())
        self.assertEqual(test1.histogram([1,2,3]), ['*','**','***'])
    def test_CaesarCipher(self):
        """CaesarCipher test"""
        print("id: " + self.id())
        self.assertEqual(test1.CaesarCipher("abc",1), "bcd")
    def test_diagonalReverse(self):
        """diagonalReverse test"""
        print("id: " + self.id())
        self.assertEqual(test1.diagonalReverse([[1,2,3],[4,5,6],[7,8,9]]), [[1,4,7],[2,5,8],[3,6,9]])
    def test_game(self):
        """Game test"""
        print("id: " + self.id())
        self.assertTrue(test1.game(1,2), 1)
    def test_balance(self):
        """Balance test"""
        print("id: " + self.id())
        self.assertTrue(test1.balance("[][]"))
    def test_charFreq(self):
        """charFreq test"""
        print("id: " + self.id())
        self.assertEqual(test1.charFreq("aabbcc"), {"a":'2',"b":'2',"c":'2'})
    def test_decToBin(self):
        """DecToBin"""
        print("id: " + self.id())
        self.assertEqual(test1.decToBin(5), '101')           
                 
if __name__ == '__main__':
    unittest.main()           
            

    