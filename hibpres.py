import json
from tabulate import tabulate

class HIBPRes():
    def __init__(self, res: str) -> None:
        self.datastr = res
        self.data = self._validate_data_schema()
        self.cnt = self._get_data_count()
        self.fields = self._get_field_names()
    
    def _validate_data_schema(self):
        if len(self.datastr) == 0:
            return []
        return json.loads(self.datastr)

    def _get_data_count(self):
        return len(self.data)
    
    def _get_field_names(self):
        return self.data[0].keys()

    def __str__(self):
        return tabulate(self.data, tablefmt='html')
