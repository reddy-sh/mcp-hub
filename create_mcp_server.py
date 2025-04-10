import os
import argparse
import subprocess
from pathlib import Path
import json
from typing import Any, Dict

class MCPServerTemplate:
    def __init__(self, project_name: str, output_dir: str = "mcp-servers"):
        self.project_name = project_name
        self.output_dir = output_dir
        self.project_path = Path(output_dir) / project_name

    def create_directory_structure(self):
        """Create the basic directory structure for the MCP server."""
        os.makedirs(self.project_path, exist_ok=True)
        os.makedirs(self.project_path / "prompts", exist_ok=True)
        os.makedirs(self.project_path / "resources", exist_ok=True)
        print(f"Created project directory structure in: {self.project_path}")

    def create_pyproject_toml(self):
        """Create pyproject.toml with basic dependencies."""
        content = f'''[project]
name = "{self.project_name}"
version = "0.1.0"
description = "MCP server for {self.project_name}"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "httpx>=0.28.1",
    "mcp[cli]>=1.6.0",
    "Pillow>=10.2.0",  # For image processing
]
'''
        with open(self.project_path / "pyproject.toml", "w") as f:
            f.write(content)

    def create_sample_prompts(self):
        """Create sample prompt files to demonstrate prompt engineering."""
        system_prompt = f'''You are a specialized assistant for the {self.project_name} MCP server.

Follow these guidelines:
1. Be concise and direct in your responses
2. Use the available tools and resources effectively:
   - server_info: Access server configuration and settings
   - sample_image: Work with sample images when needed
3. Tools support context-aware operations:
   - Use ctx.get_resource() to access server resources
   - Handle image processing with proper error handling
4. Validate inputs before processing
5. Provide clear error messages when needed

Remember to:
- Stay focused on server capabilities
- Use proper error handling with try/except blocks
- Access server configuration through resources
- Handle image operations safely
- Follow type hints and documentation'''

        user_prompt = '''Example user request:
I need help with [specific task]...

Expected response format:
1. Acknowledge the request
2. Use appropriate tools
3. Provide clear results'''

        # Create prompts directory and sample files
        with open(self.project_path / "prompts" / "system_prompt.txt", "w") as f:
            f.write(system_prompt)
        
        with open(self.project_path / "prompts" / "user_prompt_example.txt", "w") as f:
            f.write(user_prompt)

        # Create a README for prompts
        prompts_readme = '''# Prompts Directory

This directory contains prompt templates and examples for the MCP server:

- `system_prompt.txt`: Main system prompt that defines assistant behavior
- `user_prompt_example.txt`: Example user prompts and expected response formats

## Best Practices
1. Keep prompts clear and specific
2. Include input validation requirements
3. Define expected output formats
4. Update prompts based on user feedback'''

        with open(self.project_path / "prompts" / "README.md", "w") as f:
            f.write(prompts_readme)

    def create_sample_resources(self):
        """Create sample resource files and documentation."""
        # Create a sample config file
        config = f'''{{
    "server_name": "{self.project_name}",
    "version": "0.1.0",
    "settings": {{
        "max_retries": 3,
        "timeout": 30,
        "debug_mode": false
    }},
    "api_endpoints": {{
        "example": "https://api.example.com/v1"
    }}
}}'''
        
        with open(self.project_path / "resources" / "config.json", "w") as f:
            f.write(config)

        # Create resources README
        resources_readme = '''# Resources Directory

This directory contains configuration and resource files:

- `config.json`: Server configuration settings
- Add other resource files as needed (e.g., templates, schemas, data files)

## Resource Management
1. Keep sensitive data in .env files (not in config.json)
2. Document all configuration options
3. Use appropriate file formats (JSON, YAML, etc.)
4. Version control non-sensitive resources'''

        with open(self.project_path / "resources" / "README.md", "w") as f:
            f.write(resources_readme)

    def create_main_server_file(self):
        """Create the main MCP server file with sample tools."""
        content = f'''from typing import Any, Dict, Optional
import json
from pathlib import Path
from PIL import Image as PILImage
from mcp.server.fastmcp import FastMCP, Image, Context, Resource

# Initialize FastMCP server
mcp = FastMCP("{self.project_name}")

# Load configuration
def load_config() -> Dict[str, Any]:
    """Load server configuration from resources."""
    config_path = Path(__file__).parent / "resources" / "config.json"
    try:
        with open(config_path) as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading config: {{e}}")
        return {{"server_name": "{self.project_name}", "version": "0.1.0"}}

# Initialize configuration
CONFIG = load_config()

# Define resources
@mcp.resource("server_info")
async def get_server_info_resource() -> Resource[Dict[str, Any]]:
    """Server information resource.
    
    Returns:
        A resource containing server information
    """
    return Resource(
        data={{
            "name": CONFIG["server_name"],
            "version": CONFIG["version"],
            "settings": CONFIG.get("settings", {{}})
        }},
        description="Current server configuration and settings"
    )

@mcp.resource("sample_image")
async def get_sample_image() -> Resource[Image]:
    """Sample image resource.
    
    Returns:
        A resource containing a sample image
    """
    # Example using a placeholder image path
    image_path = Path(__file__).parent / "resources" / "sample.png"
    if not image_path.exists():
        return Resource(
            data=None,
            description="Sample image not found"
        )
    
    return Resource(
        data=Image(image_path),
        description="A sample image for demonstration"
    )

# Define tools
@mcp.tool()
async def hello_world(ctx: Context) -> str:
    """A simple hello world tool with context.
    
    Args:
        ctx: The tool execution context
    
    Returns:
        A greeting message including the server name and version.
    """
    server_info = await ctx.get_resource("server_info")
    return f"Hello from {{server_info['name']}} v{{server_info['version']}}!"

@mcp.tool()
async def echo(message: str) -> str:
    """Echo back the input message.
    
    Args:
        message: The message to echo back
        
    Returns:
        The echoed message with a prefix
    """
    return f"Echo: {{message}}"

@mcp.tool()
async def create_thumbnail(
    image_path: str, 
    max_size: tuple[int, int] = (100, 100)
) -> Optional[Image]:
    """Create a thumbnail from an image.
    
    Args:
        image_path: Path to the input image
        max_size: Maximum dimensions for the thumbnail (width, height)
        
    Returns:
        A thumbnail image, or None if the operation fails
    """
    try:
        img = PILImage.open(image_path)
        img.thumbnail(max_size)
        return Image(img)
    except Exception as e:
        print(f"Error creating thumbnail: {{e}}")
        return None

@mcp.tool()
async def get_server_settings(ctx: Context) -> Dict[str, Any]:
    """Get server settings using context and resources.
    
    Args:
        ctx: The tool execution context
        
    Returns:
        The server settings dictionary
    """
    server_info = await ctx.get_resource("server_info")
    return server_info.get("settings", {{}})

# Add more tools here...

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
'''
        with open(self.project_path / f"{self.project_name}.py", "w") as f:
            f.write(content)

    def create_readme(self):
        """Create README.md with setup instructions."""
        content = f'''# {self.project_name.title()} MCP Server

## Project Structure
```
{self.project_name}/
├── prompts/             # Prompt templates and examples
│   ├── system_prompt.txt
│   └── user_prompt_example.txt
├── resources/           # Configuration and resource files
│   └── config.json
├── {self.project_name}.py    # Main server implementation
├── README.md           # This file
└── pyproject.toml      # Project dependencies
```

## Setup
1. Ensure you have Python 3.13+ installed
2. Install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate
   uv sync
   ```

## Running the Server
```bash
uv run {self.project_name}.py
```

## Available Tools
- `hello_world`: A greeting that includes server info
- `echo`: Echoes back the input message
- `create_thumbnail`: Creates a thumbnail from an image
- `get_server_settings`: Returns server settings using context and resources

## Development Guide

### Adding New Tools
Add new tools by creating async functions decorated with `@mcp.tool()` in `{self.project_name}.py`:

```python
@mcp.tool()
async def your_tool(param1: str, param2: int) -> str:
    """Tool description.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
    """
    return f"Result: {{param1}} {{param2}}"
```

### Prompt Engineering
Check the `prompts/` directory for:
- System prompt templates
- Example user prompts
- Best practices

### Resource Management
The `resources/` directory contains:
- Server configuration
- Additional resources needed by your tools
- Documentation for resource usage
'''
        with open(self.project_path / "README.md", "w") as f:
            f.write(content)

    def create_gitignore(self):
        """Create .gitignore file."""
        content = '''.env
.venv
__pycache__/
*.py[cod]
'''
        with open(self.project_path / ".gitignore", "w") as f:
            f.write(content)

    def setup_python_environment(self):
        """Set up Python environment using uv."""
        try:
            subprocess.run(["uv", "venv"], cwd=self.project_path, check=True)
            print("Created virtual environment")
            subprocess.run(["uv", "sync"], cwd=self.project_path, check=True)
            print("Installed dependencies")
        except subprocess.CalledProcessError as e:
            print(f"Error setting up Python environment: {e}")
        except FileNotFoundError:
            print("Error: 'uv' command not found. Please install uv first.")

    def create_server(self):
        """Create the complete MCP server template."""
        print(f"Creating new MCP server: {self.project_name}")
        self.create_directory_structure()
        self.create_pyproject_toml()
        self.create_main_server_file()
        self.create_sample_prompts()
        self.create_sample_resources()
        self.create_readme()
        self.create_gitignore()
        self.setup_python_environment()
        print(f"\nMCP server template created successfully at {self.project_path}")
        print("\nNext steps:")
        print(f"1. cd {self.project_path}")
        print("2. source .venv/bin/activate")
        print(f"3. uv run {self.project_name}.py")
        print("\nExplore the prompts/ and resources/ directories for examples and templates.")

def main():
    parser = argparse.ArgumentParser(description="Create a new MCP server template")
    parser.add_argument("project_name", help="Name of the MCP server project")
    parser.add_argument("--output-dir", default="mcp-servers",
                      help="Output directory for the MCP server (default: mcp-servers)")
    args = parser.parse_args()

    template = MCPServerTemplate(args.project_name, args.output_dir)
    template.create_server()

if __name__ == "__main__":
    main()