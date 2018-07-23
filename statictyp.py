"""Basic static typing support ; by weld, wtfpl 
"""
""" This :
        myInt = Type(int)
        a = myInt(5)
        print((a+a)())
    Should print:
        >>> 10
"""
 
class TypeError(Exception):
    pass

class UninitializedValue(Exception):
    pass

class CustomType:
    def __init__(self, classtype, value):
        self._t = classtype
        if value:
            if type(value) != self._t:
                raise TypeError
            self._val = value
        else:
            self._val = None

    def set_val(self, val):
        if type(val) != self._t:
            raise TypeError
        self._val = val

    def get_val(self):
        if self._val is None:
            raise UninitializedValue
        return(self._val)
   
    def get_type(self):
        return(self._t)

    def cast(self, classtype):
        return (CustomType(classtype, classtype(self.get_val())))

    def _sametype(function):
        def wrapper(a, b):
            if a.get_type() != b.get_type():
                raise TypeError
            return(CustomType(a.get_type(), a.get_type()(function(a.get_val(), b.get_val()))))
        return(wrapper)

    def __call__(self, val=None):
        return(self.set_val(val) if val else self.get_val())
    
    @_sametype
    def __eq__(self, op):
        return(self == op)

    @_sametype
    def __lt__(self, op):
        return(self < op)

    @_sametype
    def __le__(self, op):
        return(self <= op)

    @_sametype
    def __ne__(self, op):
        return(self != op)

    @_sametype
    def __ge__(self, op):
        return(self >= op)

    @_sametype
    def __grt__(self, op):
        return(self > op)

    @_sametype
    def __add__(self, op):
        return(self + op)
        
    @_sametype
    def __sub__(self, op):
        return(self - op)
    
    @_sametype
    def __mul__(self, op):
        return(self * op)

    @_sametype
    def __matmul__(self, op):
        return(self @ op)
    
    @_sametype
    def __truediv__(self, op):
        return(self / op)

    @_sametype
    def __floordiv__(self, op):
        return(self // op)

    @_sametype
    def __mod__(self, op):
        return(self % op)

    @_sametype
    def __pow__(self, op):
        return(self ** op)

    @_sametype
    def __lshift__(self, op):
        return(self << op)

    @_sametype
    def __rshift__(self, op):
        return(self >> op)
    
    @_sametype
    def __and__(self, op):
        return(self & op)

    @_sametype
    def __xor__(self, op):
        return(self ^ op)

    @_sametype
    def __or__(self, op):
        return(self | op)


class Type:
    def __init__(self, classtype):
        if type(classtype) != type:
            raise ValueError
        self._t = classtype

    def __call__(self, val=None):
        return(CustomType(self._t, val))
