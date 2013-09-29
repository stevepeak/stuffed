# Stuffed

[![Build Status](https://secure.travis-ci.org/stevepeak/stuffed.png)](http://travis-ci.org/stevepeak/stuffed)

### CreditCard

```python
from stuffed import CreditCard
card = CreditCard.from_swipe("%B4111111111111111^SMITH/JOHN ^15024041234567891234?\n;4111111111111111=150224041234567891234?")
card.number
>>> "4111111111111111"
card.expires
>>> datetime.datetime(month=15, year=2020, day=01)
```

### Address

```python
from stuffed import Address
a = Address("1 ininity loop, california")
```
