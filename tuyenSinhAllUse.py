import unittest
from tuyenSinh import tuyenSinh


class TestTuyenSinhC2(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(tuyenSinh(-5, 10, 1400), "Error")
    
    def test_case_2(self):
        self.assertEqual(tuyenSinh(29, 10, 1550), "Accepted")
    
    def test_case_3(self):
        self.assertEqual(tuyenSinh(20, 5, 1000), "Rejected")
    
    def test_case_4(self):
        self.assertEqual(tuyenSinh(25, 8, 1400), "Waitlisted")
    
    def test_case_5(self):
        self.assertEqual(tuyenSinh(5, 10, 1800), "Error")
    
    def test_case_6(self):
        self.assertEqual(tuyenSinh(5, 15, 1400), "Error")

if __name__ == '__main__':
    unittest.main()

