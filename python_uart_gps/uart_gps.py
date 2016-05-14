# Copyright (c) 2016 Daniel Smith
# Author: Daniel Smith
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import time
import sys
import serial


class uart_gps:
    # The GPS module used is a Grove GPS module http://www.seeedstudio.com/depot/Grove-GPS-p-959.html
    # Refer to SIM28 NMEA spec file http://www.seeedstudio.com/wiki/images/a/a0/SIM28_DATA_File.zip

    def __init__(self, port="/dev/ttyO2", baudrate=9600, timeout=1):
        self.port = port
        self.baud = baudrate
        self.timeout = timeout
        self.sensor = serial.Serial(port, baudrate, timeout)
        self.sensor.flush()
        self.read() #set up values

    #Read data from the GPS
    def read(self):
        while True:
            raw = self.sensor.readline()
            if raw[:6] =='$GPGGA': # this is the packet we are looking for
                break
        try:
            index = raw.index('$GPGGA',5,len(raw)) # Take data after the last '$GPGGA'
            raw = raw[ind:]
        except ValueError:
            pass

        parsed_input = raw.split(",") #Split the stream into individual parts
        self.time = parsed_input[1] #UTC time
        self.lat = parsed_input[2]
        self.lat_ns = parsed_input[3]
        self.lon = parsed_input[4]
        self.lon_ew = parsed_input[5]
        self.fix = parsed_input[6]
        self.sats = parsed_input[7]
        self.altitude = parsed_input[9]
        return self.current_values()

    #Split the data into individual elements
    def current_values(self):
        data = {}
        data['time'] = self.time
        data['lat'] = self.lat
        data['lat_ns'] = self.lat_ns
        data['lon'] = self.lon
        data['lon_ew'] = self.lon_ew
        data['fix'] = self.fix
        data['sats'] = self.sats
        data['altitude'] = self.altitude
        return data
