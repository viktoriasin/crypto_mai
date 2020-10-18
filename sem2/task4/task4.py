class Node:
    def __init__(self, value, mode):
        self.value = value
        self.mode = mode

    def check_mode_equals(self, other):
        if self.mode != other.mode:
            return False
        return True

    def __add__(self, other):
        if self.check_mode_equals(other):
            new_val = (self.value + other.value)
            return Node(new_val, self.mode)
        else:
            raise ValueError("The modes of numbers must be equal!")

    def __mul__(self, other):
        if self.check_mode_equals(other):
            new_val = (self.value * other.value)
            return Node(new_val, self.mode)
        else:
            raise ValueError("The modes of numbers must be equal!")

    def __pow__(self, power):
        new_val = (self.value ** power)
        return Node(new_val, self.mode)

    def __eq__(self, other):
        if self.check_mode_equals(other):
            if self.value == other.value:
                return True
            return False
        else:
            raise ValueError("The modes of numbers must be equal!")

    def __neg__(self):
        return Node(-self.value, self.mode)

    def __sub__(self, other):
        if self.check_mode_equals(other):
            neg_node = -other
            return self.__add__(neg_node)
        else:
            raise ValueError("The modes of numbers must be equal!")

    def equality_by_modulo(self, other):
        if self.check_mode_equals(other):
            if self.value % self.mode == other.value % self.mode:
                return True
            return False
        else:
            raise ValueError("The modes of numbers must be equal!")

