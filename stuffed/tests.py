import unittest
import stuffed
from datetime import datetime
from tornado.testing import AsyncTestCase
import tornado.httpclient

class CreditCardTest(unittest.TestCase):
    def test_one(self):
        c = stuffed.CreditCard.from_swipe("%B4111111111111111^SMITH/JOHN      ^15024041234567891234?\n;4111111111111111=150224041234567891234?")
        self.assertEqual(c.number, "4111111111111111")
        self.assertEqual(c.name, "SMITH/JOHN")
        self.assertEqual(c.track1, "%B4111111111111111^SMITH/JOHN      ^15024041234567891234?")
        self.assertEqual(c.track2, ";4111111111111111=150224041234567891234?")
        self.assertEqual(c.expires, datetime(day=01, month=2, year=2015))
        self.assertIsNone(c.zip)
        self.assertIsNone(c.cvv)

    def test_two(self):
        c = stuffed.CreditCard(number="4111111111111111",
                               expires="feb 2015")
        self.assertEqual(c.number, "4111111111111111")
        self.assertIsNone(c.name)
        self.assertIsNone(c.track1)
        self.assertIsNone(c.track2)
        self.assertEqual(c.expires, datetime(day=01, month=2, year=2015))
        self.assertIsNone(c.zip)
        self.assertIsNone(c.cvv)


class AddressAsync(AsyncTestCase):
    def test(self):
        a = stuffed.Address(httpclient=tornado.httpclient.AsyncHTTPClient(),
                            callback=self.callback,
                            address="Wisconsin State Capitol, Madison")
        self.assertEqual(a.street, None)
        self.assertEqual(a.state, None)
        self.assertEqual(a.city, None)
        self.assertEqual(a.country, None)
        self.wait()

    def callback(self, response):
        self.assertEqual(response.street, "2 E Main St")
        self.assertEqual(response.city, "Madison")
        self.assertEqual(response.state, "WI")
        self.assertEqual(response.latlng, (43.07466770000001, -89.38434559999999))
        self.assertEqual(response.name, "Wisconsin State Capitol")
        self.assertEqual(response.type, "establishment")
        self.stop()


class AddressTests(unittest.TestCase):
    def test_one(self):
        a = stuffed.Address("1 infinity loop, california")
        self.assertEqual(a.name, "Apple Inc.")
        self.assertEquals(a.city, "Cupertino")
        self.assertEqual(a.state, "CA")
        self.assertEqual(a.address, "1 Infinite Loop, Apple Inc., Cupertino, CA 95014, USA")
        self.assertEqual(a.street, "1 Infinite Loop")
        self.assertEqual(a.county, "Santa Clara")
        self.assertEqual(a.country, "US")
        self.assertEqual(a.latlng, (37.331741, -122.0303329))
        self.assertEqual(a.lat, 37.331741)
        self.assertEqual(a.lng, -122.0303329)

if __name__ == '__main__':
    unittest.main()
