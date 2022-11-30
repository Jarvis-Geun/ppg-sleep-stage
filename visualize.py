import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class AnimationPlot:
    def animate(self, i, dataList, py_serial):
        #print(i)                                           # 'i' is a incrementing variable based upon frames = x argument

        if py_serial.readable():
            ppg = py_serial.readline()
            ppg = str(ppg).lstrip("b'")
            ppg = ppg[:7]
            ppg = ppg + '\n'
            dataList.append(ppg)
            print(ppg)

        dataList = dataList[-50:]                           # Fix the list size so that the animation plot 'window' is x number of points
        ax.clear()                                          # Clear last data frame
        
        self.getPlotFormat()
        ax.plot(dataList)                                   # Plot new data frame


    def getPlotFormat(self):
        ax.set_ylim(0, 4)                              # Set Y axis limit of plot
        ax.set_title("PPG data")                        # Set title of figure
        ax.set_ylabel("PPG")                              # Set title of y axis


if __name__=="__main__":
    py_serial = serial.Serial(
        port='/dev/cu.usbserial-130',
        # Baud rate (speed of communication)
        baudrate=9600,
    )
    
    dataList = []                                           # Create empty list variable for later use

    fig = plt.figure()                                      # Create Matplotlib plots fig is the 'higher level' plot window
    ax = fig.add_subplot(111)                               # Add subplot to main fig window

    realTimePlot = AnimationPlot()
    time.sleep(2)                                           # Time delay for Arduino Serial initialization 

                                                            # Matplotlib Animation Fuction that takes takes care of real time plot.
                                                            # Note that 'fargs' parameter is where we pass in our dataList and Serial object. 
    ani = animation.FuncAnimation(fig, realTimePlot.animate, frames=100, fargs=(dataList, py_serial), interval=1) 

    plt.show()                                              # Keep Matplotlib plot persistent on screen until it is closed
    py_serial.close()                                             # Close Serial connection when plot is closed