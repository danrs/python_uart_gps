import python_uart_gps as GPS
import time

g=GPS.uart_gps()
while True:
    try:
        data=g.read()
        print("Time:",data['time'],"Fix status:",data['fix'],"Sats in view:",data['sats'],
              "Altitude",data['altitude'],"Lat:",data['lat'],data['lat_ns'],"Long:",data['lon'],data['lon_ew'])
        time.sleep(2)
    except IndexError:
        print "Unable to read"
    except KeyboardInterrupt:
        print "Exiting"
        sys.exit(0)


