# handling misc func which are not relevant to
# functioning of this program
import json
import os

with open(os.path.join(os.path.dirname(__file__), "version.json"), "r") as f:
    VERSION = json.loads(f.read())


def greet(version=VERSION):
    return f"""
        #####################################################
        ##             Nginx QuickDeploy                   ##
        ##                v{version["version"]}                           ##
        ## https://github.com/regmibijay/nginx-quickdeploy ##
        ##                                                 ##
        #####################################################


        """


def adios(version=VERSION, message="             script ended successfully           "):
    #                   Bye                           ##
    #             Script ended abnormally             ##
    #             script ended successfully           ##
    return f"""
        #####################################################
        ##             Nginx QuickDeploy                   ##
        ##{message}##
        ##                v{version["version"]}                           ##
        ## https://github.com/regmibijay/nginx-quickdeploy ##
        ##                                                 ##
        #####################################################
    """
