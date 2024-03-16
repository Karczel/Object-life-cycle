import logging
# configure logging. Normally do this in your "app" script.
logging.basicConfig(level=logging.INFO,
                   format="%(levelname)s %(funcName)8s: %(message)s"
                   )

class MyMeta(type):
   """Custom metaclass extends 'type'."""


   def __call__(cls, *args, **kwargs):
       logging.info("override __call__")
       # instance = super().__call__(*args, **kwargs)
       # instance = cls.__new__(cls)
       # instance.__init__(*args, **kwargs)
       # Use the default behavior:
       # instance = super().__call__(*args, **kwargs)
       # return instance

       print('sorry, objects are on strike!')
       return None

# class Person(metaclass=type):
class Person(metaclass=MyMeta):
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

