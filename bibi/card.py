OBEN = "O"
UNTEN = "U"
ROTATION_KEINE = 0
ROTATION_VIERTEL = 90
ROTATION_HALB = 180
ROTATION_DREIVIERTEL = 270
ROTATION_VOLL = 360

class Connector:
    nummer = 0;

    def __init__(self, nummer, ausrichtung):
        self.nummer = nummer
        if (ausrichtung == OBEN or ausrichtung == UNTEN):
            self.ausrichtung = ausrichtung

    def __str__(self) -> str:
        return (str(self.nummer) + self.ausrichtung)

    def __repr__(self) -> str:
        return (str(self.nummer) + self.ausrichtung)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Connector):
            return self.nummer == other.nummer and self.ausrichtung == other.ausrichtung
        return False

    def copy(self):
        return Connector(self.nummer, self.ausrichtung)

    def suites(self, other):
        return self.nummer == other.nummer and self.ausrichtung != other.ausrichtung

class Card:
    nummer = 0;

    def __init__(self, nummer, oben, rechts, unten, links, rotation):
        self.nummer = nummer
        self.oben = oben
        self.rechts = rechts
        self.unten = unten
        self.links = links
        self.rotation = rotation

    def __str__(self) -> str:
        return (str(self.nummer) + "(" + 
            #str(self.oben) + "," + 
            #str(self.rechts) + "," + 
            #str(self.unten) + "," + 
            #str(self.links) + ")(" +
            str(self.rotation) + ")")

    def __repr__(self) -> str:
        return (str(self.nummer) + "(" + 
            #str(self.oben) + "," + 
            #str(self.rechts) + "," + 
            #str(self.unten) + "," + 
            #str(self.links) + ")(" +
            str(self.rotation) + ")")
    
    def copy(self):
        return Card(self.nummer,
            self.oben.copy(),
            self.rechts.copy(),
            self.unten.copy(),
            self.links.copy(),
            self.rotation);

    def reset_rotation(self):
        rotation = 0

    def rotate_clockwise(self):
        if (self.rotation == ROTATION_KEINE):
            self.rotation = ROTATION_VIERTEL
        elif (self.rotation == ROTATION_VIERTEL):
            self.rotation = ROTATION_HALB
        elif (self.rotation == ROTATION_HALB):
            self.rotation = ROTATION_DREIVIERTEL
        elif (self.rotation == ROTATION_DREIVIERTEL):
            self.rotation = ROTATION_VOLL
        else:
            self.rotation = ROTATION_KEINE

    def check_rechts(self, other):
        c1 = Card.get_rechts(self)
        c2 = Card.get_links(other)
        return c1.suites(c2)

    def check_links(self, other):
        c1 = Card.get_links(self)
        c2 = Card.get_rechts(other)
        return c1.suites(c2)

    def check_oben(self, other):
        c1 = Card.get_oben(self)
        c2 = Card.get_unten(other)
        return c1.suites(c2)

    def check_unten(self, other):
        c1 = Card.get_unten(self)
        c2 = Card.get_oben(other)
        return c1.suites(c2)

    def get_rechts(card) -> Connector:
        if (card.rotation == ROTATION_KEINE):
            return card.rechts
        elif (card.rotation == ROTATION_VIERTEL):
            return card.oben
        elif (card.rotation == ROTATION_HALB):
            return card.links
        elif (card.rotation == ROTATION_DREIVIERTEL):
            return card.unten

    def get_unten(card) -> Connector:
        if (card.rotation == ROTATION_KEINE):
            return card.unten
        elif (card.rotation == ROTATION_VIERTEL):
            return card.rechts
        elif (card.rotation == ROTATION_HALB):
            return card.oben
        elif (card.rotation == ROTATION_DREIVIERTEL):
            return card.links

    def get_links(card) -> Connector:
        if (card.rotation == ROTATION_KEINE):
            return card.links
        elif (card.rotation == ROTATION_VIERTEL):
            return card.unten
        elif (card.rotation == ROTATION_HALB):
            return card.rechts
        elif (card.rotation == ROTATION_DREIVIERTEL):
            return card.oben

    def get_oben(card) -> Connector:
        if (card.rotation == ROTATION_KEINE):
            return card.oben
        elif (card.rotation == ROTATION_VIERTEL):
            return card.links
        elif (card.rotation == ROTATION_HALB):
            return card.unten
        elif (card.rotation == ROTATION_DREIVIERTEL):
            return card.rechts
