import matplotlib.pyplot as plt
import time as t

time = []
mistakes =0

print ("this program will help type faster")
input("press enter to continue")

while(times)<5:
    start= t.time()
    word = inpute("type word")
    end = t.time()
    time_elasped = end -start

    time.append(time_elasped)

    if (word.lower() != "programming:"):
        mistakes +=1
print("your mode"+ str(mistakes)+"mistakes")
print("Now let's se you evolution")
t.sleep(3)

x=[1,2,3,4,5]
y= times
plt.plot(x,y)
plot.show()
