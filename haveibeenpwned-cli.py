#!/usr/bin/env python3

# TODO: Add paste functionality

import os
import requests
import argparse

from hibpcli import HIBPCli

hibp_cli = HIBPCli()
def _get_cli_args():
    arg_parser = argparse.ArgumentParser(
        description="Command Line Interface for haveibeenpwned.com",
        epilog="Hope you enjoy it - Karan"
        )
    arg_parser.add_argument('--get-breaches', required=True, dest='get_breaches', action='store_true') 
    arg_parser.add_argument('--account-name', dest='account_name', action='store', metavar="mail@example.com")
    arg_parser.add_argument('--truncate-response', dest='is_full_response', action='store_false', default=True)
    arg_parser.add_argument('--domain', dest="domain_name", action="store", metavar='adobe.com')
    arg_parser.add_argument('--verified-only' , dest='exclude_unverified_breach', action='store_true')

    output_format_argparse = arg_parser.add_mutually_exclusive_group()
    output_format_argparse.add_argument('--quiet' , dest='output_format', action='store_const', const='quiet')
    output_format_argparse.add_argument('--output-format' , dest='output_format', action='store', choices=['json', 'table', 'pdf', 'quiet'])

    return arg_parser.parse_known_args()

def _validate_cli_args(input_cli_args):
    pass

def _pop_filter_args(unknown_cli_args):
    ## Arguments that start with "filter" are popped out to filter the output
    pass

def _get_breach(input_cli_args):
    hibp_cli.get_breach(
        account_name=input_cli_args.account_name,
        is_full_response=input_cli_args.is_full_response,
        domain_name=input_cli_args.domain_name,
        exclude_unverified_breach=input_cli_args.exclude_unverified_breach
        )

def _is_account_breached(account_name):
    pass

if __name__ == '__main__':
    input_cli_args, unknown_cli_args = _get_cli_args()
    clean_cli_args = _validate_cli_args(input_cli_args)
    result_filter_args = _pop_filter_args(unknown_cli_args)
    if input_cli_args.get_breaches :
       _get_breach(input_cli_args) 