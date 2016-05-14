import python_uart_gps as GPS
import time

g=GPS.uart_gps()
f=open("gps_data.csv",'w')    #Open file to log the data
f.write("name,latitude,longitude\n")    #Write the header to the top of the file
while True:
    try:
        [t,fix,sats,alt,lat,lat_ns,lon,lon_ew]=g.read()
        print "Time:",t,"Fix status:",fix,"Sats in view:",sats,"Altitude",alt,"Lat:",lat,lat_ns,"Long:",lon,lon_ew
        if lat is not "" and lon is not "":
            s=str(t)+","+str(float(lat)/100)+","+str(float(lon)/100)+"\n"
            f.write(s)    #Save to file
        time.sleep(2)
    except IndexError:
        print "Unable to read"
    except KeyboardInterrupt:
        print "Exiting"
        f.close()
        sys.exit(0)


