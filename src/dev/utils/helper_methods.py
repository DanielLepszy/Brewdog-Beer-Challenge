from datetime import datetime

class HelperMethods:

    def to_date_format(self,date_to_format:str, date_format:str) -> datetime:
        return datetime.strptime(date_to_format, date_format)

    