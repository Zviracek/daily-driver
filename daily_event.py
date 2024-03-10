class DailyEvent:
    """Class for represantation of daily events

    Atribute:
        start_time (int): start time of the event
        end_time (int): end time of the event
        name (str): display name of the event
    """
    _start_time = 0
    _end_time = 0
    _name = None

    def __init__(self, start_time: int, end_time: int, name: str) -> None:
        """Initiating _private variables"""
        self._start_time = start_time
        self._end_time = end_time
        self._name = name

    def from_to(self)-> [int, int]:
        """Getter for time interval of the event
            
        Returns:
            [int, int]: list of two int for start and end time
        """
        return[self._start_time, self._end_time]

    def get_name(self) -> str:
        """Getter"""
        return self._name 

