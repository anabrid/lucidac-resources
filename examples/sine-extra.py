# Copyright (c) 2022-2025 anabrid GmbH
# Contact: https://www.anabrid.com/licensing/
# SPDX-License-Identifier: MIT OR GPL-2.0-or-later
from pybrid.lucidac.lucipy import Circuit, LUCIDAC, time_series
import matplotlib.pyplot as plt
import numpy as np

###
# Create a simple sine/cosine oscillator circuit in lucipy-syntax with some
# additional goodies (LEDs, signal generator) showing the use of the pront panel
###

c   = Circuit()                         # Create a circuit

ic_sin  = -1                            # Initial value for the sine
omega   = .01 * (2.*np.pi)              # Oscillation frequency

sin = c.int(ic = ic_sin)                # Integrators for sine and cosine
cos = c.int()

c.connect(sin, cos, weight = +omega)    # Connect sine to cosine integrator
c.connect(cos, sin, weight = -omega)    # Connect cosine to sine integrator

c.measure(sin, adc_channel=0)           # Connect integrators to ADC
c.measure(cos, adc_channel=1)           # to sample data

# output signals on ACL_OUT - indexec from left starting from 0 through `front_port`
c.probe(sin, front_port=0, weight=0.2)
c.probe(cos, front_port=1, weight=0.5)

###
# Setup the front panel: signal generator & LEDs
# - output either a sine & rect OR triangle (on SINE port)
# - output two constant signals at AUX port
###

# sets frequency of sine, rect, triangle in Hza
c.front_panel.set_frequency(1000)

# enables sine wave with amplitude (0 - 1) and offset(0 - 0.5)
c.front_panel.set_sine(amplitude=0.6, offset=0.2)

# set rectagle signal that switches between low and high voltage
c.front_panel.set_rect(low=-0.2, high=0.7)

# set triangle signal with amplitude = 1
c.front_panel.set_triangle(offset=0.2)

# set constant values for AUX ports
c.front_panel.set_aux(0.3, -0.8)

# note: the generator allows onlu outputting sine & rect _OR_ triangle at each iime
# plus the two AUX signals

# set 8 LED states on frontpanel from left to right
c.front_panel.set_leds([True, True, False, True, False, True, True, True])


###
# Auto-detect LUCIDAC-device (empty constructor) or:
# - set environment variable LUCIDAC_ENDPOINT to a connection string
# - pass the connection string directly
#
# where the connection string is `tcp://<LUCIDAC IP or hostname>:5732`.
###
luci    = LUCIDAC()

luci.set_circuit(c)                     # Assign circuit

###
# Settings for sampling and circuit execution
###
op_secs     = .1                       # Duration of OP cycle in seconds
sample_rate = 100_000                   # Samples per second (max: 150_000 for each channel)

luci.set_daq(num_channels=2, sample_rate=sample_rate)
luci.set_run(ic_time = 1_000, op_time=int(op_secs * 1_000_000_000))

###
# Run circuit and start sampling
###
run = luci.run()

###
# Receive sample data and plot
###
for adc_key, values in run.data.items():
    x = time_series(sample_rate, len(values))
    plt.plot(x, values, label=adc_key[-1])
plt.xlabel("time / s")
plt.legend()
plt.grid()
plt.show()
