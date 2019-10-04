# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class Gcode3dPlugin(octoprint.plugin.AssetPlugin):

	##~~ AssetPlugin mixin

	def get_assets(self):
		return dict(
			js=["lib/three.js","lib/TrackballControls.js","js/renderer3d.js","js/gcode3d.js"]
		)

	def get_update_information(self):
		return dict(
			gcode3d=dict(
				displayName="OctoPrint-GCode3D",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="jneilliii",
				repo="OctoPrint-GCode3D",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/jneilliii/OctoPrint-GCode3D/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "OctoPrint-GCode3D"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = Gcode3dPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

