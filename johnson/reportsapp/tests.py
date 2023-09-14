from django.test import TestCase

# Create your tests here.


class FirstTestCase(TestCase):
    def setUp(self):
        print('setup called')
    
    def test_equal(self):
        self.assertEqual(1,1)
