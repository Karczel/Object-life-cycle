"""Registrar knows all the Courses offered by the university.
   It reads course data from a file, defined in the COURSES_FILE constant.

   Do Not Modify This File.
   Don't Waste Time Reading This Code -- it won't help you on the exam!

   Requires Python 3.9 or newer.
"""
import logging
from typing import Iterable, Iterator
from course import Course
from serializer import Serializer

# Location and name of a file containing course data.
# If file is not in the current directory, include a path.
COURSES_FILE = "courses.csv"


class Registrar(Iterable[Course]):
    """Registrar manages courses.

    This class is a Singleton. The same instance can be accessed
    repeatedly by using `registrar = Registrar()`.
    `get_courses()`          - returns a list of all known courses
    `get_course("019999999") - get one course using course id

    >>> registrar = Registrar()
    >>> prog2 = registrar.get_course("01219116")
    >>> prog2.name
    'Computer Programming II'
    >>> prog2.credits
    3
    >>> registrar.get_course('09999999') is None
    True
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Create and initialize a single instance of the Registrar."""
        if not cls._instance: #if None
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.courses = {}
            cls._instance.load_courses(COURSES_FILE)
            cls._instance.logger = logging.getLogger("Registrar")
        return cls._instance

    def __len__(self) -> int:
        """Number of courses in the course catalog."""
        return len(self.courses)

    def __iter__(self) -> Iterator[Course]:
        """Create an iterator for courses in the catalog."""
        return iter(self.courses.values())

    def get_courses(self) -> list:
        """Get a list of all the courses in the course catalog."""
        return self.courses.values()

    def get_course(self, course_id: str) -> Course:
        """Return one Course for a given course id (a string).

        :param course_id: course number to find (8-digits at KU)
        :return: a matching Course or None if no matching course_id
        """
        return self.courses.get(course_id)

    def load_courses(self, course_file: str) -> None:
        """Read the course data and create courses.

        :param course_file: file containing course data in a known format.
        :raises Exception: if file does not exist or does not contain valid course data
        """
        courses_list = Serializer().read_courses(course_file)
        self.courses = { course.course_id: course for course in courses_list }

    def save_courses(self, filename: str) -> None:
        """Write the course catalog to a file.

        :param filename: name of a new file to write course data to
        """
        Serializer().write_courses(filename, self.courses.values())

