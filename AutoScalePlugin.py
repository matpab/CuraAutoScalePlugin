# Copyright (c) 2020 Matthias Pabel
# The AutoScalePlugin is released under the terms of the AGPLv3 or higher.

import os

from UM.PluginRegistry import PluginRegistry
from UM.Extension import Extension
from UM.Math.Vector import Vector
from UM.Application import Application
from UM.Scene.Iterator.BreadthFirstIterator import BreadthFirstIterator
from UM.Message import Message

from UM.i18n import i18nCatalog
i18n_catalog = i18nCatalog("AutoScalePlugin")


class AutoScalePlugin(Extension):
    def __init__(self):
        super().__init__()
        self._settings_view = None

        Application.getInstance().getPreferences().addPreference("AutoScalePlugin/x_scale", 0.0)
        self._x_scale = Application.getInstance().getPreferences().getValue("AutoScalePlugin/x_scale")  # type: float
        Application.getInstance().getPreferences().addPreference("AutoScalePlugin/y_scale", 0.0)
        self._y_scale = Application.getInstance().getPreferences().getValue("AutoScalePlugin/y_scale")  # type: float
        Application.getInstance().getPreferences().addPreference("AutoScalePlugin/z_scale", 0.0)
        self._z_scale = Application.getInstance().getPreferences().getValue("AutoScalePlugin/z_scale")  # type: float
        Application.getInstance().getPreferences().preferenceChanged.connect(self._onPreferencesChanged)

        self.setMenuName("Auto Scale")
        self.addMenuItem("Settings", self.showPopup)

        self._scene_objects = set()
        self._scene = Application.getInstance().getController().getScene()
        self._scene.sceneChanged.connect(self._onSceneChanged)

    def _onPreferencesChanged(self, name: str) -> None:
        if not name.startswith("AutoScalePlugin"):
            return
        self._x_scale = Application.getInstance().getPreferences().getValue("AutoScalePlugin/x_scale")  # type: float
        self._y_scale = Application.getInstance().getPreferences().getValue("AutoScalePlugin/y_scale")  # type: float
        self._z_scale = Application.getInstance().getPreferences().getValue("AutoScalePlugin/z_scale")  # type: float

    def _onSceneChanged(self, _) -> None:
        root = Application.getInstance().getController().getScene().getRoot()
        new_scene_objects = set(node for node in BreadthFirstIterator(root) if node.callDecoration("isSliceable"))
        if new_scene_objects != self._scene_objects:
            to_scale = new_scene_objects - self._scene_objects
            self._scene_objects = new_scene_objects

            for node in to_scale:
                node.scale(Vector(
                    (100.0 + float(self._x_scale)) / 100.0,
                    (100.0 + float(self._z_scale)) / 100.0,
                    (100.0 + float(self._y_scale)) / 100.0
                ))
                self._message = Message(i18n_catalog.i18nc("@info:status", "Scaled: %s." % (node.getName())),
                                        title=i18n_catalog.i18nc("@title", "Auto Scale"))
                self._message.show()

    def _createSettingsView(self) -> None:
        path = os.path.join(PluginRegistry.getInstance().getPluginPath(self.getPluginId()), "SettingsPopup.qml")
        self._settings_view = Application.getInstance().createQmlComponent(path)

    def showPopup(self) -> None:
        if self._settings_view is None:
            self._createSettingsView()
        self._settings_view.show()
