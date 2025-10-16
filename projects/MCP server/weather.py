from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """Get the weather location."""
    if location.lower() == "san francisco":
        return "heavy rain"
    elif location.lower() == "los angeles":
        return "very hot"
    elif location.lower() == "san diego":
        return "extreme cold"
    else:
        return "no info about the provided location"

if __name__=="__main__":
    mcp.run(transport="streamable-http")