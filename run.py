#!/usr/bin/env python3

import asyncio
from mcp.server.fastmcp import FastMCP
from woob.core import Woob
from woob.capabilities.bank import CapBank
import yaml
import sys
import json
import requests
from datetime import datetime

mcp = FastMCP("woob", dependencies=['woob'])

@mcp.tool()
def bank_get_accounts() -> str:
    """
    List user's banking accounts, including their balance
    """
    w = Woob()
    w.load_backends(CapBank)
    s = ""
    for backend in list(w.iter_backends()):
        for account in list(backend.iter_accounts()):
            prefix = ''
            if account.balance > 0:
                prefix = '+'
            s += f"{backend.DESCRIPTION} -- {account.label} -- {prefix}{account.balance} {account.currency}\n"
    return s


if __name__ == '__main__':
    print(bank_get_accounts())
