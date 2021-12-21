# PyFract
A simple implementation of fraction numbers in Python. In some cases it is better than default Python library for fractions.

## Instalation
```
pip install pyfract
```

## Usage
### Initialization
```python
from pyfract.fraction import Fraction

f = Fraction(1, 2)
print(f) # [1/2]

f = Fraction(numerator=1, denominator=2)
print(f) # [1/2]
```

### Mathematical operations
You can use all of the math operations with other fraction, int or float as shown in the example below
```python
from pyfract.fraction import Fraction

f1 = Fraction(1, 2)
f2 = Fraction(1, 4)

print(f1 + f2) # [3/4]
print(f1 - f2) # [1/4]
print(f1 * f2) # [1/8]
print(f1 / f2) # [2/1]

print(f1 + 2) # [5/2]
print(f1 - 2) # [-3/2]
print(f1 * 2) # [1/1]
print(f1 / 2) # [1/4]
```

### Comparisons
You can compare fractions using operators like greater than, less than and so on...
```python
from pyfract.fraction import Fraction

f1 = Fraction(1, 2)
f2 = Fraction(1, 4)

print(f1 < f2) # False
print(f1 <= f2) # False
print(f1 > f2) # True
print(f1 >= f2) # True
print(f1 == f2) # False
print(f1 != f2) # True
```

### Conversion from float
```python
from pyfract.fraction import Fraction

print(Fraction.from_float(0.5)) # [1/2]
print(Fraction.from_float(0.134)) # [67/500]
```

### Accurate conversion from float
Fast conversion from float doesn't work so well for float like `0.333333333333333333`. This method is much slower, but allows to convert floats more accurately
```python
from pyfract.fraction import Fraction

x = 1 / 3
print(x) # 0.3333333333333333
f = Fraction.from_float_accurately(x)
print(f) # [1/3]
```
`accuracy` defines up to how many decimal places the fraction must be accurate. By default it is `8`
```python
from pyfract.fraction import Fraction

f = Fraction.from_float_accurately(0.31987398749812214, accuracy=10)
print(f) # [44981/140621]
```
### To float
```python
from pyfract.fraction import Fraction

f = Fraction(1, 2)
print(f.to_float()) # 0.5
```

## Contributing
Make a fork of this repository, clone codebase, create new branch, make your changes, commit it, push to remote, create pull request to this repository. Any contribution highly appreciated
