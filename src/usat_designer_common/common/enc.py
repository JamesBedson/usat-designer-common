# ================================================================
# Encoding and Decoding Utilities for USAT Designer
# ================================================================

# Miscellaneous imports
import os
from typing import Union
from pathlib import Path

# Universal Transcoder imports
from universal_transcoder.auxiliars.my_coordinates import MyCoordinates
from universal_transcoder.auxiliars.get_cloud_points import (
    get_all_sphere_points,
    get_equi_t_design_points,
    get_equi_circumference_points,
    mix_clouds_of_points
)

from universal_transcoder.auxiliars.get_input_channels import (
    get_input_channels_ambisonics,
    get_input_channels_vbap
)

# USAT Designer Common imports
from usat_designer_common.constants.io import *
from usat_designer_common.constants.opt import *
from usat_designer_common.common.utils import (
    open_t_design_file,
    get_num_ambisonics_channels
)

# ================================================================

def get_ambisonics_enc_matrix(order: int, 
                              t_design_filename: str) -> tuple:

    with open_t_design_file(t_design_filename) as f:
        cloud_optimization = get_equi_t_design_points(f, False)

    G = get_input_channels_ambisonics(cloud_optimization, order)
    return cloud_optimization, G


def get_ambisonics_output(order: int) -> MyCoordinates:

    # Load t-design file
    with open_t_design_file("des.3.60.10.txt") as f:
        t_design_points = get_equi_t_design_points(f, False)

    list_of_cloud_points = [
        t_design_points,
        get_equi_circumference_points(
            get_num_ambisonics_channels(order), 
            False
        )
    ]

    list_of_weights = [1, 1]
    ambisonics_output, _ = mix_clouds_of_points(
        list_of_cloud_points=list_of_cloud_points,
        list_of_weights=list_of_weights,
        discard_lower_hemisphere=True
    ) 
    
    return ambisonics_output


def get_speaker_enc_matrix(speaker_layout: MyCoordinates,
                           t_design_filename: str) -> tuple:

    # Load t-design file
    with open_t_design_file(t_design_filename) as f:
        t_design_points = get_equi_t_design_points(f, False)

    circumference_points = get_equi_circumference_points(15, False)
    cloud_points_list = [t_design_points, circumference_points, speaker_layout]     
    
    cloud_optimization, weights = mix_clouds_of_points(
        cloud_points_list,
        list_of_weights=None,
        discard_lower_hemisphere=True
    )

    G = get_input_channels_vbap(cloud_optimization, speaker_layout)
    
    return cloud_optimization, G, weights


def create_encoding_matrix(format: str, parameter_dict: dict, layout_data: Union[int, MyCoordinates]) -> dict:

    t_design_filename = "des.3.56.9.txt"

    cloud_plots = get_all_sphere_points(1, plot_show=False).discard_lower_hemisphere()

    if format == DSN_XML_AMBISONICS:
        assert(isinstance(layout_data, int))
        directional_weights = 1
        cloud_optimization, G = get_ambisonics_enc_matrix(layout_data, t_design_filename)
        input_matrix_plots = get_input_channels_ambisonics(cloud_plots, layout_data)
    
    elif format == DSN_XML_SPEAKER_LAYOUT:
        assert(isinstance(layout_data, MyCoordinates))
        cloud_optimization, G, directional_weights = get_speaker_enc_matrix(layout_data, t_design_filename)
        input_matrix_plots = get_input_channels_vbap(cloud_plots, layout_data)

    else:
        raise ValueError("Invalid Format.", format)

    parameter_dict[OPT_PD_DIRECTIONAL_WEIGHTS] = directional_weights
    parameter_dict[OPT_PD_CLOUD_OPTIMIZATION] = cloud_optimization
    parameter_dict[OPT_PD_CLOUD_PLOTS] = cloud_plots
    parameter_dict[OPT_PD_INPUT_MATRIX_PLOTS] = input_matrix_plots
    parameter_dict[OPT_PD_INPUT_MATRIX_OPTIMIZATION] = G

    return parameter_dict