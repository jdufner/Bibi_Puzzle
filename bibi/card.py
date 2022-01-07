OBEN = "oben"
UNTEN = "unten"
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
        return (str(self.nummer))

    def __repr__(self) -> str:
        return (str(self.nummer))
    
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
        return self.rechts.suites(other.links)

    def check_links(self, other):
        return self.links.suites(other.rechts)

    def check_oben(self, other):
        return self.oben.suites(other.unten)

    def check_unten(self, other):
        return self.unten.suites(other.oben)
