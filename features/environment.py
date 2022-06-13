# ---------------------------------------------------------------------------
# Created By  : Guillermo Navarro
# Created Date: 13/06/2022
# version ='1.0'
# Comment: Definition of setup and cleanup methods
# ---------------------------------------------------------------------------

import os
from configparser import ConfigParser
from helper.helper_web import get_browser


def before_all(context):
    config = ConfigParser()
    print((os.path.join(os.getcwd(), 'setup.cfg')))
    my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_file)

    # Reading the browser type from the configuration file
    helper_func = get_browser(config.get('Environment', 'Browser'))
    context.helperfunc = helper_func


def after_scenario(context, scenario):
    context.helperfunc.delete_all_cookies()


def after_all(context):
    context.helperfunc.close()


