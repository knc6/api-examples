# This module defines a set of common functions which are used in other examples.
import time
import datetime
import os
import importlib.util
import settings
import urllib
from IPython.display import display, JSON
import json


# GENERIC UTILITIES

def update_settings_with_users_authorization_info(ACCOUNT_ID='ACCOUNT_ID', 
                                                  AUTH_TOKEN='AUTH_TOKEN', 
                                                  MATERIALS_PROJECT_API_KEY='MATERIALS_PROJECT_API_KEY', 
                                                  ORGANIZATION_ID='ORGANIZATION_ID'):
    """
    This function updates settings.py with the users authorization info.
    It assumes 'settings.py' is located in the folder above this file's location.
    Ex) '../settings.py'

    Args:
        ACCOUNT_ID (str): Users' ACCOUNT_ID
        AUTH_TOKEN (str): Users' AUTH_TOKEN
        MATERIALS_PROJECT_API_KEY (str): Users' MATERIALS_PROJECT_API_KEY
        ORGANIZATION_ID (str): Users' ORGANIZATION_ID
        settings_filepath (str): Path to settings.py

    Returns:
        None
    """
    
    assert os.path.isfile('../settings.py')
    
    with open('../settings.py') as settings:
        settings_filelines = settings.readlines()
    with open('../settings.py', "w") as settings:
        for line in settings_filelines:
            if 'ACCOUNT_ID = ' in line:
                settings.write('%s "%s"\n' % ("ACCOUNT_ID =", ACCOUNT_ID))
            elif 'AUTH_TOKEN = ' in line:
                settings.write('%s "%s"\n' % ("AUTH_TOKEN =", AUTH_TOKEN))
            elif 'MATERIALS_PROJECT_API_KEY = ' in line:
                settings.write('%s "%s"\n' % ("MATERIALS_PROJECT_API_KEY =", MATERIALS_PROJECT_API_KEY))
            elif 'ORGANIZATION_ID = ' in line:
                settings.write('%s "%s"\n' % ("ORGANIZATION_ID =", ORGANIZATION_ID))
            else:
                settings.write(line)


def save_files(job_id, job_endpoint, filename_on_cloud, filename_on_disk):
    """
    Saves a file to disk, overwriting any files with the same name as filename_on_disk

    Args:
        job_id (str): ID of the job
        filename_on_cloud (str): Name of the file on the server
        filename_on_disk (str): Name the file will be saved to

    Returns:
        None
    """
    files = job_endpoint.list_files(job_id)
    for file in files:
        if file["name"] == filename_on_cloud:
            file_metadata = file

    # Get a download URL for the CONTCAR
    signed_url = file_metadata['signedUrl']

    # Download the contcar to memory
    server_response = urllib.request.urlopen(signed_url)

    # Write it to disk
    with open(filename_on_disk, "wb") as outp:
        outp.write(server_response.read())


# IMPORT UTILITIES

def install_package(name, version=None):
    """
    Installs a package via Pip. If a version is supplied, will attempt to install that specific version.
    If one is not supplied, requirements.txt will be searched to find a version.
    If a version is still not found, the latest version of the package will be installed.

    Args:
        name (str): the name of the module (e.g. pandas, numpy, etc)
        version (str): the specific version (if any) to import (e.g. 0.1.5, 1.0.0, etc).

    Returns:
        None
    """
    # Check requiements.txt for current version, if one wasn't supplied
    if version is None:
        reqs_file = os.path.realpath(os.path.join(__file__, "../../../requirements.txt"))
        with open(reqs_file, "r") as reqs:
            for line in reqs:
                if name in line:
                    version = line.strip().split("==")[1]

    # Add version if one was found or specified
    if version is not None:
        pip_name = f"{name}=={version}"
    else:
        pip_name = name

    # Install the modules
    import sys, subprocess
    subprocess.call([sys.executable, "-m", "pip", "install", pip_name])
    # Invalidate module cache based on import_lib doc recommendation:
    #   https://docs.python.org/3/library/importlib.html#importlib.invalidate_caches
    importlib.invalidate_caches()


def ensure_packages_are_installed(*names):
    """
    Ensures a package is installed on the system, by installing it if it does not exist currently.
    If nothing is passed as the argument, packages specified in requirements.txt are installed.

    Args:
        names (str): the names of the package to be checked (e.g. pandas, numpy, etc)

    Returns:
        None
    """
    # Install packages passed in to names
    if len(names) > 0:
        for name in names:
            if importlib.util.find_spec(name) is None:
                install_package(name)

    # Install requirements.txt if nothing was passed in
    else:
        reqs_file = os.path.realpath(os.path.join(__file__, "../../../requirements.txt"))
        with open(reqs_file, "r") as reqs:
            for line in reqs:
                # Ignore Jupyterlab, since the user is probably running it already to view the notebooks
                if "jupyterlab" in line:
                    pass
                # Check if packages exist, and install if they don't
                else:
                    name, version = line.strip().split("==")
                    if importlib.util.find_spec(name) is None:
                        install_package(name, version)


