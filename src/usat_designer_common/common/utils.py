from importlib import resources
import sys, os
from contextlib import contextmanager

def open_t_design_file(filename: str):
    return resources.files("universal_transcoder.encoders.t_design").joinpath(filename).open("r")

def get_num_ambisonics_channels(order: int) -> int:
    return (order + 1) ** 2

@contextmanager
def suppress_stdout():
    saved_stdout = sys.stdout
    try:
        sys.stdout = open(os.devnull, "w")
        yield
    finally:
        sys.stdout.close()
        sys.stdout = saved_stdout