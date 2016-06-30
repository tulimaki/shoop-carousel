Shuup Carousel
==============

This package implements carousels
for the `Shuup <https://shuup.io/>`_ platform.

Copyright
---------

Copyright (C) 2012-2015 by Shuup Ltd. <contact@shuup.io>

Shuup is International Registered Trademark & Property of Shuup Ltd.,
Business ID: FI24815722, Business Address: Aurakatu 12 B, 20100 Turku,
Finland.

License
-------

Shuup Carousel is published under the GNU Affero General Public License,
version 3 (AGPLv3). See the LICENSE file.

Running tests
-------------

You can run tests with `py.test <http://pytest.org/>`_.

Requirements for running tests:

* Your virtualenv needs to have Shuup installed.

* Project root must be in the Python path.  This can be done with:

  .. code:: sh

     pip install -e .

* The packages from ``testing_requirements.txt`` must be installed.

  .. code:: sh

     pip install -r testing_requirements.txt

To run tests, use command:

.. code:: sh

   py.test -v shuup_carousel_tests

Vendor plugins
-------------

Shuup Carousel uses the `Owl Carousel 2 <http://www.owlcarousel.owlgraphic.com/>`_
jQuery slider plugin, which has been included in the ``js/vendor`` directory.
