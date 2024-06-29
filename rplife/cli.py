# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 21:53:01 2024

@author: Soheb
"""

import argparse

from rplife import __version__, patterns, views

def get_command_line_args():
	parser = argparse.ArgumentParser(
		prog='rplife',
		description = "Conway's Game of Life - Terminal Edition"
		
		)
	parser.add_argument("--version", action='version',
					 version=f"%(prog)s v(__version__)")
	parser.add_argument(
		"-p",
		"--pattern",
		choices=[pat.name for pat in patterns.get_all_patterns()],
		default='Blinker',
		help="Game of Life Pattern (default = %(default)s)"
		)
	parser.add_argument(
		"-a",
		"--all",
		action="store_true",
		help="Show all available patterns"
		)
	parser.add_argument(
		"-v",
		"--view",
		choices = views.__all__,
		default="CursesView",
		help="Display the game of life in a specific view (default: %(default)s)"
		)
	parser.add_argument(
		"-g",
		"--gen",
		metavar = "NUM_GENERATIONS",
		type =int,
		default=10,
		help="Number of generations: (%(default)s)"
		)
	parser.add_argument(
		"-f",
		"--fps",
		metavar = "FRAMES_PER_SECOND",
		type=int,
		default=7,
		help="Frames per second (%(default)s)"
		)
	return parser.parse_args()