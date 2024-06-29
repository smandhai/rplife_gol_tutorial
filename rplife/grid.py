# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 21:53:11 2024

@author: Soheb
"""

import collections

ALIVE = "♥"
DEAD = "."

class LifeGrid:
	def __init__(self,pattern):
		self.pattern = pattern
	def evolve(self):
		neighbours = (
			(-1,-1), #Top left
			(-1,0),  #Top
			(-1,1),  #Top right
			(0,-1),  #Left
			(0,1),   #Right
			(1,1),   #Bottom Right
			(1,0),   #Bottom
			(1,-1),  #Bottom Left
			)
		num_neighbours = collections.defaultdict(int)
		for row, col in self.pattern.alive_cells:
			for drow, dcol in neighbours:
					num_neighbours[(row+drow,col+dcol)] +=1
		stay_alive = {
			cell for cell, num in num_neighbours.items() if num in {2,3}
			} & self.pattern.alive_cells
		come_alive = {
			cell for cell, num in num_neighbours.items() if num==3
			} - self.pattern.alive_cells
		
		self.pattern.alive_cells = stay_alive | come_alive
		
		pass
	def as_string(self,bbox):
		start_col, start_row, end_col, end_row = bbox
		display = [self.pattern.name.center(2*(end_col-start_col))]
		for row in range(start_row,end_row):
			display_row = [
				ALIVE if (row,col) in self.pattern.alive_cells else DEAD
				for col in range(start_col, end_col)
				]
			display.append(" ".join(display_row))
		return "\n ".join(display)
			
	def __str__(self):
		return (
			f"{self.pattern.name}:\n"
			f"Alive Cells -> {sorted(self.pattern.alive_cells)}"
			)
		pass