from person3 import Person
# person is the first version of Person, used to understand logging
# person2 is used to understand Metatype
# person3 is used to understand Singleton
# Singleton, to not get INFO __init__: initialize Person('Bird')
# see registrar.py from midterm for example

if __name__ == '__main__':
   p = Person("Bird")
   print("This is", p)
   q = Person("Cat")  # now nothing refers to Person("Bird")
   print("Now p is", p)
   c = Person("Dog")  # now nothing refers to Person("Cat")
   print("Now p is", p)

   print("p has id", id(p))
   print("q has id", id(q))
   print("c has id", id(c))
   print("Finished")

