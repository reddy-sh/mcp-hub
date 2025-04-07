# mcp-hub
mcp-hub


<!-- Why UV -->
UV is blazing fast package install and other config. learn few commands to start with and your good to go. 
uv init
<!-- update the python version .python-version and update in pyproject.toml -->
uv sync


https://github.com/astral-sh/uv

<!-- Motivation -->
https://modelcontextprotocol.io/quickstart/server

<!-- Getting started  -->
1. how to create a sample mcp server
2. what tools you need to build your first mcp server
3. how to run the mcp



Example to create a new XYZ server

# Create a new directory for our project
uv init XYZ
cd XYZ

# Create virtual environment and activate it
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx

# Create our server file
touch XYZ.py