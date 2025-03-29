Give your chatbot access to your bank accounts!

Please remember that the LLM sees all MCP calls/responses, so if you don't want to share your banking accounts,
use a Local LLM!

Setup:

# Create a virtualenv
virtualenv venv
# Use it
source venv/bin/activate
# Install deps
pip install woob 'mcp[cli]'
# Setup your bank accounts
# This will prompt you for your bank credentials
woob bank

Once this is done, you can add the mcp server like this:
/where/is/woob-mcp-server/venv/bin/mcp run -t stdio /where/is/woob-mcp-server/run.py
