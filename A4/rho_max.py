#!/usr/bin/python

# Plot evolution of central density
from plot_defaults import *

# load data
Fx, Fy = numpy.loadtxt("dx4.asc.bz2",
                       comments="#", usecols=(1,2), unpack=True)
Gx, Gy = numpy.loadtxt("dx8.asc.bz2",
                       comments="#", usecols=(1,2), unpack=True)

# plot basics
fig = plt.figure(figsize=(6, 3))
fig.subplots_adjust(top=0.85, bottom=0.16, left=0.12,right=0.97)
ax = fig.add_subplot(1,1,1)

# plot
ax.plot(Fx/200, Fy/Fy[0]*100, linestyle='--', color='blue', label='dx=4')
ax.plot(Gx/200, Gy/Gy[0]*100, linestyle='-', color='black', label='dx=8')
plt.axis([0, 260000, 99.0, 100.5])

ax.legend(loc='upper left')
ax.set_xlabel(r't [ms]')
#ax.set_xlim((ax.get_xlim()[0]/M_to_ms, ax.get_xlim()[1]/M_to_ms))
ax.xaxis.set_minor_locator(mticker.AutoMinorLocator())
ax.xaxis.grid(False)
ax2 = ax.twiny()
ax2.set_xlabel(r't [M]')
ax2.set_xlim((0, 1300))
ax.set_xlim((ax2.get_xlim()[0]/M_to_ms, ax2.get_xlim()[1]/M_to_ms))
ax2.xaxis.set_minor_locator(mticker.AutoMinorLocator())
ax.xaxis.set_minor_locator(mticker.MultipleLocator(.5))
ax.set_ylabel(r'$\varrho_c/\varrho_c(0)[\%]$')
ax.yaxis.set_major_locator(mticker.MaxNLocator(4))
ax.yaxis.set_minor_locator(mticker.AutoMinorLocator())
ax.yaxis.grid(False)
set_tick_sizes(ax, 8, 4)

#plt.show()
plt.savefig('rho_max.pdf')

