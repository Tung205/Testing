import unittest
from tuyenSinh import tuyenSinh


class TestTuyenSinhC2(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(tuyenSinh(100, 5, 800), "Error")
    
    def test_case_2(self):
        self.assertEqual(tuyenSinh(15, 15, 800), "Error")
    
    def test_case_3(self):
        self.assertEqual(tuyenSinh(15, 5, 2000), "Error")
    
    def test_case_4(self):
        self.assertEqual(tuyenSinh(15, 5, 800), "Rejected")
    
    def test_case_5(self):
        self.assertEqual(tuyenSinh(25, 8.5, 1400), "Waitlisted")
    
    def test_case_6(self):
        self.assertEqual(tuyenSinh(28, 9.5, 1500), "Accepted")

if __name__ == '__main__':
    unittest.main()

