# MCP Hub Documentation

## Overview
MCP Hub is a framework for creating and managing Model Context Protocol (MCP) servers and clients. It leverages the `uv` tool for fast package installation and configuration management.

## Why Use UV?
UV simplifies package management and configuration with blazing-fast commands. Learn a few commands to get started, and you're good to go:

- Initialize a project:
  ```bash
  uv init
  ```
- Sync Python version and dependencies:
  ```bash
  uv sync
  ```

For more details, visit the [UV GitHub repository](https://github.com/astral-sh/uv).

## Motivation
To understand the basics of MCP and get started with creating MCP servers, refer to the [MCP Quickstart Server Guide](https://modelcontextprotocol.io/quickstart/server).

## Getting Started

### How to Create a Sample MCP Server

1. **Create a New Project Directory**
   ```bash
   uv init XYZ
   cd XYZ
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

4. **Create the Server File**
   ```bash
   touch XYZ.py
   ```

### How to Run the MCP Server
To run the server, use the following command:
```bash
uv run XYZ.py
```

## Example: Creating a New XYZ Server

Follow the steps outlined above to create and run a new XYZ server. Replace `XYZ` with your desired project name.


<!-- Git hub copilot automation with git mcp server  -->
 "github": {
            "command": "docker",
            "args": [
                "run",
                "-i",
                "--rm",
                "-e",
                "GITHUB_PERSONAL_ACCESS_TOKEN",
                "ghcr.io/github/github-mcp-server"
            ],
            "env": {
                "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR API KEY>"
            }
        }