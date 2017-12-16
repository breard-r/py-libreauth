Install
=======

In order to work, you need to install LibreAuth 0.6 or higher.


Installing Rust with rustup
---------------------------

LibreAuth is developed in Rust. If you do not already have the latest stable version of the Rust compiler, you can install it with rustup.

.. code-block:: console

    curl https://sh.rustup.rs -sSf | sh
    rustc --version
    cargo --version


Building LibreAuth
------------------

Now that we have the Rust compiler, let's download and install LibreAuth.

.. code-block:: console

    wget 'https://github.com/breard-r/libreauth/archive/v0.6.0.tar.gz' -O '/tmp/libreauth.tar.gz'
    tar -xvf '/tmp/libreauth.tar.gz'
    cd 'libreauth-0.6.0'
    make
    sudo make install

It is not mandatory to install it system-wide. You can also copy the file ``target/release/liblibreauth.so`` anywhere and specify its path using the ``LIBREAUTH_LIB_PATH`` environment variable.
