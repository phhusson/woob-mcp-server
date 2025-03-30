#!/usr/bin/env python3

# /// script
# dependencies = ["woob", "mcp"]
# ///


from mcp.server.fastmcp import FastMCP
from woob.core import Woob
from woob.capabilities.bank import CapBank
import argparse
from datetime import datetime
import argparse
import sys


mcp = FastMCP("woob", dependencies=['woob'])

@mcp.tool()
def bank_get_accounts() -> str:
    """
    List user's banking accounts, including their balance
    """
    w = Woob()
    w.load_backends(CapBank)
    s = "\n"
    for backend in list(w.iter_backends()):
        for account in list(backend.iter_accounts()):
            prefix = ''
            if account.balance > 0:
                prefix = '+'
            s += f"{backend.DESCRIPTION} -- {account.label} -- {prefix}{account.balance} {account.currency}\n"
    return s

def main():
    argparser = argparse.ArgumentParser(description="Woob MCP server")
    argparser.add_argument('--sse', action='store_true', help='Run in SSE mode (default stdio)')
    argparser.add_argument('--test', action='store_true', help='Test woob integration -- no MCP server')
    args = argparser.parse_args()

    if args.test:
        print(bank_get_accounts())
        sys.exit(0)
    transport = 'stdio'
    if args.sse:
        transport = 'sse'
    mcp.run(transport=transport)

if __name__ == '__main__':
    main()
