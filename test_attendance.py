import unittest

# Sample attendance logic for demonstration.
# This is not connected to a real AttendX application.

def mark_attendance(student_id, status):
    if not student_id:
        return "Student ID is required"
    if status not in ("Present", "Absent"):
        return "Invalid attendance status"
    return "Attendance marked successfully"


class AttendanceTests(unittest.TestCase):

    def test_mark_present(self):
        self.assertEqual(
            mark_attendance("ST101", "Present"),
            "Attendance marked successfully"
        )

    def test_mark_absent(self):
        self.assertEqual(
            mark_attendance("ST102", "Absent"),
            "Attendance marked successfully"
        )

    def test_empty_student_id(self):
        self.assertEqual(
            mark_attendance("", "Present"),
            "Student ID is required"
        )

    def test_invalid_status(self):
        self.assertEqual(
            mark_attendance("ST103", "Unknown"),
            "Invalid attendance status"
        )


if __name__ == "__main__":
    unittest.main()
