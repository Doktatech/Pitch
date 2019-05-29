import unittest
from models import Pitch
Pitch =pitch.Pitch

class PitchTest (unittest.TestCase):
    '''
    A testcase class for testing our pitch object
    '''
    def setUp(self):
        '''
        A Setup metthod that will run before every test
        '''
        self.new_pitch =Pitch(1234,'Pitch Perfect','A pitch in time saves one minute',0,0)
        
    def test_instance (self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))
        
if __name__=='__main__':
    unittest.main()