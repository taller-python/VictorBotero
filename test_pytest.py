import pytest
import unittest
import compuertas


class mtTest(unittest.TestCase):
    #@pytest.fixture(scope="class")

    #@pytest.fixture(scope="class")

    def test_compuertas(self):

        entrya = '1'
        entryb = '1'
        outside = compuertas.compuertOR(entrya, entryb)
        print (outside)
        assert outside == '1'
        assert '1' == '1'
