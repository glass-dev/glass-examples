:orphan:


Examples for *GLASS*
====================

.. toctree::
   :hidden:

   Documentation <https://glass.readthedocs.io>

These examples show how `GLASS`__, the Generator for Large Scale Structure, can
be used in practice.  They are often a good starting point for more complicated
and realistic simulations.

__ https://glass.readthedocs.io

To run the examples yourself, you need to have GLASS installed.  To install the
specific version of GLASS for the examples you are reading:

.. parsed-literal::

    $ pip install |pip_package|

The examples currently require `CAMB`__ to produce angular matter power spectra
and for the cosmological background.  Make sure you have CAMB installed::

    $ python -c 'import camb'  # should not give an error

If you want to compute the angular matter power spectra in the examples, you
need the `glass-camb` package::

    $ pip install glass-camb

__ https://camb.readthedocs.io/



.. raw:: html

    <div class="sphx-glr-thumbnails">


.. raw:: html

    </div>

Basic examples
--------------
To get started, these examples focus on simulating one thing at a time.



.. raw:: html

    <div class="sphx-glr-thumbnails">


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example simulates a matter-only light cone up to redshift 1 and samples galaxies from a un...">

.. only:: html

  .. image:: /basic/images/thumb/sphx_glr_plot_density_thumb.png
    :alt:

  :ref:`sphx_glr_basic_plot_density.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Galaxy distribution</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example simulates only the matter field in nested shells up to redshift 1.">

.. only:: html

  .. image:: /basic/images/thumb/sphx_glr_matter_thumb.png
    :alt:

  :ref:`sphx_glr_basic_matter.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Matter distribution</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example demonstrates how matter shells are defined, and their angular power spectra comput...">

.. only:: html

  .. image:: /basic/images/thumb/sphx_glr_shells_thumb.png
    :alt:

  :ref:`sphx_glr_basic_shells.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Matter shell definition</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example simulates galaxies with a simple photometric redshift model.">

.. only:: html

  .. image:: /basic/images/thumb/sphx_glr_photoz_thumb.png
    :alt:

  :ref:`sphx_glr_basic_photoz.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Photometric redshifts</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example computes weak lensing maps (convergence and shear) for a redshift distribution of ...">

.. only:: html

  .. image:: /basic/images/thumb/sphx_glr_plot_lensing_thumb.png
    :alt:

  :ref:`sphx_glr_basic_plot_lensing.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Weak lensing</div>
    </div>


.. raw:: html

    </div>

Advanced examples
-----------------
More advanced examples, combining multiple interacting generators.



.. raw:: html

    <div class="sphx-glr-thumbnails">


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example simulates a galaxy catalogue with shears affected by weak lensing, combining the /...">

.. only:: html

  .. image:: /advanced/images/thumb/sphx_glr_plot_shears_thumb.png
    :alt:

  :ref:`sphx_glr_advanced_plot_shears.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Galaxy shear</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example simulates a galaxy catalogue from a Stage IV Space Satellite Galaxy Survey such as...">

.. only:: html

  .. image:: /advanced/images/thumb/sphx_glr_plot_s4_galaxies_thumb.png
    :alt:

  :ref:`sphx_glr_advanced_plot_s4_galaxies.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Stage IV Galaxy Survey</div>
    </div>


.. raw:: html

    </div>


.. toctree::
   :hidden:
   :includehidden:


   /./basic/index.rst
   /./advanced/index.rst

