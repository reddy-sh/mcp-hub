from mcp.server.fastmcp import FastMCP
import os
import subprocess
import yaml

# Initialize FastMCP server
mcp = FastMCP("mcp-autopilot")

@mcp.tool()
def create_mcp_server(server_name: str) -> str:
    """Create a new MCP server by running the create-mcp-server.sh script.

    Args:
        server_name: Name of the MCP server to create.

    Returns:
        A message indicating success or failure.
    """
    script_path = "./_create-mcp-server.sh"
    try:
        result = subprocess.run(["bash", script_path, server_name], capture_output=True, text=True, check=True)
        # Update the YAML configuration after creating the server
        update_mcp_servers_config()
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@mcp.tool()
def list_mcp_servers() -> list:
    """Get the list of all MCP servers available in the mcp-servers directory.

    Returns:
        A list of server names.
    """
    servers_dir = "/mcp-servers"
    try:
        servers = [name for name in os.listdir(servers_dir) if os.path.isdir(os.path.join(servers_dir, name))]
        return servers
    except FileNotFoundError:
        return []

@mcp.tool()
def update_mcp_servers_config() -> str:
    """Create or update a YAML configuration file for all MCP servers.

    This function scans the `mcp-servers` directory and generates a YAML file
    containing the configuration of all MCP servers. The YAML file can be used
    to recreate the servers if needed.

    Returns:
        A message indicating success.
    """
    servers_dir = "./mcp-servers"
    config_file = "./mcp-servers-config.yaml"

    try:
        servers = [name for name in os.listdir(servers_dir) if os.path.isdir(os.path.join(servers_dir, name))]
        config_data = {"servers": servers}

        with open(config_file, "w") as yaml_file:
            yaml.dump(config_data, yaml_file, default_flow_style=False)

        return f"Configuration file '{config_file}' updated successfully."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")