ensure_packages_are_installed("tabulate")

# Needs to go here, to ensure it's installed before we import
from tabulate import tabulate


# JOB UTILITIES

def get_jobs_statuses_by_ids(endpoint, job_ids):
    """
    Gets jobs statues by their IDs.

    Args:
        endpoint (endpoints.jobs.JobEndpoints): an instance of JobEndpoints class
        job_ids (list): list of job IDs to get the status for

    Returns:
        list: list of job statuses
    """
    jobs = endpoint.list({"_id": {"$in": job_ids}}, {"fields": {"status": 1}})
    return [job["status"] for job in jobs]


def wait_for_jobs_to_finish(endpoint, job_ids, poll_interval=10):
    """
    Waits for jobs to finish and prints their statuses.
    A job is considered finished if it is not in "pre-submission", "submitted", or, "active" status.

    Args:
        endpoint (endpoints.jobs.JobEndpoints): an instance of JobEndpoints class
        job_ids (list): list of job IDs to wait for
        poll_interval (int): poll interval for job information in seconds. Defaults to 10.
    """
    print("Wait for jobs to finish, poll interval: {0} sec".format(poll_interval))
    while True:
        statuses = get_jobs_statuses_by_ids(endpoint, job_ids)

        errored_jobs = len([status for status in statuses if status == "error"])
        active_jobs = len([status for status in statuses if status == "active"])
        finished_jobs = len([status for status in statuses if status == "finished"])
        submitted_jobs = len([status for status in statuses if status == "submitted"])

        headers = ["TIME", "SUBMITTED-JOBS", "ACTIVE-JOBS", "FINISHED-JOBS", "ERRORED-JOBS"]
        now = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        row = [now, submitted_jobs, active_jobs, finished_jobs, errored_jobs]
        print(tabulate([row], headers, tablefmt='grid', stralign='center'))

        if all([status not in ["pre-submission", "submitted", "active"] for status in statuses]):
            break
        time.sleep(poll_interval)


# WORKFLOW

def copy_bank_workflow_by_system_name(endpoint, system_name, account_id):
    """
    Copies a bank workflow with given ID into the account's workflows.

    Args:
        endpoint (endpoints.bank_workflows.BankWorkflowEndpoints): an instance of BankWorkflowEndpoints class
        system_name (str): workflow system name.
        account_id (str): ID of account to copy the bank workflow into.

    Returns:
        dict: new account's workflow
    """
    bank_workflow_id = endpoint.list({"systemName": system_name})[0]["_id"]
    return endpoint.copy(bank_workflow_id, account_id)["_id"]


# PROPERTY

def get_property_by_subworkow_and_unit_indicies(endpoint, property_name, job, subworkflow_index, unit_index):
    """
    Returns the property extracted in the given unit of the job's subworkflow.

    Args:
        endpoint (endpoints.raw_properties.RawPropertiesEndpoints): an instance of RawPropertiesEndpoints class.
        property_name (str): name of property to extract.
        job (dict): job config to extract the property from.
        subworkflow_index (int): index of subworkflow to extract the property from.
        unit_index (int): index of unit to extract the property from.

    Returns:
        dict: extracted property
    """
    unit_flowchart_id = job["workflow"]["subworkflows"][subworkflow_index]["units"][unit_index]["flowchartId"]
    return endpoint.get_property(job["_id"], unit_flowchart_id, property_name)


# DISPLAY UTILITIES

def dataframe_to_html(df, text_align="center"):
    """
    Converts Pandas dataframe to HTML.
    See https://pandas.pydata.org/pandas-docs/stable/style.html for more information about styling.

    Args:
        df (pd.dataFrame): Pandas dataframe.
        text_align (str): text align. Defaults to center.
    """
    styles = [
        dict(selector="th", props=[("text-align", text_align)]),
        dict(selector="td", props=[("text-align", text_align)])
    ]
    return (df.style.set_table_styles(styles))


def display_JSON(obj, interactive_viewer=settings.use_interactive_JSON_viewer):
    """
    Displays JSON, either interactively or via a text dump to Stdout
    Args:
        obj (dict): Object to display as nicely-formatted JSON
        interactive (bool): Whether to use the interactive viewer or not
    """
    if interactive_viewer:
        display(JSON(obj))
    else:
        print(json.dumps(obj, indent=4))
