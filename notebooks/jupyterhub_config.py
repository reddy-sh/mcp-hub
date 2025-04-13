# Configuration file for JupyterHub

import os
import sys
from oauthenticator.github import GitHubOAuthenticator

c = get_config()  # noqa

# Basic JupyterHub configuration
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.JupyterHub.hub_ip = '0.0.0.0'

# Use a secure cookie secret
c.JupyterHub.cookie_secret_file = './srv/jupyterhub/jupyterhub_cookie_secret'

# Set the log level
c.JupyterHub.log_level = 'INFO'

# Persist hub data
c.JupyterHub.db_url = './srv/jupyterhub/jupyterhub.sqlite'

# Use a local authenticator
c.JupyterHub.authenticator_class = 'jupyterhub.auth.LocalAuthenticator'

# Create sample users 
c.LocalAuthenticator.create_system_users = True

# Sample user configuration
c.Authenticator.admin_users = {'admin'}
c.Authenticator.allowed_users = {'sampleuser', 'admin'}

c.Authenticator.password = 'samplepassword'  # Set a password for the sample user

# In production, use a more secure method for password management
from jupyterhub.auth import LocalAuthenticator
from passlib.hash import bcrypt
c.LocalAuthenticator.check_common_password = True

# Default server options
c.Spawner.default_url = '/lab'  # Use JupyterLab by default
c.Spawner.mem_limit = '1G'  # Memory limit per user
c.Spawner.cpu_limit = 1.0   # CPU limit per user

# Configure single-user servers using the default local process spawner
# Use the built-in LocalProcessSpawner instead of DockerSpawner
c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'

# Specify the Python environment for the single-user servers
c.Spawner.environment = {
    'JUPYTER_ENABLE_LAB': 'yes',  # Enable JupyterLab
}

# For development, allow any origin for api requests
c.JupyterHub.tornado_settings = {
    'headers': {
        'Access-Control-Allow-Origin': '*',
    },
}

# Add configuration for HTTPS (recommended for production)
# c.JupyterHub.ssl_key = '/path/to/ssl.key'
# c.JupyterHub.ssl_cert = '/path/to/ssl.cert'

# Custom template directory
# c.JupyterHub.template_paths = ['/custom/templates']

# Customize the shutdown button
c.JupyterHub.shutdown_on_logout = False

# Define a custom logo
# c.JupyterHub.logo_file = '/custom/logo.png'

print("JupyterHub configuration loaded")
