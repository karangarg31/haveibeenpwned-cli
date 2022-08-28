#!/usr/bin/env python3

import os
import requests
import argparse

from hibpcli import HIBPCli

# truncateResponse (default true)
# domain
# includeUnverified (default true)
def get_cli_args():
    arg_parser = argparse.ArgumentParser(
        description="Command Line Interface for haveibeenpwned.com",
        epilog="Hope you enjoy it - Karan"
        )
    breach_params = arg_parser.add_argument_group('Breach Parameters','Parameters to use to get breach information')
    # paste_params = arg_parser.add_argument_group('Paste Parameters','Parameters to use to get paste information')
    # common_params = arg_parser.add_argument_group('Common Parameters','Parameters that can be applied to both breach and paste')
    breach_params.add_argument('-a', '--account-name', dest='account_name', action='store', required=True, metavar="mail@example.com")
    breach_params.add_argument('-f', '--full-response', action='store_true', default=False)
    return arg_parser.parse_args()

def pop_filter_args():
    ## Arguments that start with "filter" are popped out to filter the output
    pass

if __name__ == '__main__':
    input_cli_args = get_cli_args()
    hibp_cli = HIBPCli()
    hibp_cli.get_account_breach(input_cli_args.account_name)