import unittest
from tuyenSinh import tuyenSinh


class TestTuyenSinh(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(tuyenSinh(-0.1, 5, 800), "Error")
    
    def test_case_2(self):
        self.assertEqual(tuyenSinh(0, 5, 800), "Rejected")
    
    def test_case_3(self):
        self.assertEqual(tuyenSinh(0.1, 5, 800), "Rejected")
    
    def test_case_4(self):
        self.assertEqual(tuyenSinh(29.9, 5, 800), "Rejected")
    
    def test_case_5(self):
        self.assertEqual(tuyenSinh(30, 5, 800), "Rejected")
    
    def test_case_6(self):
        self.assertEqual(tuyenSinh(30.1, 5, 800), "Error")
    
    def test_case_7(self):
        self.assertEqual(tuyenSinh(15, -0.1, 800), "Error")
    
    def test_case_8(self):
        self.assertEqual(tuyenSinh(15, 0, 800), "Rejected")
    
    def test_case_9(self):
        self.assertEqual(tuyenSinh(15, 0.1, 800), "Rejected")
    
    def test_case_10(self):
        self.assertEqual(tuyenSinh(15, 9.9, 800), "Rejected")
    
    def test_case_11(self):
        self.assertEqual(tuyenSinh(15, 10, 800), "Rejected")
    
    def test_case_12(self):
        self.assertEqual(tuyenSinh(15, 10.1, 800), "Error")
    
    def test_case_13(self):
        self.assertEqual(tuyenSinh(15, 5, -1), "Error")
    
    def test_case_14(self):
        self.assertEqual(tuyenSinh(15, 5, 0), "Rejected")
    
    def test_case_15(self):
        self.assertEqual(tuyenSinh(15, 5, 1), "Rejected")
    
    def test_case_16(self):
        self.assertEqual(tuyenSinh(15, 5, 1599), "Rejected")
    
    def test_case_17(self):
        self.assertEqual(tuyenSinh(15, 5, 1600), "Rejected")
    
    def test_case_18(self):
        self.assertEqual(tuyenSinh(15, 5, 1601), "Error")
    
    def test_case_19(self):
        self.assertEqual(tuyenSinh(15, 5, 800), "Rejected")


if __name__ == '__main__':
    unittest.main()