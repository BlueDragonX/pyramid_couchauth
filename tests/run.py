# Copyright (c) 2011, Ryan Bourgeois <bluedragonx@gmail.com>
# All rights reserved.
#
# This software is licensed under a modified BSD license as defined in the
# provided license file at the root of this project.  You may modify and/or
# distribute in accordance with those terms.
#
# This software is provided "as is" and any express or implied warranties,
# including, but not limited to, the implied warranties of merchantability and
# fitness for a particular purpose are disclaimed.

import unittest
import pyramid_couchauth.tests.test_principal
import pyramid_couchauth.tests.test_identification

def runtests():
    suites = unittest.TestSuite()
    suites.addTest(pyramid_couchauth.tests.test_principal.suite())
    suites.addTest(pyramid_couchauth.tests.test_identification.suite())
    return suites
