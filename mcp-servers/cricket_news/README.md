# SAMPLE MCP SERVER 

# Cricket News MCP Server

This is a sample MCP server for fetching and managing cricket news. It demonstrates how to create a new MCP server using the MCP framework.

## Getting Started

Follow these steps to set up and run the Cricket News MCP server:

### Prerequisites
- Python 3.8 or higher
- `uv` installed: [UV GitHub Repository](https://github.com/astral-sh/uv)

### Steps to Create the Server

1. **Initialize the Project**
   ```bash
   uv init cricket_news
   cd cricket_news
   ```

2. **Set Up a Virtual Environment**
   ```bash
   uv venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   uv add "mcp[cli]" httpx
   ```

4. **Create the Main Server File**
   Create a file named `cricket_news.py` with the following content:
   ```python
   from mcp.server.fastmcp import FastMCP

   app = FastMCP("cricket_news")

   @app.tool()
   async def get_latest_news() -> str:
       """Fetch the latest cricket news."""
       return "Here are the latest cricket news updates!"

   if __name__ == "__main__":
       app.run(transport="stdio")
   ```

5. **Run the Server**
   ```bash
   uv run cricket_news.py
   ```

## Example Usage

Once the server is running, you can use the MCP client to interact with it. For example:

```bash
mcp-client query cricket_news get_latest_news
```

This will return the latest cricket news.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.