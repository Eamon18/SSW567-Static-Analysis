# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self):
    	self.assertEqual(classifyTriangle(20,25,30),'Scalene')

    def testIsocelesTriangles(self):
    	self.assertEqual(classifyTriangle(20,20,30),'Isoceles')

    def testInvalidInputA(self):
    	self.assertEqual(classifyTriangle(0,0,0),'InvalidInput')


    def testInvalidInputB(self):
    	self.assertEqual(classifyTriangle(200,300,300),'InvalidInput')

    def testInvalidInputC(self):
    	self.assertEqual(classifyTriangle(30,'b',20),'InvalidInput')

    def testNotTriangle(self):
    	self.assertNotEqual(classifyTriangle(10,10,40),'Isoceles','Should be NotATriangle')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

