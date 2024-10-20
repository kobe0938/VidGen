conda create --name VidGen python=3.10 -y

conda activate VidGen

brew install cmake boost sdl2

pip3 install vizdoom

generate data
python3 vizdoom_example.py

load data
python3 load_npy.py