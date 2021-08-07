import datetime

from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

env = gym_super_mario_bros.make('SuperMarioBros-v3')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

done = True
episodes = 1000
for step in range(episodes):
    if done:
        state = env.reset()
    state, reward, done, info = env.step(env.action_space.sample())
    print(datetime.datetime.now(), state)
    env.render()

env.close()

# gym_super_mario_bros -e SuperMarioBros-v0 -m human
