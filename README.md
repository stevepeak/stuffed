# Stuffed

[![Build Status](https://secure.travis-ci.org/stevepeak/stuffed.png)](http://travis-ci.org/stevepeak/stuffed)
[![codecov.io](https://codecov.io/github/stevepeak/stuffed/coverage.svg?branch=master)](https://codecov.io/github/stevepeak/stuffed?branch=master)

## CreditCard

```python
from stuffed import CreditCard
card = CreditCard.from_swipe("%B4111111111111111^SMITH/JOHN ^15024041234567891234?\n;4111111111111111=150224041234567891234?")
card.number
>>> "4111111111111111"
card.expires
>>> datetime.datetime(month=15, year=2020, day=01)
```

## Address

#### Synchronous

```python
from stuffed import Address
a = Address("1 ininity loop, california")
a.name
>>> "Apple Inc."
a.state, a.country
>>> "CA", "US"
```

#### Asynchronous

```python
from stuffed import Address
import tornado.httpclient
import tornado.web

class RequestHandler(tornado.web.RequestHandler):
	def get(self, address):
		Address("1 ininity loop, california",
				httpclient=tornado.httpclient.AsyncHTTPClient(),
				callback=self.callback)

	def callback(self, address):
		self.finish(address.full)

```


## Email

Validation through Mailgun

```python
from stuffed import Email
e = Email('joe@anderson.com')
e.valid
>>> True
```

```python
e = Email('Victor@gmil.com')
e.valid
>>> False
e.suggestion
>>> "Victor@gmail.com"
```