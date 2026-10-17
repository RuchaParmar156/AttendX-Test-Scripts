
import unittest
from attendx_app import mark_attendance


class TestAttendanceMarking(unittest.TestCase):

    def test_mark_present(self):
        result = mark_attendance("STU001", "Present")
        self.assertEqual(result["status"], "Present")
        self.assertEqual(result["student_id"], "STU001")

    def test_mark_absent(self):
        result = mark_attendance("STU002", "Absent")
        self.assertEqual(result["status"], "Absent")

    def test_missing_student_id(self):
        with self.assertRaises(ValueError):
            mark_attendance("", "Present")

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            mark_attendance("STU003", "Late")

    def test_duplicate_attendance(self):
        with self.assertRaises(ValueError):
            mark_attendance(
                "STU001",
                "Present",
                existing_records={"STU001"}
            )


if __name__ == "__main__":
    unittest.main()
