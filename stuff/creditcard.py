import re
from datetime import datetime
import valideer


class CreditCard(object):
    _VALIDATOR = valideer.parse({"name": valideer.String(min_length=1, max_length=30),
                                 "+expires": datetime,
                                 "+number": valideer.Pattern(r"^\d{15,16}$"),
                                 "cvv": valideer.String(max_length=41),
                                 "track1": valideer.Pattern(r"^B\d{0,19}\^[\w\s\/]{2,26}\^\d{7}\w*$"),
                                 "track2": valideer.Pattern(r"\d{0,19}=\d{7}\w*"),
                                 "zip":  valideer.String(max_length=10)})
    _CARD_BRANDS = {"Visa": re.compile(r"/^4[0-9]{12}(?:[0-9]{3})?$/"),
                    "Mastercard": re.compile(r"/^5[1-5][0-9]{14}$/"),
                    "Diners Club": re.compile(r"/^3(?:0[0-5]|[68][0-9])[0-9]{11}$/"),
                    "American Express": re.compile(r"/^3[47][0-9]{13}$/"),
                    "JBC": re.compile(r"/^35/"),
                    "Discover": re.compile(r"/^6(?:011|5[0-9]{2})[0-9]{12}$/")}
    _TRACKS = [re.compile(r"^%B\d{0,19}\^[\w\s\/]{2,26}\^\d{7}\w*\?$"),
               re.compile(r";\d{0,19}=\d{7}\w*\?")]

    def __init__(self, **kwargs):
        self._number = str(kwargs.get('number'))
        self._track1 = str(kwargs.get('track1'))
        self._track2 = str(kwargs.get('track2'))
        self._expires = datetime.strptime(kwargs.get('expires'), "%y%m") if kwargs.get('expires') else None
        self._name = kwargs.get('name')
        self._zip = kwargs.get('zip')
        self._cvv = kwargs.get('cvv')
        self._VALIDATOR.validate(dict([data for data in (("name", self._name),
                                                         ("expires", self._expires),
                                                         ("track1", self._track1),
                                                         ("track2", self._track2),
                                                         ("zip", self._zip),
                                                         ("cvv", self._cvv),
                                                         ("number", self._number)) if data[1]]))

    @property
    def number(self):
        return self._number

    @property
    def track1(self):
        return self._track1

    @property
    def track2(self):
        return self._track2

    @property
    def expires(self):
        return self._expires

    @property
    def cvv(self):
        return self._cvv

    @property
    def zip(self):
        return self._zip

    @property
    def brand(self):
        for brand in self._CARD_BRANDS.items():
            if brand[1].match(self.number):
                return brand[0]
        return "Gift"

    @classmethod
    def from_swipe(self, swipe):
        # decode swipe
        tracks = re.split(r"[\t\n]", swipe)
        return CreditCard(number=re.search(r"\d+", tracks[0]).group(),
                          track1=tracks[0],
                          track2=tracks[1],
                          expires=re.search(r"\^(\d{4})", tracks[0]).group()[1:],
                          name=re.search(r"\^([^\s]+)", tracks[0]).group()[1:])

    @classmethod
    def random(self):
        """Generage a random credit card for example
        """
        pass
