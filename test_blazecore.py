# test_blazecore.py
"""
Tests for BlazeCore module.
"""

import unittest
from blazecore import BlazeCore

class TestBlazeCore(unittest.TestCase):
    """Test cases for BlazeCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlazeCore()
        self.assertIsInstance(instance, BlazeCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlazeCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
