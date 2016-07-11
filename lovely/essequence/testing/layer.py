import os

from crate.testing.layer import CrateLayer

here = os.path.dirname(__file__)
project_root = os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(
                            __file__
                        ))))
print project_root


crate_settings = os.path.join(here, 'crate.yaml')

crate_setup_dir = os.path.join(here, 'sql')
crash_path = os.path.join(project_root, 'bin', 'crash')
crate_cleanup = os.path.join(project_root, 'bin', 'crate_cleanup')
crate_setup = os.path.join(project_root, 'bin', 'crate_setup')

jinja_params = os.path.join(here, 'sqlparams.py')


def crate_path(*parts):
    return os.path.join(project_root, 'parts', 'crate', *parts)

# crate Layer
port = 18990

crate_layer = CrateLayer('crate',
                         crate_home=crate_path(),
                         crate_config=crate_settings,
                         crate_exec=crate_path('bin', 'crate'),
                         port=port)
crate_host = "127.0.0.1:%s" % port
crate_url = "http://%s" % crate_host
