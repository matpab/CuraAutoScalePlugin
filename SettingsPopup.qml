// Copyright (c) 2020 Matthias Pabel

import QtQuick 2.2
import QtQuick.Controls 2.0


import UM 1.2 as UM

UM.Dialog
{
    minimumWidth: 350
    minimumHeight: 150

    title: qsTr("Auto scale plugin settings")

    Column
    {
        anchors.fill: parent;
        Row
        {
            Text
            {
                id: xLabel
                anchors.verticalCenter: xScale.verticalCenter
                text: qsTr("X-Scale")
            }
            TextField
            {
                id: xScale
                height: xLabel.height + 10
                text: UM.Preferences.getValue("AutoScalePlugin/x_scale")
                Keys.onReleased:
                {
                    UM.Preferences.setValue("AutoScalePlugin/x_scale", parseFloat(x_scale.text))
                }
            }
        }
        Row
        {
            Text
            {
                id: yLabel
                anchors.verticalCenter: yScale.verticalCenter
                text: qsTr("Y-Scale")
            }
            TextField
            {
                id: yScale
                height: yLabel.height + 10
                text: UM.Preferences.getValue("AutoScalePlugin/y_scale")
                Keys.onReleased:
                {
                    UM.Preferences.setValue("AutoScalePlugin/y_scale", parseFloat(y_scale.text))
                }
            }
        }
        Row
        {
            Text
            {
                id: zLabel
                anchors.verticalCenter: zScale.verticalCenter
                text: qsTr("Z-Scale")
            }
            TextField
            {
                id: zScale
                height: zLabel.height + 10
                text: UM.Preferences.getValue("AutoScalePlugin/y_scale")
                Keys.onReleased:
                {
                    UM.Preferences.setValue("AutoScalePlugin/z_scale", parseFloat(z_scale.text))
                }
            }
        }
    }
}