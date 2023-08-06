# Scrape Data Cleaner
Clean scraped data fields to recieve your disired text without unicodes,spaces and other unessesary quirks.
# Installation
`pip install scrape-data-cleaner`
# Usage
```python
from cleaner import string_cleaner,price_cleaner,remove_char
print(string_cleaner('Iphone 8   plus   '))
print(price_cleaner(remove_char('USD 100')))
```