import h5py
import numpy as np
import matplotlib.pyplot as plt

with h5py.File('hdf5_dm_july2021_expert_1.hdf5', 'r') as f:
    num_frames = 20

    for i in range(num_frames):
        image_key = f'frame_{i}_x'
        xaux_key = f'frame_{i}_xaux'
        target_action_key = f'frame_{i}_y'
        helper_arr_key = f'frame_{i}_helperarr'

        if image_key in f:
            frame_image = np.array(f[image_key])
            plt.imshow(frame_image)
            plt.title(f'Frame {i} Image')
        else:
            print(f"Image key {image_key} not found in file.")

        if xaux_key in f:
            frame_metadata = np.array(f[xaux_key])
            print(f"Frame {i} Metadata (xaux):", frame_metadata)
        else:
            print(f"Metadata key {xaux_key} not found in file.")

        if target_action_key in f:
            target_action = np.array(f[target_action_key])
            print(f"Frame {i} Target Actions (y):", target_action)
        else:
            print(f"Target action key {target_action_key} not found in file.")

        if helper_arr_key in f:
            helper_array = np.array(f[helper_arr_key])
            print(f"Frame {i} Helper Array [kill_flag, death_flag]:", helper_array)
        else:
            print(f"Helper array key {helper_arr_key} not found in file.")

        print("\n" + "-"*40 + "\n")
