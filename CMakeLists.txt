project(CuraAutoScalePlugin NONE)

cmake_minimum_required(VERSION 3.0.0)

install(FILES
	plugin.json
    AutoScalePlugin.py
    LICENSE
    README.md
    __init__.py
    DESTINATION lib/cura/plugins/AutoScalePlugin
)
