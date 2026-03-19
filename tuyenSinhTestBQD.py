import unittest
from tuyenSinh import tuyenSinh


class TestTuyenSinhBQD(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(tuyenSinh(-1, 8.5, 1500), "Error")
    
    def test_case_2(self):
        self.assertEqual(tuyenSinh(20, 8.5, 1500), "Rejected")
    
    def test_case_3(self):
        self.assertEqual(tuyenSinh(24, 7, 1500), "Rejected")
    
    def test_case_4(self):
        self.assertEqual(tuyenSinh(24, 8.5, 1000), "Rejected")
    
    def test_case_5(self):
        self.assertEqual(tuyenSinh(23, 8.5, 1500), "Waitlisted")
    
    def test_case_6(self):
        self.assertEqual(tuyenSinh(27, 8.3, 1500), "Waitlisted")
    
    def test_case_7(self):
        self.assertEqual(tuyenSinh(27, 9.5, 1400), "Waitlisted")
    
    def test_case_8(self):
        self.assertEqual(tuyenSinh(27, 9.5, 1500), "Accepted")


if __name__ == '__main__':
    unittest.main()
