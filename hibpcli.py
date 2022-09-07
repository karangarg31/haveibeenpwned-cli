from typing import Union
import requests
import inspect
# from ratelimit import limits 

class HIBPCli():
    HIBP_API_URL = "https://haveibeenpwned.com/api"
    HIBP_API_VERSION = None
    REQUEST_HEADER_DICT = {
        "hibp-api-key"  : "92b20d288f334bb98b36a946b1c1568a",
        "user-agent"    : "karan-hibp-cli-linux" 
    }

    REQUEST_URI_DICT = {
        "_get_account_breach"    : "breachedaccount",
        "_get_all_breaches"      : "breaches",
    }

    def __init__(
        self,
        api_version : int = 3,
        ) -> None:
        self.HIBP_API_VERSION = api_version

    def _make_hibp_request(
        self,
        parameter: Union[str, int] = None,
        query_params:dict = None
        ):
        hibp_rest_resource = self.REQUEST_URI_DICT.get(inspect.stack()[1][3])
        hibp_url = f"{self.HIBP_API_URL}/v{self.HIBP_API_VERSION}/{hibp_rest_resource}"

        if parameter :
            hibp_url += f"/{parameter}"
        
        headers = self.REQUEST_HEADER_DICT
        hibp_response = self._execute_hibp_reqest(hibp_url, headers, query_params, parameter)
        print(hibp_response.text)

    # TODO: add exception handling
    # @limits(calls=1, period=1)
    def _execute_hibp_reqest(
        self,
        hibp_url,
        headers: dict = None,
        query_params: dict = None,
        parameter: Union[str, int] = None
        ):
        res = requests.get(hibp_url, headers=headers, params=query_params)
        if not ( (res.status_code == 200) or (parameter and res.status_code == 404) ):
            raise Exception(f"API Response code: {res.status_code} with error message: {res.text} for parameter: {parameter}")
        return res


    def is_account_breached(
        self,
        account_name : Union[str, int] = None
        ):
        pass

    def get_breach(
        self,
        account_name : Union[str, int] = None,
        is_full_response : bool = False,
        domain_name : str = None,
        exclude_unverified_breach : bool = False
        ):

        query_params={
            "truncateResponse" : not is_full_response,
            "domain" : domain_name,
            "includeUnverified" : not exclude_unverified_breach
            }

        if not account_name:
            self._get_all_breaches(query_params)
        else:
            self._get_account_breach(account_name, query_params)


    def _get_all_breaches(self, query_params):
        self._make_hibp_request(
            query_params=query_params
        )

    def _get_account_breach(self, account_name, query_params):
        self._make_hibp_request(
            parameter=account_name, 
            query_params=query_params
        )
