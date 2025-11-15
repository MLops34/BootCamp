class Over:
    def show(self):
        return "I'm a Billionaire"
    
class Ride(Over):
    def show(self):
        return "I'm a Trillionaire"
    pass

s=Ride()
print(s.show())

# Next Show Methods Override the Previous One Because Core is Previous One got Overrided By python in Memory
#In memory, both classes store their own methods,
#but the child class method with the same name shadows or replaces the parent’s method when accessed through the child object.

# print(Over().show())   # I'm a Billionaire
# print(Ride().show())   # I'm a Trillionaire

# Final Clear Version (with your logic polished)

# ✅ Key Concept: Method Resolution and Overriding

# When you call a method using an object, Python first looks for that method inside the object’s own class (subclass).

# If the method is not found there, it then looks for it in the superclass (parent class) — and so on (this chain is called the MRO → Method Resolution Order).

# If the subclass defines a method with the same name as the parent class,
# the subclass method overrides (replaces) the parent’s version for that subclass only.

# The parent’s version is still available and will work fine if you create an object of the parent class.

# So — each class keeps its own method in memory,
# but the child’s method hides (shadows) the parent’s method when accessed through the child.
