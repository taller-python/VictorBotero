#import pytest
import unittest
from compuertas import compuertOR 
from compuertas import compuertAND


class compuertasTest(unittest.TestCase):
    #@pytest.fixture(scope="class")

    #@pytest.fixture(scope="class")

    def test_compuertasOR(self):

        #print (outside)
        #self.assert outside == '1'
        #Prueba validar si compuerta or a=1, b=1
        entrya = '1'
        entryb = '1'
        outside = compuertOR(entrya, entryb)
        self.assertEqual('1',outside.evaluate())
        #Prueba validar si compuerta or a=1, b=0
        entrya = '1'
        entryb = '0'
        outside = compuertOR(entrya, entryb)
        self.assertEqual('1',outside.evaluate())
        #Prueba validar si compuerta or a=0, b=1
        entrya = '0'
        entryb = '1'
        outside = compuertOR(entrya, entryb)
        self.assertEqual('1',outside.evaluate())

    def test_compuertasAND(self):
    
        entrya = '1'
        entryb = '1'
        outside = compuertAND(entrya, entryb)
        #print (outside)
        #self.assert outside == '1'
        self.assertEqual('1',outside.evaluate())
        #assert outside == '1'
