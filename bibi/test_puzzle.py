import unittest
from unittest.case import TestCase

import card
import puzzle

class TestPuzzle(unittest.TestCase):

    def test_build_cards(self):
        cards = puzzle.Puzzle.build_cards()
        self.assertEqual(9, len(cards))

    def test_find_solution(self):
        puzzle.Puzzle.find_solution(0, 0, [], puzzle.Puzzle.build_cards())
        self.assertTrue(False)

    def test_get_next_or_rotate_card_1(self):
        solution = []
        cards = puzzle.Puzzle.build_cards()
        puzzle.Puzzle.get_next_or_rotate_card(solution, cards)
        self.assertEqual(1, len(solution))
        self.assertEqual(card.ROTATION_KEINE, solution[0].rotation)
        self.assertEqual(8, len(cards))

    def test_get_next_or_rotate_card_2(self):
        solution = []
        cards = puzzle.Puzzle.build_cards()
        puzzle.Puzzle.get_next_or_rotate_card(solution, cards)
        puzzle.Puzzle.get_next_or_rotate_card(solution, cards)
        self.assertEqual(1, len(solution))
        self.assertEqual(card.ROTATION_VIERTEL, solution[0].rotation)
        self.assertEqual(8, len(cards))
    
    def build_default_card(nummer):
        return card.Card(nummer, 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.UNTEN), 
            card.Connector(1, card.UNTEN),
            card.ROTATION_KEINE)

    def test_is_valid_positive_2_cards(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(card.Card(2, 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.UNTEN), 
            card.Connector(1, card.UNTEN),
            card.ROTATION_KEINE))
        self.assertTrue(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_negative_2_cards(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(card.Card(2, 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.UNTEN), 
            card.Connector(2, card.UNTEN),
            card.ROTATION_KEINE))
        self.assertFalse(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_positive_3_cards(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        self.assertTrue(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_negative_3_cards(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(card.Card(3, 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.UNTEN), 
            card.Connector(2, card.UNTEN),
            card.ROTATION_KEINE))
        self.assertFalse(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_positive_4_cards(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        self.assertTrue(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_negative_4_cards(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(card.Card(4, 
            card.Connector(2, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.UNTEN), 
            card.Connector(1, card.UNTEN),
            card.ROTATION_KEINE))
        self.assertFalse(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_positive_5_cards(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        cards.append(TestPuzzle.build_default_card(5))
        self.assertTrue(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_negative_5_cards_1(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        cards.append(card.Card(5, 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.UNTEN), 
            card.Connector(2, card.UNTEN),
            card.ROTATION_KEINE))
        self.assertFalse(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_negative_5_cards_2(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        cards.append(card.Card(5, 
            card.Connector(2, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.UNTEN), 
            card.Connector(1, card.UNTEN),
            card.ROTATION_KEINE))
        self.assertFalse(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_positive_6_cards(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        cards.append(TestPuzzle.build_default_card(5))
        cards.append(TestPuzzle.build_default_card(6))
        self.assertTrue(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_negative_6_cards_1(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        cards.append(TestPuzzle.build_default_card(5))
        cards.append(card.Card(6, 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.UNTEN), 
            card.Connector(2, card.UNTEN),
            card.ROTATION_KEINE))
        self.assertFalse(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_negative_6_cards_2(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        cards.append(TestPuzzle.build_default_card(5))
        cards.append(card.Card(6, 
            card.Connector(2, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.UNTEN), 
            card.Connector(1, card.UNTEN),
            card.ROTATION_KEINE))
        self.assertFalse(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_positive_7_cards(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        cards.append(TestPuzzle.build_default_card(5))
        cards.append(TestPuzzle.build_default_card(6))
        cards.append(TestPuzzle.build_default_card(7))
        self.assertTrue(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_negative_7_cards(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        cards.append(TestPuzzle.build_default_card(5))
        cards.append(TestPuzzle.build_default_card(6))
        cards.append(card.Card(7, 
            card.Connector(2, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.UNTEN), 
            card.Connector(1, card.UNTEN),
            card.ROTATION_KEINE))
        self.assertFalse(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_positive_8_cards(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        cards.append(TestPuzzle.build_default_card(5))
        cards.append(TestPuzzle.build_default_card(6))
        cards.append(TestPuzzle.build_default_card(7))
        cards.append(TestPuzzle.build_default_card(8))
        self.assertTrue(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_negative_8_cards_1(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        cards.append(TestPuzzle.build_default_card(5))
        cards.append(TestPuzzle.build_default_card(6))
        cards.append(TestPuzzle.build_default_card(7))
        cards.append(card.Card(8, 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.UNTEN), 
            card.Connector(2, card.UNTEN),
            card.ROTATION_KEINE))
        self.assertFalse(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_negative_8_cards_2(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        cards.append(TestPuzzle.build_default_card(5))
        cards.append(TestPuzzle.build_default_card(6))
        cards.append(TestPuzzle.build_default_card(7))
        cards.append(card.Card(8, 
            card.Connector(2, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.UNTEN), 
            card.Connector(1, card.UNTEN),
            card.ROTATION_KEINE))
        self.assertFalse(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_positive_9_cards(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        cards.append(TestPuzzle.build_default_card(5))
        cards.append(TestPuzzle.build_default_card(6))
        cards.append(TestPuzzle.build_default_card(7))
        cards.append(TestPuzzle.build_default_card(8))
        cards.append(TestPuzzle.build_default_card(9))
        self.assertTrue(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_negative_9_cards_1(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        cards.append(TestPuzzle.build_default_card(5))
        cards.append(TestPuzzle.build_default_card(6))
        cards.append(TestPuzzle.build_default_card(7))
        cards.append(TestPuzzle.build_default_card(8))
        cards.append(card.Card(9, 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.UNTEN), 
            card.Connector(2, card.UNTEN),
            card.ROTATION_KEINE))
        self.assertFalse(puzzle.Puzzle.is_valid(cards))

    def test_is_valid_negative_9_cards_2(self):
        cards = []
        cards.append(TestPuzzle.build_default_card(1))
        cards.append(TestPuzzle.build_default_card(2))
        cards.append(TestPuzzle.build_default_card(3))
        cards.append(TestPuzzle.build_default_card(4))
        cards.append(TestPuzzle.build_default_card(5))
        cards.append(TestPuzzle.build_default_card(6))
        cards.append(TestPuzzle.build_default_card(7))
        cards.append(TestPuzzle.build_default_card(8))
        cards.append(card.Card(9, 
            card.Connector(2, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(1, card.UNTEN), 
            card.Connector(1, card.UNTEN),
            card.ROTATION_KEINE))
        self.assertFalse(puzzle.Puzzle.is_valid(cards))

if __name__ == "__main__":
    unittest.main()
