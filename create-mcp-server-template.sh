# A script for creating a new MCP server template
#!/bin/bash

# Read the MCP server name from the user
read -p "Enter the MCP server name: " mcp_server_name

# Check if the MCP server name is empty
if [ -z "$mcp_server_name" ]; then
    echo "Error: MCP server name cannot be empty."
    exit 1
fi

# Create the MCP server template directory
mcp_server_dir="mcp-servers/$mcp_server_name"
if [ -d "$mcp_server_dir" ]; then
    echo "Error: MCP server directory '$mcp_server_dir' already exists. Please choose a different name."
    exit 1
fi

# Initialize the MCP server directory using uv
uv init "$mcp_server_dir"
if [ $? -ne 0 ]; then
    echo "Error: Failed to create MCP server template directory '$mcp_server_dir'."
    exit 1
fi

echo "Success: MCP server template directory '$mcp_server_dir' created successfully."

# Navigate to the new directory
cd "$mcp_server_dir" || {
    echo "Error: Failed to navigate to directory '$mcp_server_dir'."
    exit 1
}

# Set up a virtual environment
uv venv
if [ $? -ne 0 ]; then
    echo "Error: Failed to set up virtual environment."
    exit 1
fi

# Activate the virtual environment
source .venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate virtual environment."
    exit 1
fi

# Add required dependencies
uv add "mcp[cli]" httpx
if [ $? -ne 0 ]; then
    echo "Error: Failed to add dependencies."
    exit 1
fi

# Create the main server file
touch "$mcp_server_name.py"
if [ $? -ne 0 ]; then
    echo "Error: Failed to create the server file '$mcp_server_name.py'."
    exit 1
fi

echo "Success: MCP server '$mcp_server_name' setup completed. Happy coding!. If you love the repo, consider contributing or following us!"

