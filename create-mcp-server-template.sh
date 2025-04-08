# A script for creating a new MCP server template
#!/bin/bash

# Check if project name is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <project_name>"
  exit 1
fi

PROJECT_NAME=$1

# Step 1: Create a New Project Directory
uv init "$PROJECT_NAME"
cd "$PROJECT_NAME" || exit

# Step 2: Set Up a Virtual Environment
uv venv
source .venv/bin/activate

# Step 3: Install Dependencies
uv add "mcp[cli]" httpx

# Step 4: Create the Server File
touch "$PROJECT_NAME.py"

# Output instructions for running the server
echo "\n### How to Run the MCP Server\nTo run the server, use the following command:\nuv run $PROJECT_NAME.py"

