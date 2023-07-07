# Mat3ra API Examples

## Contents of this Repository

Below, we list the contents of this repository, in roughly the order that a user might want to go through it in order to learn how our API works.

| Folder            | Notebook                                | Description |
| ------------------|-----------------------------------------| ----------- |
| [Examples/System](examples/system/)     | [Get Authentication Params](examples/system/get_authentication_params.ipynb)               | Demonstrates how to programatically find your user ID and access token, which is to [authenticate](https://docs.mat3ra.com/rest-api/authentication/) for many portions of the Mat3ra API.
| [Examples/Workflow](examples/workflow/) | [Get Workflows](examples/workflow/get_workflows.ipynb)                           | Walks through how to [query](https://docs.mat3ra.com/rest-api/query-structure/) the Mat3ra API to programatically search for workflows. In this example, we search for workflows that calculate the total energy of a material.
| [Examples/Material](examples/material/) | [Get Materials by Formula](examples/material/get_materials_by_formula.ipynb)                | Shows how [queries](https://docs.mat3ra.com/rest-api/query-structure/) can be made to search for materials stored on your account by their formula. In this example, we search for a system containing Si.
| [Examples/Material](examples/material/) | [Create Material](examples/material/create_material.ipynb)                         | Gives an overview of how materials can be generated in [JSON format](https://docs.mat3ra.com/materials/data/) and uploaded to your user account. In this example, we create an FCC Si crystal and upload it.
| [Examples/Material](examples/material/) | [Import Materials from Materials Project](examples/material/import_materials_from_materialsproject.ipynb) | Demonstrates how materials can be imported from [Materials Project](https://materialsproject.org/about), if their Materials Project ID is known. In this example, we import monoclinic and hexagonal SiGe cells.
| [Examples/Material](examples/material/) | [Import Materials from Poscar](examples/material/import_materials_from_poscar.ipynb)            | Provides an example of how materials can be imported directly from Poscar files (a common chemical file format best-known [for its use in VASP](https://www.vasp.at/wiki/index.php/Input)). In this example, we import the unit cell of SiGe.
| [Examples/Material](examples/material/) | [Interoperability between Mat3ra and Materials Project](examples/material/api_interoperability_showcase.ipynb)            | In this notebook, we showcase a major advantage of APIs: interoperability. We begin by performing a query using the [Materials Project](https://materialsproject.org) API for all systems containing Iron and Oxygen. We then filter our results (for demonstraiton purposes, we keep only the first 10 materials found). Finally, we upload our results to the Mat3ra platform, where further calculations could be performed to characterize these materials.
| [Examples/Job](examples/job/)            | [Create and Submit Job](examples/job/create_and_submit_job.ipynb)                   | Shows how to use the Mat3ra API to [create jobs](https://docs.mat3ra.com/jobs/data/) and run them on our cluster. In this example, we run a DFT calculation to get the total energy of an FCC Si unit cell using Quantum Espresso.
| [Examples/Job](examples/job/)            | [Get File from Job](examples/job/get-file-from-job.ipynb) | Guides you through using the Mat3ra API to query for a list of files produced by a job, describes the metadata assigned to each file, and ends by demonstrating how to download any remote file generated by a job to the local disk.
| [Examples/Job](examples/job/)            | [Run Simulations and Extract Properties](examples/job/run-simulations-and-extract-properties.ipynb)  | Leads you through the process of copying a [bank workflow](https://docs.mat3ra.com/workflows/bank/) to your account and using it to automatically calculate the [properties](https://docs.mat3ra.com/properties/overview/) of multiple materials. In this example, we determine the [band gap](https://docs.mat3ra.com/properties-directory/non-scalar/band-gaps/) of Si and Ge.
| [Examples/Job](examples/job/)            | [ML - Train Model Predict Properties](examples/job/ml-train-model-predict-properties.ipynb)     | Walks you through automated dataset generation and the training/prediction of material properties using [machine learning](https://docs.mat3ra.com/software-directory/overview/#machine-learning). In this example, we calculate the band gaps of Si and SiGe, and using various materials properties as descriptors, train a model to predict their band gaps. Finally, we use this trained model to predict the band gap of Ge.



## Setup

NOTE: tested with Python version 3.8 and 3.10, please assert that the virtual environment is created with it. Use [`pyenv`](https://github.com/pyenv/pyenv#installation) to manage Python versions.

Follow the steps below in order to setup and view the Jupyter notebooks:

0. [Install git-lfs](https://help.github.com/articles/installing-git-large-file-storage/) [[3](#links)] in order to get access to the source code and notebook files.

1. Clone repository:

    ```bash
    git clone https://github.com/Exabyte-io/api-examples.git
    ```

    Or, if you have set up SSH keys

    ```bash
    git clone git@github.com:Exabyte-io/api-examples.git
    ```

    In case for some reason git-lfs was not installed at the time of cloning, the files can be pulled after installing git-lfs, through `git lfs pull`.

    Related to this, please be aware that as the `.ipynb` and `.poscar` files are stored on git-lfs, they are not part of the zip archive downloaded through GitHub's web interface.

3. Install [virtualenv](https://virtualenv.pypa.io/en/stable/) using [pip](https://pip.pypa.io/en/stable/) if not already present:

    ```bash
    pip install virtualenv
    ```

4. Create virtual environment and install required packages:

    ```bash
    cd api-examples
    virtualenv .env
    source .env/bin/activate
    pip install -e ."[localhost]"
    ```

5. Run Jupyter and open a notebook in a browser. In order for the post-save hook feature to work properly, one must launch their Jupyter Notebook environment in the folder that contains the file `config.py`, which is the `examples` folder shown below:

    ```bash
    cd examples
    jupyter lab --config=config.py
    ```

## Usage

In order to run or edit the examples:

1. Assert an existing Mat3ra.com account. Examples require an account to run. New users can register [here](https://platform.mat3ra.com/register) to obtain one.

2. Open [settings](utils/settings.json) and adjust it to provide the API authentication parameters. See the [corresponding example](examples/system/get_authentication_params.ipynb) to learn how to obtain the authentication parameters. It is also possible to generate an API token by logging in to [Mat3ra platform](https://platform.mat3ra.com/), navigating to the Account Preferences, and clicking the 'Generate new token' button under API Tokens. More details can be found [here](https://docs.mat3ra.com/accounts/ui/preferences/api/).

3. Open the desired example notebook, adjust it as necessary and run. One can speed up the notebooks execution after running the [Get Authentication Params](examples/system/get_authentication_params.ipynb) one by reusing the kernel from the first notebook.

  <img src="images/reusable-kernel.png" width="250px" />

NOTE: The Materials Project API key should be obtained from [https://legacy.materialsproject.org/open](https://legacy.materialsproject.org/open).


## Contribute

This is an open-source repository and we welcome contributions for other use cases. The original set of examples is only meant to demonstrate the capabilities and can be extended.

We suggest forking this repository and introducing the adjustments there. The changes in the fork can further be considered for merging into this repository as it is commonly used on Github. This process is explained in more details elsewhere online [[4](#links)].

If you would like to add new examples or adjust existing ones, please consider the following:

1. Put examples into the corresponding directories by domain.

2. Walk the readers through the examples by providing step-by-step explanation similar to [this](examples/material/get_materials_by_formula.ipynb).

3. We use post-save hooks to automatically convert notebooks to python scripts. See [config](examples/config.py) file for more information. In order to facilitate code review, we exclude notebook sources from version control and store them in Git LFS [[3](#links)]. Please follow this convention.

## Links

1. Mat3ra.com RESTful API, description in the online documentation: [link](https://docs.mat3ra.com/rest-api/overview/)
2. Jupyter.org, official website: [link](https://jupyter.org/)
3. Git Large File Storage, official website: [link](https://git-lfs.github.com/)
4. GitHub Standard Fork & Pull Request Workflow, online explanation: [link](https://gist.github.com/Chaser324/ce0505fbed06b947d962)
