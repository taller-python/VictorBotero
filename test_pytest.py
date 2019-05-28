#import pytest
import unittest
from compuertas import compuertOR 
from compuertas import compuertAND

class compuertasTest(unittest.TestCase):
    def test_OR_1_1(self):

        #print (outside)
        #self.assert outside == '1'
        #Prueba validar si compuerta or a=1, b=1
        entrya = '1'
        entryb = '1'
        outside = compuertOR(entrya, entryb)
        self.assertEqual('1',outside.evaluate())
    def test_OR_1_0(self):
        entrya = '1'
        entryb = '0'
        outside = compuertOR(entrya, entryb)
        self.assertEqual('1',outside.evaluate())
    def test_OR_0_1(self):
        entrya = '0'
        entryb = '1'
        outside = compuertOR(entrya, entryb)
        self.assertEqual('1',outside.evaluate())
    def test_OR_0_0(self):
    
        #print (outside)
        #self.assert outside == '1'
        #Prueba validar si compuerta or a=1, b=1
        entrya = '0'
        entryb = '0'
        outside = compuertOR(entrya, entryb)
        self.assertEqual('0',outside.evaluate())
    def test_AND_1_1(self):
    
        entrya = '1'
        entryb = '1'
        outside = compuertAND(entrya, entryb)
        #print (outside)
        #self.assert outside == '1'
        self.assertEqual('1',outside.evaluate())
        #assert outside == '1'
    def test_AND_1_0(self):       
        entrya = '1'
        entryb = '0'
        outside = compuertAND(entrya, entryb)
        #print (outside)
        #self.assert outside == '1'
        self.assertEqual('0',outside.evaluate())
    def test_AND_0_1(self): 
        entrya = '1'
        entryb = '0'
        outside = compuertAND(entrya, entryb)
        #print (outside)
        #self.assert outside == '1'
        self.assertEqual('0',outside.evaluate())
    def test_AND_0_0(self): 
        entrya = '0'
        entryb = '0'
        outside = compuertAND(entrya, entryb)
        #print (outside)
        #self.assert outside == '1'
        self.assertEqual('0',outside.evaluate())
