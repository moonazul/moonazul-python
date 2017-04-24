# moonazul-python

## How to use
```python
import unittest
import moonazul


class TestValidators(unittest.TestCase):
    def test_zip_code_validator(self):
        moonazul.validate_zip_validator(self, validate_zip)

```