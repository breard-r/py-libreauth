Python LibreAuth
================

Python bindings to the LibreAuth library.
LibreAuth is a collection of tools for user authentication written in Rust.

.. image:: https://api.travis-ci.org/breard-r/py-libreauth.png
    :target: https://travis-ci.org/breard-r/py-libreauth
    :alt: Build status

.. image:: https://readthedocs.org/projects/libreauth/badge/?version=latest
    :target: http://libreauth.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/status/libreauth.svg
    :target: https://pypi.python.org/pypi/libreauth
    :alt: Project status

.. image:: https://img.shields.io/pypi/v/libreauth.svg
    :target: https://pypi.python.org/pypi/libreauth
    :alt: Version

.. image:: https://img.shields.io/pypi/pyversions/libreauth.svg
    :target: https://pypi.python.org/pypi/libreauth
    :alt: Python versions

.. image:: https://img.shields.io/pypi/l/libreauth.svg
    :target: http://cecill.info/index.en.html
    :alt: CeCILL license


Features
--------

This is a work in progress. Some features may not be available.

* Password / passphrase authentication

  - ✓ no character-set limitation
  - ✓ reasonable lenth limit (`security vs. DOS <http://arstechnica.com/security/2013/09/long-passwords-are-good-but-too-much-length-can-be-bad-for-security/>`_)
  - ✓ strong, evolutive and retro-compatible password hashing functions
  - ✓ optional NIST Special Publication 800-63B compatibility

* HOTP - HMAC-based One-time Password Algorithm (`OATH <http://www.openauthentication.org/>`_ - `RFC 4226 <https://tools.ietf.org/html/rfc4226>`_)

  - ✗ the key can be passed as bytes, an ASCII string, an hexadicimal string or a base32 string
  - ✗ customizable counter
  - ✗ customizable hash function (sha1, sha256, sha512)
  - ✗ customizable output length
  - ✗ customizable output alphabet

* TOTP - Time-based One-time Password Algorithm (`OATH <http://www.openauthentication.org/>`_ - `RFC 6238 <https://tools.ietf.org/html/rfc6238>`_)

  - ✗ the key can be passed as bytes, an ASCII string, an hexadicimal string or a base32 string
  - ✗ customizable timestamp
  - ✗ customizable period
  - ✗ customizable initial time (T0)
  - ✗ customizable hash function (sha1, sha256, sha512)
  - ✗ customizable output length
  - ✗ customizable output alphabet
  - ✗ customizable positive and negative period tolerance
