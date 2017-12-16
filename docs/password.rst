Password module
===============

Hashing a password
------------------

::

    from libreauth.password import *

    password = b'my super secret password'
    hashed = password_hash(password)

Verifying a password against the hash
-------------------------------------

::

    from libreauth.password import *

    password = b'user submited password'
    hashed = ''
    if is_valid(password, hashed):
        // Successful authentication
        pass
    else:
        // Failed authentication
        pass
