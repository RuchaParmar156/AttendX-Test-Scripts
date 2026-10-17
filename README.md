
# AttendX-Test-Scripts

## Project Description
This repository demonstrates version control of automated test
scripts for a student attendance application called AttendX.

## Files

- `attendx_app.py`: Contains sample login and attendance-marking
  functions used by the demonstration tests.
- `test_login.py`: Tests valid login, invalid password, empty
  username, and empty password.
- `test_attendance_marking.py`: Tests present and absent attendance,
  missing student ID, invalid status, and duplicate attendance.

## Requirements
- Python 3
- Git

The tests use Python's built-in `unittest` framework, so no
additional Python packages are required.

## Running the Tests

Run the login tests:

```bash
python -m unittest test_login.py -v
```

Run the attendance tests:

```bash
python -m unittest test_attendance_marking.py -v
```

Run all tests:

```bash
python -m unittest discover -v
```

## Purpose
Git and GitHub are used to track changes, maintain commit history,
and share test scripts among QA team members.

## Version Control

This project uses Git for local version control and GitHub
for remote storage and collaboration.
