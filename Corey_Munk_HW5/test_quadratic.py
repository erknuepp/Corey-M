#%%
from quadratic import quadratic_formula
import unittest

class TestQuadratic(unittest.TestCase):
    
    #Test normal case
    def test_normal_case(self):
        ret = quadratic_formula(5,-10,5).roots()
        self.assertAlmostEqual(ret,(10.0, 10.0))

    #Test identical roots
    def test_identical_roots(self):
        ret = quadratic_formula(1,-1,0).roots()
        self.assertAlmostEqual(ret,(1.0, 1.0))

    #Test no real roots
    def test_no_real_roots(self):
        try:
            ret = quadratic_formula(3,4,5).roots()
        except:
            ret = Exception
        self.assertEqual(ret,Exception)
        
if __name__ == '__main__':
    unittest.main()