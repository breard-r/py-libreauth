# Copyright Rodolphe Breard (2017)
# Author: Rodolphe Breard (2017)
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

from ctypes import *
from . import lib

PASSWORD_MIN_LEN = 8
PASSWORD_MAX_LEN = 128
PASSWORD_STORAGE_LEN = 1024

NOSTANDARD = 0
NIST80063B = 1


class LibreAuthPassError(Exception):
    """Exception raised for errors in the password authentication module.

    Attributes:
        code -- error code
        message -- explanation of the error
    """

    def __init__(self, code):
        valid_codes = {
            0: 'success',
            1: 'password is too short',
            2: 'password is too long',
            10: 'invalid password format',
            20: 'not enough space',
        }
        self.code = code
        if code in valid_codes:
            self.message = valid_codes[code]
        else:
            self.message = 'unknown error'

def password_hash(password):
    return password_hash_standard(password, NOSTANDARD)

def password_hash_standard(password, standard):
    pass_len = len(password)
    if pass_len < PASSWORD_MIN_LEN:
        raise LibreAuthPassError(1)
    if pass_len > PASSWORD_MAX_LEN:
        raise LibreAuthPassError(2)
    buff = create_string_buffer(b'\000' * PASSWORD_STORAGE_LEN)
    c_pass = create_string_buffer(password)
    err = lib.libreauth_password_hash(c_pass, buff, PASSWORD_STORAGE_LEN, standard)
    if err != 0:
        raise LibreAuthPassError(err)
    return str(buff.value, encoding="utf-8")

def is_valid(password, reference):
    c_pass = create_string_buffer(password)
    c_ref = create_string_buffer(bytes(reference, encoding='utf-8'))
    return bool(lib.libreauth_password_is_valid(c_pass, c_ref))
