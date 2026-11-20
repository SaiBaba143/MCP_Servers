from fastmcp import FastMCP

mcp = FastMCP.create_proxy("https://first-remote.fastmcp.app/mcp",
                       name="Proxy ExpenseTracker")

if __name__ == "__main__":
    mcp.run()