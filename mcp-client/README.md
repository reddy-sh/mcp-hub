# MCP Client Documentation

## Motivation
For a quick start guide to creating an MCP client, refer to the official documentation: [MCP Quickstart Client](https://modelcontextprotocol.io/quickstart/client).

## Steps to Create an MCP Client

### 1. Create Project Directory
```bash
uv init mcp-client
cd mcp-client
```

### 2. Create Virtual Environment
```bash
uv venv
```

### 3. Activate Virtual Environment
#### On Windows:
```bash
.venv\Scripts\activate
```
#### On Unix or macOS:
```bash
source .venv/bin/activate
```

### 4. Install Required Packages
```bash
uv add mcp anthropic python-dotenv
```

### 5. Remove Boilerplate Files
```bash
rm main.py
```

### 6. Create the Main File
```bash
touch client.py
```

## How to Run the Client
To run the client, use the following command:
```bash
uv run client.py ../mcp-servers/weather/weather.py
```