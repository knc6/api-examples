# Exabyte RESTful API Examples

This repository contains the RESTful API examples in [Jupyter Notebook](http://jupyter.org/) format.

# Run Examples

1. Clone the repository.
    
    ```bash
    git clone git@github.com:Exabyte-io/exabyte-api-examples.git
    ```

2. Install python [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) if you do not have it.
    ```bash
    pip install virtualenv
    ```

3. Install required python packages.

    ```bash
    cd exabyte-api-examples
    virtualenv .env
    source .env/bin/activate
    pip install -r requirements.txt
    ```

4. Run Jupyter. This will open Jupyter notebook in your browser.

    ```bash
    cd examples
    jupyter notebook --config=config.py
    ```

5. Open [settings](examples/settings.ipynb) and adjust it as necessary.

6. Navigate to desired example, open, adjust and run it.


# Contribute

If you would like to add new examples or adjust existing ones, please consider the following points.

1. Put examples into proper directories.

2. Provide enough explanation in examples, close to the code as much as possible.

3. We use post-save hooks to automatically convert notebooks to python scripts. See [jupyter notebook config](config.py) for more information.
 
4. As it is difficult to review the notebooks on GitHub we [automatically](.gitattributes) add iPython notebooks to [Git LFS](https://git-lfs.github.com/).
