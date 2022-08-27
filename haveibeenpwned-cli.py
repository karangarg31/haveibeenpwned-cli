#!/usr/bin/env python

import os
import requests
import argparse

request_header_map = {
    "hibp-api-key"  : "92b20d288f334bb98b36a946b1c1568a",
    "user-agent"    : "karan-hibp-cli-linux" 
}

# truncateResponse (default true)
# domain
# includeUnverified (default true)
def get_cli_args():
    arg_parser = argparse.ArgumentParser(
        description="Command Line Interface for haveibeenpwned.com",
        epilog="Hope you enjoy it - Karan"
        )
    arg_parser.add_argument_group('Breach_Parameters','Parameters to use to get breach information')
    arg_parser.add_argument_group('Paste_Parameters','Parameters to use to get paste information')
    arg_parser.add_argument_group('Common_Parameters','Parameters that can be applied to both breach and paste')
    Breach_Parameters.add_argument('-f', '--full-response', action='store_true')

def pop_filter_args():
    pass

def make_hibp_request():
    pass

def is_account_breached():
    pass

def parse_breach():
    pass

def parse_paste():
    pass

def get_account_breach():
    pass

def get_all_breaches():
    pass

def print_help_message():
    pass 

if __name__ == '__main__':
    print("hello world")