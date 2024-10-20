import vizdoom as vzd
import numpy as np
import time
import cv2

game = vzd.DoomGame()
game.load_config("../ViZDoom/scenarios/basic.cfg")
game.set_window_visible(True)
game.set_mode(vzd.Mode.PLAYER)
game.init()

actions = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
action_data = []
frame_data = []

fps = 35
frame_size = (game.get_screen_width(), game.get_screen_height())
video_writer = cv2.VideoWriter(
    "doom_rl_data.avi", cv2.VideoWriter_fourcc(*'XVID'), fps, frame_size)

for episode in range(3):
    print(f"Starting Episode {episode + 1}")
    game.new_episode()

    while not game.is_episode_finished():
        state = game.get_state()
        screen_buffer = state.screen_buffer
        frame = np.moveaxis(screen_buffer, 0, -1)
        frame_data.append(frame)
        video_writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        action = actions[np.random.randint(len(actions))]
        action_data.append(action)
        reward = game.make_action(action)
        time.sleep(0.02)

    print(
        f"Episode {episode + 1} finished. Total reward: {game.get_total_reward()}")

game.close()
video_writer.release()
np.save('action_data.npy', action_data)
np.save('frame_data.npy', frame_data)
print("Data collection finished.")
