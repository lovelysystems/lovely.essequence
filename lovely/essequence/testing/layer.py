import os

from crate.testing.layer import CrateLayer

here = os.path.dirname(__file__)
project_root = os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(
                            __file__
                        ))))
crate_settings = os.path.join(here, 'crate.yml')

crate_setup_dir = os.path.join(here, 'sql')
crash_path = os.path.join(project_root, 'bin', 'crash')
crate_cleanup = os.path.join(project_root, 'bin', 'crate_cleanup')
crate_setup = os.path.join(project_root, 'bin', 'crate_setup')
crate_home = os.path.join(project_root, 'parts', 'crate')

# crate Layer
host = '127.0.0.1'
port = 18990

crate_layer = CrateLayer('crate',
                         crate_home=crate_home,
                         crate_config=crate_settings,
                         host=host,
                         port=port,
                         verbose=True)
crate_host = host + ":" + str(port)
crate_url = "http://%s" % crate_host
