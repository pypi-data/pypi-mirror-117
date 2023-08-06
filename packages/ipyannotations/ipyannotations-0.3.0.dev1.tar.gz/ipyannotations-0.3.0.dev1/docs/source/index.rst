
ipyannotations
=====================================

Version: |release|

Create rich adata annotations in jupyter notebooks.


Quickstart
----------

To get started with ipyannotations, install with pip::

    pip install ipyannotations

To start labelling data, import from the appropriate ipyannotations module. For
example, for text span/entity labelling:

.. code-block:: python

   from ipyannotations import text
   widget = text.TextTagger()
   widget.display("This is a text tagging widget. Highlight words "
                  "or phrases to tag them with a class.")
   widget

.. jupyter-execute::
   :hide-code:

   from ipyannotations import text
   widget = text.TextTagger()
   widget.display("This is a text tagging widget. Highlight words "
                  "or phrases to tag them with a class.")
   from ipyannotations._doc_utils import recursively_remove_from_dom
   widget = recursively_remove_from_dom(widget)
   widget


Or, if you would like to classify images:

.. code-block:: python

   from ipyannotations import images
   widget = images.ClassLabeller(options=["monkey", "ape"])
   widget.display("img/baboon.png")
   widget

.. jupyter-execute::
   :hide-code:

   from ipyannotations import images
   widget = images.ClassLabeller(options=["monkey", "ape"])
   widget.display("source/img/baboon.png")
   from ipyannotations._doc_utils import recursively_remove_from_dom
   widget = recursively_remove_from_dom(widget)
   widget

|br|

.. note::

   Throughout this documentation, UI elements can be interacted with (e.g.
   buttons can be clicked, sliders can be moved), but because there is no
   python process running in the background, the effect will mostly not be
   visible.


.. toctree::
   :maxdepth: 2
   :caption: Contents

   installing
   introduction
   examples/index


.. toctree::
   :maxdepth: 2
   :caption: Development

   develop-install


.. links

.. _`Jupyter widgets`: https://jupyter.org/widgets.html

.. _`notebook`: https://jupyter-notebook.readthedocs.io/en/latest/


.. |br| raw:: html

      <br>
