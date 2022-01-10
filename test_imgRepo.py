import unittest
import imgRepo



class TestimgRepo(unittest.TestCase):

    def test_addImg(self):
        self.assertEqual(imgRepo.addImg(), 3)  #change the second parameter to the desired number of images you plan to 'upload'

#change the directory to the folder that holds imgRepo.img and test_imgRepo.py
#python -m unittest test_imgRepo.py