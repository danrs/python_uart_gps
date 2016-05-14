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

ser = serial.Serial(port = "/dev/ttyO2", baudrate=9600)
ser.flush()

class uart_gps:
    # The GPS module used is a Grove GPS module http://www.seeedstudio.com/depot/Grove-GPS-p-959.html
    # Refer to SIM28 NMEA spec file http://www.seeedstudio.com/wiki/images/a/a0/SIM28_DATA_File.zip

    def __init__(self):
        raw=[] #raw input string
        parsed_input=[] #parsed input

    #Read data from the GPS
    def read(self):
        while True:
            self.raw = ser.readline()
            if self.raw[:6] =='$GPGGA': # parsed_input data , packet 1, has all the data we need
                break
        try:
            index = self.raw.index('$GPGGA',5,len(self.raw)) #Sometimes multiple GPS data packets come into the stream. Take the data only after the last '$GPGGA' is seen
            self.raw = self.raw[ind:]
        except ValueError:
            pass
        self.parsed_input=self.raw.split(",") #Split the stream into individual parts
        return self.current_values()

    #Split the data into individual elements
    def current_values(self):
        time=self.parsed_input[1] #UTC time
        lat=self.parsed_input[2]
        lat_ns=self.parsed_input[3]
        lon=self.parsed_input[4]
        lon_ew=self.parsed_input[5]
        fix=self.parsed_input[6]
        sats=self.parsed_input[7]
        alt=self.parsed_input[9]
        return [time,fix,sats,alt,lat,lat_ns,lon,lon_ew]
