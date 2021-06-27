class RomVersion:
    STANDARD = 0
    DOWN_SAMPLED = 1
    PIXEL = 2
    RECTANGLE = 3


MARIO_ENVS = [
    "SuperMarioBros-v0",  # SMB standard
    "SuperMarioBros-v1",  # SMB downsample
    "SuperMarioBros-v2",  # SMB pixel
    "SuperMarioBros-v3",  # SMB rectangle
    "SuperMarioBros2-v0",  # SMB2 standard
    "SuperMarioBros2-v1",  # SMB2 downsample
]


def get_version(world: int, stage: int, version: RomVersion):
    """
    :param int world: <world> is a number in {1, 2, 3, 4, 5, 6, 7, 8} indicating the world.
    :param int stage: <stage> is a number in {1, 2, 3, 4} indicating the stage within a world.
    :param int version: <version> is a number in {0, 1, 2, 3} specifying the ROM mode to use.
        0: standard ROM
        1: downsampled ROM
        2: pixel ROM
        3: rectangle ROM
    :return:
    """
    return f"SuperMarioBros-{world}-{stage}-v{version}"
