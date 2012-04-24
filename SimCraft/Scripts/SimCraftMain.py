# -*- coding: utf-8 -*-

import Python # Ladda in vår c++ modul GameEngine

totaltime = 0
id = 0
def Update(time):
	global totaltime
	global id
	
	totaltime += time
	if totaltime > 5000:
		Python.CreateEntity("Media/bth.obj", id, id * 5, -10, 0)
		id += 1
		totaltime = 0
	
	if id > 3:
		Python.DeleteEntity(0)
		Python.DeleteEntity(1)
		Python.DeleteEntity(2)

	return (i < 20000)