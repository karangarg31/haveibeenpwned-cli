from typing import Union
import requests
import inspect

class HIBPCli():
    HIBP_API_URL = "https://haveibeenpwned.com/api"
    HIBP_API_VERSION = None
    REQUEST_HEADER_DICT = {
        "hibp-api-key"  : "92b20d288f334bb98b36a946b1c1568a",
        "user-agent"    : "karan-hibp-cli-linux" 
    }

    REQUEST_URI_DICT = {
        "get_account_breach"    : "breachedaccount",
        "get_all_breaches"      : "breaches",
        "get_breach"            : "breach"
    }
    def __init__(
        self,
        api_version : int = 3,
        ) -> None:
        self.HIBP_API_VERSION = api_version

    def _make_hibp_request(
        self,
        parameter: Union[str, int] ,
        query_params:dict = None
        ):
        hibp_rest_resource = self.REQUEST_URI_DICT.get(inspect.stack()[1][3])
        hibp_url = f"{self.HIBP_API_URL}/v{self.HIBP_API_VERSION}/{hibp_rest_resource}"

        if parameter is not None:
            hibp_url += f"/{parameter}"
        print(hibp_url)
        
        res = requests.get(hibp_url, params=query_params, headers=self.REQUEST_HEADER_DICT)
        print(res.text)

    def is_account_breached(
        self,
        account_name : Union[str, int] = None
        ):
        pass

    def _parse_breach():
        pass

    def _parse_paste():
        pass

    def get_account_breach(
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

        self._make_hibp_request(
            parameter=account_name, 
            query_params=query_params
        )

    def get_all_breaches():
        pass
