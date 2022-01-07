import card
from card import Card

class Puzzle:

    def find_solution(stack, counter, solution, cards):
        if Puzzle.is_valid(solution):
            if len(solution) >= 9:
                print("Solution: " + solution)
            else:
                solution_copy = Puzzle.copy_cards(solution)
                cards_copy = Puzzle.copy_cards(cards)
                solution_copy.append(cards_copy.pop(0))
                Puzzle.find_solution(stack + 1, 0, solution_copy, cards_copy)
        else:
            if (counter <= len(cards) * 4):
                Puzzle.get_next_or_rotate_card_new(solution, cards)
                Puzzle.find_solution(stack, counter + 1, solution, cards)

    def copy_cards(cards) -> list:
        copy = []
        for card in cards:
            copy.append(card.copy())
        return copy

    def get_next_or_rotate_card(solution, cards):
        if (len(solution) == 0 or solution[len(solution)-1].rotation == card.ROTATION_VOLL):
            solution.append(cards.pop(0))
        else:
            solution[len(solution)-1].rotate_clockwise()

    def get_next_or_rotate_card_new(solution, cards) -> Card:
        if (len(solution) == 0 or solution[len(solution)-1].rotation == card.ROTATION_VOLL):
            c = solution.pop(len(solution)-1)
            c.rotation = card.ROTATION_KEINE
            cards.append(c)
            return solution.append(cards.pop(0))
        else:
            return solution[len(solution)-1].rotate_clockwise()

    def is_valid(cards) -> bool:
        if (len(cards) >= 2):
            if not cards[0].check_rechts(cards[1]):
                return False
        if (len(cards) >= 3):
            if not cards[1].check_rechts(cards[2]):
                return False
        if (len(cards) >= 4):
            if not cards[0].check_unten(cards[3]):
                return False
        if (len(cards) >= 5):
            if not cards[1].check_unten(cards[4]):
                return False
            if not cards[3].check_rechts(cards[4]):
                return False
        if (len(cards) >= 6):
            if not cards[2].check_unten(cards[5]):
                return False
            if not cards[4].check_rechts(cards[5]):
                return False
        if (len(cards) >= 7):
            if not cards[3].check_unten(cards[6]):
                return False
        if (len(cards) >= 8):
            if not cards[4].check_unten(cards[7]):
                return False
            if not cards[6].check_rechts(cards[7]):
                return False
        if (len(cards) >= 9):
            if not cards[5].check_unten(cards[8]):
                return False
            if not cards[7].check_rechts(cards[8]):
                return False
        return True

    def build_cards() -> list:
        cards = []
        cards.append(card.Card(1, 
            card.Connector(2, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(4, card.UNTEN), 
            card.Connector(3, card.UNTEN),
            card.ROTATION_KEINE))
        cards.append(card.Card(2,
            card.Connector(4, card.OBEN), 
            card.Connector(3, card.OBEN), 
            card.Connector(4, card.UNTEN), 
            card.Connector(1, card.UNTEN),
            card.ROTATION_KEINE))
        cards.append(card.Card(3,
            card.Connector(3, card.OBEN), 
            card.Connector(4, card.OBEN), 
            card.Connector(4, card.UNTEN), 
            card.Connector(2, card.UNTEN),
            card.ROTATION_KEINE))
        cards.append(card.Card(4,
            card.Connector(1, card.OBEN), 
            card.Connector(3, card.OBEN), 
            card.Connector(2, card.UNTEN), 
            card.Connector(4, card.UNTEN),
            card.ROTATION_KEINE))
        cards.append(card.Card(5,
            card.Connector(2, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(2, card.UNTEN), 
            card.Connector(3, card.UNTEN),
            card.ROTATION_KEINE))
        cards.append(card.Card(6,
            card.Connector(3, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(2, card.UNTEN), 
            card.Connector(1, card.UNTEN),
            card.ROTATION_KEINE))
        cards.append(card.Card(7,
            card.Connector(4, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(2, card.UNTEN), 
            card.Connector(3, card.UNTEN),
            card.ROTATION_KEINE))
        cards.append(card.Card(8,
            card.Connector(2, card.OBEN), 
            card.Connector(3, card.OBEN), 
            card.Connector(4, card.UNTEN), 
            card.Connector(1, card.UNTEN),
            card.ROTATION_KEINE))
        cards.append(card.Card(9,
            card.Connector(3, card.OBEN), 
            card.Connector(4, card.OBEN), 
            card.Connector(2, card.UNTEN), 
            card.Connector(4, card.UNTEN),
            card.ROTATION_KEINE))
        return cards
