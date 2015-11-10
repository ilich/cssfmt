#!/usr/bin/env python

import argparse
import os
import os.path
import cssutils
import logging

def get_arguments_parser():
	parser = argparse.ArgumentParser(description="Apply CSS formatting guidelines to a file")
	parser.add_argument('-v', action='version', version='%(prog)s 0.0.1')
	parser.add_argument("-t", action="store_true", help="use tabs instead of spaces for indentation")
	parser.add_argument("-i", type=int, const=True, nargs="?", metavar="SIZE", help="set indentation size. The option is ignored if -t switch is used.", default=4)
	parser.add_argument("FILE", help="target CSS file")
	return parser
	
class CssFormatter:
	_DEFAULT_INDENT = 4
	
	def __init__(self, args):
		self._useTabs = args.t
		self._indent = args.i if args.i > 0 else self._DEFAULT_INDENT
		self._target = args.FILE
		
	@property
	def target(self):
		return self._target
		
	def format(self):
		if not os.path.isfile(self._target):
			raise FileNotFoundError
		
		# Disable cssutils warnings
		cssutils.log.setLevel(logging.CRITICAL)
		
		# Setup CSS serializer
		cssutils.ser.prefs.indent = "\t" if self._useTabs else " " * self._indent
		cssutils.ser.prefs.keepEmptyRules = True
		cssutils.ser.prefs.omitLastSemicolon = False
		cssutils.ser.prefs.indentClosingBrace = False
		
		styles = cssutils.parseFile(self._target)
		cssText = styles.cssText.decode()
		with open(self._target, "w") as out:
			out.write(cssText)		
		
def main():
	parser = get_arguments_parser()
	args = parser.parse_args()
	
	formatter = CssFormatter(args)
	try:
		formatter.format()
		print("DONE.")
	except FileNotFoundError:
		print("error: file %s is not found" % formatter.target)
	
if __name__ == "__main__":
	main()