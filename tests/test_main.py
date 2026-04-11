# tests/test_main.py

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from main import Package, DeliverySystem


class TestPackage(unittest.TestCase):

    def test_initial_status_is_created(self):
        pkg = Package("T001", "Alice", "Bob")
        self.assertEqual(pkg.get_status(), "CREATED")

    def test_status_updates_correctly(self):
        pkg = Package("T002", "Alice", "Bob")
        pkg.update_status("IN_TRANSIT")
        self.assertEqual(pkg.get_status(), "IN_TRANSIT")

    def test_history_records_previous_statuses(self):
        pkg = Package("T003", "Alice", "Bob")
        pkg.update_status("IN_TRANSIT")
        pkg.update_status("DELIVERED")
        self.assertIn("CREATED", pkg.get_history())
        self.assertIn("IN_TRANSIT", pkg.get_history())

    def test_delivery_system_tracks_package(self):
        system = DeliverySystem()
        pkg = Package("T004", "X", "Y")
        system.add_package(pkg)
        result = system.track_package("T004")
        self.assertIn("T004", result)

    def test_track_unknown_package_returns_not_found(self):
        system = DeliverySystem()
        result = system.track_package("UNKNOWN")
        self.assertEqual(result, "Package not found.")


if __name__ == '__main__':
    unittest.main()