class WeeklySchedule:
    """Class for holding informations about set Weekly schedule
    
    Atributes:
        week (List): List of lenght 7 with list of daily events for each weekday
            Defaults to [[] in range(7)]
    """
    _schedule = [[] in range(7)] 

    def __init__(self, week: [] = [[] in range(7)]) -> None:
        """Initiale by setting schedule"""
        self.schedule(week)

    @_schedule.setter
    def schedule(self, week: [])-> None:
        """Setter"""
        if len(week != 7):
            raise ValueError(f'Expected a list of length {7}, received list of length {len(week)}')
        
        self._schedule = week

    @property
    def schedule(self) -> []:
        """Getter"""
        return self._schedule