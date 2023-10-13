import matplotlib.pyplot as plt
import numpy as np

output_data = []

def encode(data):
    if bits[0] == 1:
        output_data.append(-1)
    else:
        output_data.append(1)
        
    for i in range(len(bits)):
        if bits[i]==1:
            output_data.append(-1)
        elif bits[i]==0:
            output_data.append(1)
            
        else:
            print("data invalid")
            
    return output_data
            


strbit = input("enter your bit: ")
bits=[int(bit)for bit in strbit]

x = encode(bits)

y = [i for i in  range(len(output_data))]

plt.step(y,x)


plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('NRZ-L wave') 
plt.grid(True)


plt.show()
            

    
            
   