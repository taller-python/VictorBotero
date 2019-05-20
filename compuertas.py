class compuerta(object):
    def __init__(self, a,b):
        self.entrance_a = a
        self.entrance_b = b

"""    @property
    def entrance_a(self):
        return self.entrance_a

    @property
    def entrance_b(self):
        return self.entrance_b

    @entrance_a.setter
    def entrance_a(self,number):
        self.entrance_a = number

    @entrance_b.setter
    def entrance_b(self,number):
        self.entrance_b = number"""

class compuertOR(compuerta):
    """child class of compuerta"""
    """def __init__(self, a,b):
        self.entrance_a = a
        self.entrance_b = b

    @property
    def entrance_a(self):
        return self.entrance_a

    @property
    def entrance_b(self):
        return self.entrance_b

    @entrance_a.setter
    def entrance_a(self,number):
        self.entrance_a = number

    @entrance_b.setter
    def entrance_b(self,number):
        self.entrance_b = number"""

    def __str__(self):
        returned_value = '1'
        if self.entrance_a == '0' and self.entrance_b == '0': returned_value = '0'
        return returned_value

class compuertAND(compuerta):
    """child class of compuerta"""
    def __init__(self, a,b):
        self.entrance_a = a
        self.entrance_b = b

    """@property
    def entrance_a(self):
        return self.entrance_a

    @property
    def entrance_b(self):
        return self.entrance_b

    @entrance_a.setter
    def entrance_a(self,number):
        self.entrance_a = number

    @entrance_b.setter
    def entrance_b(self,number):
        self.entrance_b = number"""

    def __str__(self):
        returned_value = '0'
        if self.entrance_a == '1' and self.entrance_b == '1' : returned_value = '1'
        return returned_value
