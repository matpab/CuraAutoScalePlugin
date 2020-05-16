# Copyright (c) 2020 Matthias Pabel
# The AutoScalePlugin is released under the terms of the AGPLv3 or higher.

from UM.i18n import i18nCatalog

i18n_catalog = i18nCatalog("AutoScalePlugin")

from . import AutoScalePlugin


def getMetaData():
    return {}


def register(app):
    return {"extension": AutoScalePlugin.AutoScalePlugin()}
