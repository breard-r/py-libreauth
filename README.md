# Python LibreAuth

Python bindings to the LibreAuth library.
LibreAuth is a collection of tools for user authentication written in Rust.


## Features

:warning: This is a work in progress. Some features may not be available.

- Password / passphrase authentication
  - [ ] no character-set limitation
  - [ ] reasonable lenth limit ([security vs. DOS](http://arstechnica.com/security/2013/09/long-passwords-are-good-but-too-much-length-can-be-bad-for-security/))
  - [ ] strong, evolutive and retro-compatible password hashing functions
  - [ ] optional NIST Special Publication 800-63B compatibility
- HOTP - HMAC-based One-time Password Algorithm ([OATH](http://www.openauthentication.org/) - [RFC 4226](https://tools.ietf.org/html/rfc4226))
  - [ ] the key can be passed as bytes, an ASCII string, an hexadicimal string or a base32 string
  - [ ] customizable counter
  - [ ] customizable hash function (sha1, sha256, sha512)
  - [ ] customizable output length
  - [ ] customizable output alphabet
- TOTP - Time-based One-time Password Algorithm ([OATH](http://www.openauthentication.org/) - [RFC 6238](https://tools.ietf.org/html/rfc6238))
  - [ ] the key can be passed as bytes, an ASCII string, an hexadicimal string or a base32 string
  - [ ] customizable timestamp
  - [ ] customizable period
  - [ ] customizable initial time (T0)
  - [ ] customizable hash function (sha1, sha256, sha512)
  - [ ] customizable output length
  - [ ] customizable output alphabet
  - [ ] customizable positive and negative period tolerance
- ~~U2F - Universal 2nd Factor~~ ([FIDO Alliance](https://fidoalliance.org/specifications/download/)) :warning: Not started
  - [ ] virtual device API
  - [ ] client API
  - [ ] server API
