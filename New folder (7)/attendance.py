class StudentAttendance:
    def __init__(self):
      
        self.attendance_record = {}

    def mark_attendance(self, roll_number, status):
 
        self.attendance_record[roll_number] = status

    def check_attendance(self, roll_number):

        if roll_number in self.attendance_record:
            return "Present" if self.attendance_record[roll_number] else "Absent"
        else:
            return "Roll number not found"

attendance_system = StudentAttendance()
attendance_system.mark_attendance(101, True) 
attendance_system.mark_attendance(102, False)  

print("Student with roll number 101 is", attendance_system.check_attendance(101))
print("Student with roll number 102 is", attendance_system.check_attendance(102))
print("Student with roll number 103 is", attendance_system.check_attendance(103)) 