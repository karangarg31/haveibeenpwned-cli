#!/usr/bin/env python3

import os
import requests
import argparse

from hibpcli import HIBPCli

def get_cli_args():
    arg_parser = argparse.ArgumentParser(
        description="Command Line Interface for haveibeenpwned.com",
        epilog="Hope you enjoy it - Karan"
        )
    breach_params = arg_parser.add_argument_group('Breach Parameters','Parameters to use to get breach information')
    # paste_params = arg_parser.add_argument_group('Paste Parameters','Parameters to use to get paste information')
    # common_params = arg_parser.add_argument_group('Common Parameters','Parameters that can be applied to both breach and paste')
    breach_params.add_argument('-a', '--account-name', dest='account_name', action='store', required=True, metavar="mail@example.com")
    breach_params.add_argument('-f', '--full-response', dest='is_full_response', action='store_true', default=False)
    breach_params.add_argument('-d', '--domain', dest="domain_name", action="store", metavar='adobe.com')
    breach_params.add_argument('--exclude-unverified' , dest='exclude_unverified_breach', action='store_true')
    return arg_parser.parse_args()

def pop_filter_args():
    ## Arguments that start with "filter" are popped out to filter the output
    pass

if __name__ == '__main__':
    input_cli_args = get_cli_args()
    hibp_cli = HIBPCli()
    hibp_cli.get_account_breach(
        account_name=input_cli_args.account_name,
        is_full_response=input_cli_args.is_full_response,
        domain_name=input_cli_args.domain_name,
        exclude_unverified_breach=input_cli_args.exclude_unverified_breach
        )