OBEN = "oben"
UNTEN = "unten"
ROTATION_KEINE = 0
ROTATION_VIERTEL = 90
ROTATION_HALB = 180
ROTAIONN_DREIVIERTEL = 270

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

    def suites(self, other):
        return self.nummer == other.nummer and self.ausrichtung != other.ausrichtung

class Card:
    nummer = 0;
    rotation = ROTATION_KEINE;

    def __init__(self, nummer, oben, rechts, unten, links):
        self.nummer = nummer
        self.oben = oben
        self.rechts = rechts
        self.unten = unten
        self.links = links
    
    def reset_rotation(self):
        rotation = 0
    
    def rotate(self, rotation):
        self.rotation = rotation
    
    def check_rechts(self, other):
        return self.rechts.suites(other.links)

    def check_links(self, other):
        return self.links.suites(other.rechts)

    def check_oben(self, other):
        return self.oben.suites(other.unten)

    def check_unten(self, other):
        return self.unten.suites(other.oben)
