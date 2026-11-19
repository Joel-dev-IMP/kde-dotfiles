#!/bin/bash
qdbus-qt6 org.kde.kglobalaccel /component/kwin invokeShortcut "Switch to Screen 0"
sleep 0.05
qdbus-qt6 org.kde.kglobalaccel /component/kwin invokeShortcut "MoveMouseToFocus"
