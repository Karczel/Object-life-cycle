"""singleton"""
import logging
# configure logging. Normally do this in your "app" script.
logging.basicConfig(level=logging.INFO,
                   format="%(levelname)s %(funcName)8s: %(message)s"
                   )


class Person:
   """Person with a name."""
   # class attribute thet refers to THE person
   #method 1: keep track if __init__ is already called
   _instance = None

   def __init__(self, name):
       logging.info(f"initialize Person('{name}')")
       self.name = name


   def __new__(cls, *args, **kwargs):
       """Allocate memory and return a reference to a new Person object."""
       # has a Person been created before?
       if cls._instance is None:
           # does not  exist yet
           cls._instance = super().__new__(cls)
           logging.info(f"allocate a new Person")
       return cls._instance


   def __del__(self):
       logging.info(f"destroying {self}")
       del self.name


   def __str__(self):
       return f"{type(self).__name__}('{self.name}')"

