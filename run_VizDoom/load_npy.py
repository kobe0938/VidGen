import matplotlib.pyplot as plt
import numpy as np

action_data = np.load('action_data.npy')
frame_data = np.load('frame_data.npy')

print(f"Action Data Shape: {action_data.shape}")
print(f"Action Data Type: {type(action_data)}")
print(f"Frame Data Shape: {frame_data.shape}")
print(f"Frame Data Type: {type(frame_data)}")

for i in range(3):
    action = action_data[i]
    frame = frame_data[i]
    print(f"Step {i}: Action taken = {action}, Frame shape = {frame.shape}")


plt.imshow(frame_data[0])
plt.title("First Frame")
plt.show()
