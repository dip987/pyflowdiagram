=============
pyflowdiagram
=============


.. image:: https://img.shields.io/pypi/v/pyflowdiagram.svg
        :target: https://pypi.python.org/pypi/pyflowdiagram

.. image:: https://img.shields.io/travis/dip987/pyflowdiagram.svg
        :target: https://travis-ci.com/dip987/pyflowdiagram

.. image:: https://readthedocs.org/projects/pyflowdiagram/badge/?version=latest
        :target: https://pyflowdiagram.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Simple python library to draw colorful process flow diagrams


* Free software: MIT license
* Documentation: https://pyflowdiagram.readthedocs.io.


Features
--------

Creates a simple, linear color-coded process flow diagram using a list of labels.

Installation
------------
First clone this github repo
::
    git clone https://github.com/dip987/pyflowdiagram
Then run the setup
::
    python setup.py install

Examples
--------
Draw a diagram with 4 labels, where each block has a width of 3cm and a height of 1.5cm
::
    import matplotlib.pyplot as plt
    from pyflowdiagram import draw_process_flow
    labels = ["Flow1", "Flow2", "Cats", "Test", "Flow3\nLine2"]
    draw_process_flow(labels, 3.0, 1.5)
    plt.show()

.. image:: figures/example1.png
    :alt: Flow1
    :align: center

Additionally you can group different blocks with the similar colors and set the figure DPI. To group blocks, pass in a
*group_id* list containing a group number corresponding to each label.
::
    import matplotlib.pyplot as plt
    from pyflowdiagram import draw_process_flow
    labels = ["Flow1", "Flow2", "Cats", "Test", "Flow3\nLine2"]
    group_ids = [0, 0, 1, 1, 1]
    draw_process_flow(labels, 3.0, 1.5, group_ids=group_ids, dpi=100)
    plt.show()

.. image:: figures/example2.png
    :alt: Flow2
    :align: center


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
