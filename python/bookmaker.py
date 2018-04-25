# -*- coding:utf-8 -*-
#!/usr/bin/python

import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import datetime
import time
import json
import twitter


north = []
west = []
east = []
south = []

p_n = []
p_w = []
p_e = []
p_s = []

x = [8, 8.3333, 8.6667,
	10, 10.3333, 10.6667, 
	12, 12.3333, 12.6667,
	14, 14.3333, 14.6667,
	16, 16.3333, 16.6667,
	17, 17.3333, 17.6667,
	18, 18.3333, 18.6667,
	20, 20.3333, 20.6667,
	22, 22.3333, 22.6667,
	24, 24.3333, 24.6667]
xt = ["08:00", "08:20", "08:40",
	"10:00", "10:20", "10:40",
	"12:00", "12:20", "12:40",
	"14:00", "14:20", "14:40",
	"16:00", "16:20", "16:40",
    "17:00", "17:20", "17:40", 
	"18:00", "18:20", "18:40",
	"20:00", "20:20", "20:40",
	"22:00", "22:20", "22:40",
	"24:00", "24:20", "24:40"]

def dealWithData(data):
	data = json.loads(data)
	north.append(int(data["north"]))
	west.append(int(data["west"]))
	east.append(int(data["east"]))
	south.append(int(data["south"]))
	t = len(north) - 1
	maxNumber = max(north[t], west[t], east[t], south[t])
	if maxNumber == 0:
		maxNumber = 1
	p_n.append(round(north[t]/maxNumber*10000, 4))
	p_w.append(round(west[t]/maxNumber*10000, 4))
	p_e.append(round(east[t]/maxNumber*10000, 4))
	p_s.append(round(south[t]/maxNumber*10000, 4))
	xtemp = []
	xttemp = []
	for i in range(t + 1):
		xtemp.append(x[i])
		xttemp.append(xt[i])

	plt.figure(figsize=(12, 6), dpi=200)
	plt.xlabel("Time")
	plt.ylabel("percent")
	plt.xlim(8, 24)
	title = str(time.strftime("%Y-%m-%d", time.localtime())) + " " +str(xt[t])
	plt.title(title)
	plt.xticks(xtemp, xttemp, rotation=50)
	plt.plot(xtemp, p_n, color="green", label="north")
	plt.plot(xtemp, p_s, color="darkred", label="south")
	plt.plot(xtemp, p_w, color="gray", label="west")
	plt.plot(xtemp, p_e, color="navy", label="east")
	plt.grid(True)
	plt.legend(loc="best")
	filename = str(time.strftime("%Y-%m-%d", time.localtime())) + str(xt[t]) + ".png"
	plt.savefig(filename)
	twitter.sendImage(title, filename)