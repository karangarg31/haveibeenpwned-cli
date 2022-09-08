import json
from collections import OrderedDict
from tabulate import tabulate
from datetime import datetime

class HIBPRes():
    BREACH_MODEL = OrderedDict({
        'Name'          : 30,
        'Title'         : None,
        'Domain'        : None,
        'BreachDate'    : None,
        'AddedDate'     : None,
        'ModifiedDate'  : None,
        'PwnCount'      : None,
        'Description'   : 30,
        'DataClasses'   : 30,
        'IsVerified'    : None,
        'IsFabricated'  : None,
        'IsSensitive'   : None,
        'IsRetired'     : None,
        'IsSpamList'    : None,
        'IsMalware'     : None,
        'LogoPath'      : 30
    })

    OPTIONAL_FIELDS = ["Name", "Description", "LogoPath"]
    DATE_FIELDS = ["AddedDate", "ModifiedDate"]

    def __init__(self, res: str) -> None:
        self.datastr = res
        self.data = self._validate_data_schema()
        self.cnt = self._get_data_count()
        self.fields = self._get_field_names()
        self.show_all_fields = False
    
    def _validate_data_schema(self):
        if len(self.datastr) == 0:
            return []
        return json.loads(self.datastr)

    def _get_data_count(self):
        return len(self.data)
    
    def _get_field_names(self):
        if self._get_data_count() <= 0:
            return None
        return self.data[0].keys()
    
    def _get_formatted_breach_data(self, data_dict):
        # data_dict['Description'] = '\n'.join(textwrap.wrap(data_dict['Description']))
        data_dict['DataClasses'] = '\n'.join(data_dict['DataClasses'])
        
        for field_name in self.DATE_FIELDS:
            data_dict[field_name] = datetime.strptime(data_dict[field_name], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
        
        return data_dict

    def _filter_fields_from_data(self):
        if self.show_all_fields:
            return
        return [ {k: v for k, v in d.items() if k not in self.OPTIONAL_FIELDS} for d in self.data]

    def _get_output_data(self):
        data = self.data
        if not self.show_all_fields:
            data = self._filter_fields_from_data()
        return map(self._get_formatted_breach_data, data)

    def _get_tabulated_data(self):
        return tabulate(
            self._get_output_data(), 
            tablefmt='pretty', 
            headers="keys", 
            maxcolwidths=list(self.BREACH_MODEL.values())
            )

    def __str__(self):
        return self._get_tabulated_data()

    def print_table(self):
        print(self._get_tabulated_data())

    def print_json(self):
        pass

    def to_file(self, filetype, filename):
        pass

    def to_html(self, filename):
        self.to_file(filetype='html', filename=filename)

    def to_pdf(self):
        self.to_file(filetype='pdf', filename=filename)