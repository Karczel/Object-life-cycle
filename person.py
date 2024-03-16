import logging
# configure logging. Normally do this in your "app" script.
logging.basicConfig(level=logging.INFO,
                   format="%(levelname)s %(funcName)8s: %(message)s"
                   )


class Person:
   """Person with a name."""


   def __init__(self, name):
       logging.info(f"initialize Person('{name}')")
       self.name = name


   def __new__(cls, *args, **kwargs):
       logging.info(f"allocate a new Person")
       return super().__new__(cls)


   def __del__(self):
       logging.info(f"destroying {self}")
       del self.name


   def __str__(self):
       return f"{type(self).__name__}('{self.name}')"

