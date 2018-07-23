# statictyp

This is a basic support of static typing in python.

## How to use it
 
 ```python
myType = Type(type) #int, float, str, ...
a = myType(value) #assigning value to our object myType
print((a+a)()) #if a.get_type() == int && a.get_val() == 5: it will print 10 
#basic operations supported (==, <, <=, !=, >=, >, +, -, *, @, /, //, %, **, <<, >>, &, ^, |)
```

```python
#auto commented
a.get_val()
a.get_type()
a.set_val(value)
a.cast(type)
```
