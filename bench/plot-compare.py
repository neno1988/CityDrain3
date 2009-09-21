#!/usr/bin/env python
import matplotlib as mpl
mpl.use('cairo')

from pylab import *
import glob
import sys
import os
import re

inch=2.54

if len(sys.argv) < 3:
	print "usage plot.py model pid"
	exit(-1)
	
format="pdf"
	
if len(sys.argv) > 3:
	format=sys.argv[3]

rc('font', size=8)
rc('figure.subplot', left=0.17, right=0.95, top=0.92, bottom=0.20)

model = sys.argv[1]
pid = sys.argv[2]

types = []
datas={}
for path in os.listdir('time/'):
	rexp = "%s-([a-x]+)-%s-time-avg\.txt" % (model, pid)
	m = re.match(rexp, path)
	if (m):
		strat = "time/%s" % m.group(0)
		datas[m.group(1)] = csv2rec(strat, delimiter="\t", names=['nthreads', 'runtime'])
		types.append(m.group(1))
	
x=[]
for s in types:
	x.append(datas[s].runtime)

f=figure(figsize=(8/inch, 5.1/inch))
	
lines=plot(transpose(x))
ls = ['-', '--', ':']

for i in range(len(types)):
	lines[i].set_linestyle(ls[i])
	
xlabel('number of threads')#, va='bottom')
ylabel('runtime (ms)')#, ha='left')
l=legend(lines, types, 'best')
l.draw_frame(False)
savefig('imgs/%s-%s-comp.%s' % (model, pid, format), format=format, dpi=400)#, bbox_inches="tight")
#show()

