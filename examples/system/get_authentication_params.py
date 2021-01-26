#!/usr/bin/env python
# coding: utf-8

# # Overview
# 
# This example shows how to log in to Exabyte RESTFul API via [Login](https://docs.exabyte.io/api/API/post_login) endpoint
# and generate API authentication parameters.

# # Execution
# 
# > <span style="color: orange">**NOTE**</span>: In order to run this example, an active Exabyte.io account is required.
# 
# ## Import packages

# In[]:


from IPython.display import JSON, display
import os
import sys
import json

# Import settings and utils file
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path: sys.path.append(module_path)
from settings import HOST, PORT, VERSION, SECURE
from utils import ensure_packages_are_installed

ensure_packages_are_installed()

from exabyte_api_client.endpoints.login import LoginEndpoint

# Set interactive_JSON to True if running this as a live notebook, to receive an interactive JSON viewer 
interactive_JSON = False

# ## Set Parameters
# 
# - **USERNAME**: Your Exabyte account username.
# 
# - **PASSWORD**: Your Exabyte account password.

# In[]:


USERNAME = "YOUR_USERNANE"
PASSWORD = "YOUR_PASSWORD"

# ## Initialize the endpoint

# In[]:


endpoint = LoginEndpoint(HOST, PORT, USERNAME, PASSWORD, VERSION, SECURE)
auth_params = endpoint.login()

# ## Print authentication parameters
# 
# Print the authentication parameters in pretty JSON below. Update [settings](../settings.py) with this parameters to be
# able to run other examples.

# In[]:


if interactive_JSON:
    display(JSON(auth_params))
else:
    print(json.dumps(auth_params, indent=4))
