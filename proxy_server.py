from fastmcp import FastMCP
from fastmcp.server.providers import ProxyProvider
from fastmcp.server.providers.proxy import ProxyClient

REMOTE_URL = "https://first-remote.fastmcp.app/mcp"

proxy = ProxyProvider(lambda: ProxyClient(REMOTE_URL))
mcp = FastMCP("Proxy ExpenseTracker", providers=[proxy])


if __name__ == "__main__":
    mcp.run()