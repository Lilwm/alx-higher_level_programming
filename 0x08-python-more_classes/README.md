## 0x08. Python - More Classes and Objects
All files are incremental builds to a class.

# instructions

Write a class Rectangle that defines a rectangle by:
  -  Private instance attribute: width
  -   Private instance attribute: height:
  -   Public class attribute number_of_instances
        *Initialized to 0
        *Incremented during each new instance instantiation
        *Decremented during each instance deletion
   - Public class attribute print_symbol
        - Initialized to #
        - Used as symbol for string representation
   -  Public instance method: def area(self): that returns the rectangle area
   -  Public instance method: def perimeter(self): that returns the rectangle perimeter:
   -  Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
   -  Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size
