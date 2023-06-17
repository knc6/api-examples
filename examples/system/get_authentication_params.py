#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/Exabyte-io/api-examples/blob/bugfix/SOF-5578-WIP/examples/system/get_authentication_params.ipynb" target="_parent">
# <img alt="Open in Google Colab" src="https://user-images.githubusercontent.com/20477508/128780728-491fea90-9b23-495f-a091-11681150db37.jpeg" width="150" border="0">
# </a>

# # Overview
# 
# This example shows how to log in to Exabyte RESTFul API via [Login](https://docs.mat3ra.com/api/API/post_login) endpoint and generate API authentication parameters.

# # Execution
# 
# > <span style="color: orange">**NOTE**</span>: In order to run this example, an active Exabyte.io account is required.

# ## Set Parameters
# 
# - **USERNAME**: Your Exabyte account username.
# 
# - **PASSWORD**: Your Exabyte account password.

# In[ ]:


#@title Authorization Form
USERNAME = "YOUR_USERNAME" #@param {type:"string"}
PASSWORD = "YOUR_PASSWORD" #@param {type:"string"}

import os
if "COLAB_JUPYTER_IP" in os.environ:
    get_ipython().system('GIT_BRANCH="bugfix/SOF-5578-WIP"; export GIT_BRANCH; curl -s "https://raw.githubusercontent.com/Exabyte-io/api-examples/${GIT_BRANCH}/scripts/env.sh" | bash')


# ## Import packages

# In[ ]:


from examples.settings import HOST, PORT, VERSION, SECURE
from examples.utils.generic import display_JSON

from exabyte_api_client.endpoints.login import LoginEndpoint


# ## Initialize the endpoint

# In[ ]:


endpoint = LoginEndpoint(HOST, PORT, USERNAME, PASSWORD, VERSION, SECURE)
auth_params = endpoint.login()


# ## Print authentication parameters
# 
# Print the authentication parameters in pretty JSON below. Update [settings](../settings.json) with this parameters to be able to run other examples.

# In[ ]:


display_JSON(auth_params)

