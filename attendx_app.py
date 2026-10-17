
def login(username, password):
    """Validate the demo user's login credentials."""
    if not username or not password:
        return False

    return username == "student01" and password == "AttendX@123"


def mark_attendance(student_id, status, existing_records=None):
    """Mark attendance and prevent duplicate records."""
    if not student_id:
        raise ValueError("Student ID is required")

    if status not in ("Present", "Absent"):
        raise ValueError("Invalid attendance status")

    if existing_records is None:
        existing_records = set()

    if student_id in existing_records:
        raise ValueError("Attendance already marked")

    return {
        "student_id": student_id,
        "status": status
    }
