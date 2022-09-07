#!/usr/bin/env python3

# TODO: Add paste functionality

import os
import sys
import requests
import argparse

from hibpcli import HIBPCli

hibp_cli = HIBPCli()
def _get_cli_args():
    arg_parser = argparse.ArgumentParser(
        description="Command Line Interface for haveibeenpwned.com",
        epilog="Hope you enjoy using it - Karan"
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

def _get_breach(input_cli_args):
    hibp_cli.get_breach(
        account_name=input_cli_args.account_name,
        is_full_response=input_cli_args.is_full_response,
        domain_name=input_cli_args.domain_name,
        exclude_unverified_breach=input_cli_args.exclude_unverified_breach
        )

def _exit_based_on_response(res):
    if res.cnt > 0 :
        sys.exit(1)
    else:
        sys.exit(0)

def _handle_output_action(res, output_format):
    if output_format == 'quiet':
        _exit_based_on_response(res)
    print(res)

if __name__ == '__main__':
    res = None
    input_cli_args, _ = _get_cli_args()

    if input_cli_args.get_breaches :
        res = _get_breach(input_cli_args)

    _handle_output_action(res, input_cli_args.output_format) 
