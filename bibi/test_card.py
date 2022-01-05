import unittest

import card
from card import Card
from card import Connector

class TestConnector(unittest.TestCase):

    def test_equals(self):
        c1 = Connector(1, "oben")
        c2 = Connector(1, "oben")
        self.assertEqual(c1, c2)

    def test_suites1(self):
        c1 = Connector(1, "oben")
        c2 = Connector(1, "unten")
        self.assertTrue(c1.suites(c2))

    def test_suites2(self):
        c1 = Connector(1, "oben")
        c2 = Connector(1, "oben")
        self.assertFalse(c1.suites(c2))

class TestCard(unittest.TestCase):

    def test_check_rechts(self):
        c1 = Card(1, 
            Connector(2, card.OBEN), 
            Connector(1, card.OBEN), 
            Connector(4, card.UNTEN), 
            Connector(3, card.UNTEN))
        c2 = Card(2,
            Connector(4, card.OBEN), 
            Connector(3, card.OBEN), 
            Connector(4, card.UNTEN), 
            Connector(1, card.UNTEN))
        self.assertTrue(c1.check_rechts(c2))

    def test_check_links(self):
        c1 = Card(1, 
            Connector(2, card.OBEN), 
            Connector(1, card.OBEN), 
            Connector(4, card.UNTEN), 
            Connector(3, card.UNTEN))
        c2 = Card(2,
            Connector(4, card.OBEN), 
            Connector(3, card.OBEN), 
            Connector(4, card.UNTEN), 
            Connector(1, card.UNTEN))
        self.assertTrue(c1.check_links(c2))

    def test_check_oben(self):
        c1 = Card(1, 
            Connector(2, card.OBEN), 
            Connector(1, card.OBEN), 
            Connector(4, card.UNTEN), 
            Connector(3, card.UNTEN))
        c2 = Card(5,
            Connector(2, card.OBEN), 
            Connector(1, card.OBEN), 
            Connector(2, card.UNTEN), 
            Connector(3, card.UNTEN))
        self.assertTrue(c1.check_oben(c2))

    def test_check_unten(self):
        c1 = Card(1, 
            Connector(2, card.OBEN), 
            Connector(1, card.OBEN), 
            Connector(4, card.UNTEN), 
            Connector(3, card.UNTEN))
        c2 = Card(2,
            Connector(4, card.OBEN), 
            Connector(3, card.OBEN), 
            Connector(4, card.UNTEN), 
            Connector(1, card.UNTEN))
        self.assertTrue(c1.check_unten(c2))

if __name__ == "__main__":
    unittest.main()
