# Stuff

Common stuff that needs parsing

### CreditCard

```python
from stuff import CreditCard
card = CreditCard.from_swipe("%B4111111111111111^SMITH/JOHN ^15204041234567891234?\$n;4111111111111111=152024041234567891234?")
card.number
>>> 4111111111111111
card.expires
>>> datetime.datetime(month=15, year=2020)
```

### Address

```python
from stuff import Address
a = Address("1 ininity loop, california")
```
