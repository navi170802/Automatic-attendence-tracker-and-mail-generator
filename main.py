from Modules.Attendance import AttendanceManager
from Modules.Timer import Timer
from time import sleep

if(__name__ == "__main__"):
    timer = Timer()
    attendanceManager = AttendanceManager()

    while(True):
        if( not timer.CanTakeAttendance() ):
            attendanceManager.checkForStudent()
        sleep(200)
