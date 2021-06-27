import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from nes_py.wrappers import JoypadSpace

from services.util_service import RomVersion, get_version

default_version = get_version(world=1, stage=1, version=RomVersion.STANDARD)

env = gym_super_mario_bros.make(default_version)
env = JoypadSpace(env, SIMPLE_MOVEMENT)

(width, height, channel_size) = env.observation_space.shape
