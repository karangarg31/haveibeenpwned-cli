#!/usr/bin/env python3

# TODO: Add paste functionality

import os
import sys
import requests
import argparse

from hibpcli import HIBPCli

hibp_cli = HIBPCli()
def _get_and_validate_cli_args():
    arg_parser = argparse.ArgumentParser(
        description="Command Line Interface for haveibeenpwned.com",
        epilog="Hope you enjoy using it - Karan",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
    action_argparse = arg_parser.add_mutually_exclusive_group()
    action_argparse.add_argument('--get-breaches', dest='get_breaches', action='store_true', help="Get breaches. Can be filtered based on account") 
    action_argparse.add_argument('--list-fields', dest='list_fields', action='store_true', help="Get list of fields available for breaches") 

    arg_parser.add_argument('--account-name', dest='account_name', action='store', metavar="mail@example.com", help="return breaches for a specific account")
    arg_parser.add_argument('--truncate-response', dest='is_full_response', action='store_false', default=True, help="Return only title of the breaches.")
    arg_parser.add_argument('--domain', dest="domain_name", action="store", metavar='adobe.com', help="return breaches that happened on a specific domain")
    arg_parser.add_argument('--verified-only' , dest='exclude_unverified_breach', action='store_true', default=False, help="Only show verified breaches.")
    arg_parser.add_argument('--show-all-fields', dest="show_all_fields", action="store_true", default=False, help="Show all fields. By default, fields Description and LogoPath are not shown. This may affect how data renders due to long values")

    output_format_argparse = arg_parser.add_mutually_exclusive_group()
    output_format_argparse.add_argument('--output-format' , dest='output_format', default="table", choices=('json', 'table', 'html', 'quiet'), help="Output Format.")
    output_format_argparse.add_argument('--quiet' , dest='output_format', action='store_const', const='quiet', help="Does not print output. Exits with 0 if no breach found, 1 otherwise")

    arg_parser.add_argument('--file-name', action="store", dest="file_name", help="File name where to create a graphical report. Only considered for output format pdf or html")

    args = arg_parser.parse_args()
    if not (args.get_breaches or args.list_fields):
        arg_parser.error("No action requested. Need either --get-breaches or --list-fields")
    
    if not args.file_name and args.output_format in ('pdf', 'html'):
        arg_parser.error("--file-name is required if --output-format is pdf or html")
    return args

def _get_breach(args):
    return hibp_cli.get_breach(
        account_name=args.account_name,
        is_full_response=args.is_full_response,
        domain_name=args.domain_name,
        exclude_unverified_breach=args.exclude_unverified_breach
        )

def _list_fields():
    print(hibp_cli.list_fields())

def _exit_based_on_response(res):
    if res.cnt > 0 :
        sys.exit(1)
    else:
        sys.exit(0)

def _print_result(res, args):
    if args.show_all_fields:
        res.show_all_fields = True

    if args.output_format in ('pdf', 'html'):
        res.to_file(
            filetype=args.output_format,
            filename=args.file_name,
            )
        return
    
    if args.output_format == 'json':
        res.print_json()
        return

    if args.output_format == 'table':
        res.print_table()
        return
    

def _handle_breach_output_action(res, args):
    if args.output_format == 'quiet':
        _exit_based_on_response(res)
    _print_result(res, args)

        
if __name__ == '__main__':
    res = None
    args = _get_and_validate_cli_args()

    if args.get_breaches :
        res = _get_breach(args)
        _handle_breach_output_action(res, args) 
    
    if args.list_fields :
        res = _list_fields()

