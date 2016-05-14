import python_uart_gps as GPS
import time

g=GPS.uart_gps()
while True:
    try:
        [t,fix,sats,alt,lat,lat_ns,lon,lon_ew]=g.read()
        print "Time:",t,"Fix status:",fix,"Sats in view:",sats,"Altitude",alt,"Lat:",lat,lat_ns,"Long:",lon,lon_ew
        time.sleep(2)
    except IndexError:
        print "Unable to read"
    except KeyboardInterrupt:
        print "Exiting"
        sys.exit(0)


