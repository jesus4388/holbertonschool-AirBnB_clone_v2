#!/usr/bin/python3
"""Unit tests for console.py"""

import unittest
import pycodestyle
from console import HBNBCommand
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.place import Place
from models.review import Reiew
from models.state import State
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
import os
from os.path import exists

class ConsoleTest(unittest.TestCase):
    """test for console.py"""

    def test_pep8(self):
        """Check PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['console.py'])
        self.assertEqual(
            check.total_errors, 0, "Found style errors"
        )
