# Copyright Rodolphe Breard (2017-2018)
# Author: Rodolphe Breard (2017-2018)
#
# This software is a computer library whose purpose is to offer a
# collection of tools for user authentication.
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

from libreauth.password import *
import unittest


class PasswordTestCase(unittest.TestCase):
    def test_hash(self):
        p = b'my super password'
        h = password_hash(p)
        self.assertTrue(h.startswith('$'))
        self.assertEqual(len(h.split('$')), 5)

    def test_valid(self):
        p = b'my super password'
        h = password_hash(p)
        self.assertTrue(is_valid(p, h))

    def test_invalid(self):
        p = b'bad password'
        h = '$argon2$len=32,passes=3,lanes=4,mem=12$AM4ncnAXFeC9HVVEFhOLeg$' \
            'PShZis96oh5lL6AQyjOZMS+nvF4b+B/4Rs7+Pncvub0'
        self.assertFalse(is_valid(p, h))

    def test_std(self):
        p = b'my super password'
        for std in (NOSTANDARD, NIST80063B, ):
            h = password_hash(p, standard=std)
            self.assertTrue(h.startswith('$'))
            self.assertEqual(len(h.split('$')), 5)
            self.assertTrue(is_valid(p, h))
            self.assertFalse(is_valid(b'bad password', h))

    def test_pass_too_short(self):
        for p in (b'', b'a', b'1234567'):
            with self.assertRaises(LibreAuthPassError) as cm:
                password_hash(p)
            e = cm.exception
            self.assertEqual(e.code, 1)

    def test_pass_too_long(self):
        for p in (b'a' * 129, b'1' * 256):
            with self.assertRaises(LibreAuthPassError) as cm:
                password_hash(p)
            e = cm.exception
            self.assertEqual(e.code, 2)

    def test_invalid_format(self):
        p = b'my super password'
        refs = (
            '',
            'plop',
            '$argon3$len=32,passes=3,lanes=4,mem=12$AM4ncnAXFeC9HVVEFhOLeg$' \
            'PShZis96oh5lL6AQyjOZMS+nvF4b+B/4Rs7+Pncvub0',
            '$argon2$len=32,passes=3;lanes=4,mem=12$AM4ncnAXFeC9HVVEFhOLeg$' \
            'PShZis96oh5lL6AQyjOZMS+nvF4b+B/4Rs7+Pncvub0',
        )
        for h in refs:
            self.assertFalse(is_valid(p, h))
