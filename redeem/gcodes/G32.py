"""
GCode G32
Undock sled

Author: Elias Bakken
email: elias(dot)bakken(at)gmail dot com
Website: http://www.thing-printer.com
License: CC BY-SA: http://creativecommons.org/licenses/by-sa/2.0/
"""
from __future__ import absolute_import

from .GCodeCommand import GCodeCommand
from redeem.Gcode import Gcode


class G32(GCodeCommand):

    def execute(self, g):
        gcodes = self.printer.config.get("Macros", "G32").split("\n")
        self.printer.processor.execute_macro(gcodes=gcodes, parent=g)

    def get_description(self):
        return "Undock sled"

    def is_buffered(self):
        return True

    def get_test_gcodes(self):
        return ["G32"]

