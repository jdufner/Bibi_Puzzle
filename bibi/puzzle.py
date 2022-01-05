import card

class puzzle:
    
    def build_cards():
        c1 = card.Card(1, 
            card.Connector(2, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(4, card.UNTEN), 
            card.Connector(3, card.UNTEN))
        c2 = card.Card(2,
            card.Connector(4, card.OBEN), 
            card.Connector(3, card.OBEN), 
            card.Connector(4, card.UNTEN), 
            card.Connector(1, card.UNTEN))
        c3 = card.Card(3,
            card.Connector(3, card.OBEN), 
            card.Connector(4, card.OBEN), 
            card.Connector(4, card.UNTEN), 
            card.Connector(2, card.UNTEN))
        c4 = card.Card(4,
            card.Connector(1, card.OBEN), 
            card.Connector(3, card.OBEN), 
            card.Connector(2, card.UNTEN), 
            card.Connector(4, card.UNTEN))
        c5 = card.Card(5,
            card.Connector(2, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(2, card.UNTEN), 
            card.Connector(3, card.UNTEN))
        c6 = card.Card(6,
            card.Connector(3, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(2, card.UNTEN), 
            card.Connector(1, card.UNTEN))
        c7 = card.Card(7,
            card.Connector(4, card.OBEN), 
            card.Connector(1, card.OBEN), 
            card.Connector(2, card.UNTEN), 
            card.Connector(3, card.UNTEN))
        c8 = card.Card(8,
            card.Connector(2, card.OBEN), 
            card.Connector(3, card.OBEN), 
            card.Connector(4, card.UNTEN), 
            card.Connector(1, card.UNTEN))
        c9 = card.Card(9,
            card.Connector(3, card.OBEN), 
            card.Connector(4, card.OBEN), 
            card.Connector(2, card.UNTEN), 
            card.Connector(4, card.UNTEN))
