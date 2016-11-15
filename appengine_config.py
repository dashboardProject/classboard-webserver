"""`appengine_config` gets loaded when starting a new application instance."""
import sys
import os.path
# add `lib` subdirectory to `sys.path`, so our `main` module can load
# third-party libraries.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

# The secret key is used by Flask to encrypt session cookies.
# [START secret_key]
SECRET_KEY = 'secret'
# [END secret_key]