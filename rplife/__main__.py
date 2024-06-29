# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 21:52:41 2024

@author: Soheb
"""
import sys

from rplife import patterns,views
from rplife.cli import get_command_line_args

def _show_pattern(View, pattern, args):
	try:
		View(pattern=pattern,gen=args.gen,frame_rate=args.fps).show()
	except Exception as error:
		print(error, file=sys.stderr)
		


def main():
	args=get_command_line_args()
	View = getattr(views,args.view)
	if args.all:
		for pattern in patterns.get_all_patterns():
			_show_pattern(View,pattern,args)
	else:
		_show_pattern(
			View,
			patterns.get_pattern(name=args.pattern),
			args
			)
if __name__ == "__main__":
	main()