from datetime import datetime,timedelta
import json

class Timer:
    def __init__(self) -> None:
        self.Config = json.load( open("Modules//config.json",'r') )
        self.Duration = timedelta( seconds = int(self.Config["time"]["duration"]) )

        self.Timers = [
            datetime.strptime( self.Config["time"]["morning"] , "%H:%M:%S" ),
            datetime.strptime( self.Config["time"]["afternoon"],"%H:%M:%S" )
            ]
        

    def CanTakeAttendance(self) -> bool:
        now = datetime.now()
        return ( 
                (
                    now > (self.Timers[0]) and 
                    now < (self.Timers[0] + self.Duration)
                )  or 
                (
                    now > (self.Timers[1]) and 
                    now < (self.Timers[1] + self.Duration)
                )
            )