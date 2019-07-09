#######################################################
# 
# __main__.py
# Python implementation of the Class __main__
# Created on:      23-jun.-2019 6:56:24
# Original author: Betacode
# 
#######################################################
from controllers.BetahomeCoreController import (
    BetahomeCoreController
)
from view.view import View
from view.ui.windows.login import login
from models.models import Model

def main():
    core = BetahomeCoreController(
        View(),
        Model()
    )
    core.open()
    login(sys, core)

if __name__ == "__main__":
    import sys
    main()
