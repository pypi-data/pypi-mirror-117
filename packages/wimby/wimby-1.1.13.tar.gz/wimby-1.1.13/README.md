![](/resources/banner.png)

# wimby
Wimby is a lean cryptocurrency analytics, using periodic weighted averages.

## Official Release
**Wimby** can now be used on your Python projects through PyPi by running pip command on a Python-ready environment.

`pip install wimby --upgrade`

## Usage
**1. Import Package**
```python
from wimby import Wimby
```

**2. Initialization**
```python
# set a list of coin aliases
coins = ["bitcoin"]

# initialize
analytics = Wimby(coins)

# aliased coin validation
coins = ["btc"]
analytics = Wimby(coins, aliased=True)

# add coin aliases one-by-one
analytics.add("eth")

# or replace with new a list of coins
coins = ["ethereum", "dogecoin"]
analytics.change(coins)

# perform analysis
analytics.analyze()

# arkivist object
momentum = analytics.momentum

# arkivist object
movers = analytics.movers

```