
Developer install
=================


To install a developer version of ipyannotations, you will first need to clone
the repository::

    git clone https://github.com/janfreyberg/ipyannotations
    cd ipyannotations

Next, install it with a develop install using pip::

    pip install -e '.[test,dev,examples,doc]'


If you are planning on working on the JS/frontend code, you should also do
a link installation of the extension.

If you are using Jupyterlab (recommended)::

    jupyter labextension develop .

If you are using the "classic" notebook, run (with the `appropriate flag`_)::

    jupyter nbextension install [--sys-prefix / --user / --system] --symlink --py ipyannotations

    jupyter nbextension enable [--sys-prefix / --user / --system] --py ipyannotations


Note that any changes to the python code will require a restart of the 

.. links

.. _`appropriate flag`: https://jupyter-notebook.readthedocs.io/en/stable/extending/frontend_extensions.html#installing-and-enabling-extensions
