import python_uart_gps as GPS
import time

g=GPS.uart_gps()
f=open("gps_data.csv",'w')    #Open file to log the data
f.write("name,latitude,longitude\n")    #Write the header to the top of the file
while True:
    try:
        data=g.read()
        print("Time:",data['time'],"Fix status:",data['fix'],"Sats in view:",data['sats'],
              "Altitude",data['altitude'],"Lat:",data['lat'],data['lat_ns'],"Long:",data['lon'],data['lon_ew'])
        if data['lat'] is not "" and data['lon'] is not "":
            s=str(data['time'])+","+str(float(data['lat'])/100)+","+str(float(data['lon'])/100)+"\n"
            f.write(s)    #Save to file
        time.sleep(2)
    except IndexError:
        print "Unable to read"
    except KeyboardInterrupt:
        print "Exiting"
        f.close()
        sys.exit(0)


