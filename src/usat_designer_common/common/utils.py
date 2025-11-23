from importlib import resources

def open_t_design_file(filename: str):
    return resources.files("universal_transcoder.encoders.t_design").joinpath(filename).open("r")

def get_num_ambisonics_channels(order: int) -> int:
    return (order + 1) ** 2