
import os
import warnings
import jax.numpy as jnp
import numpy as np
from typing import Dict, Any

from universal_transcoder.calculations.optimization import bfgs_optim
from universal_transcoder.calculations.set_up_system import set_up_general

from constants.opt import *
from constants.io import *
from constants.data import *

warnings.filterwarnings("ignore")
os.environ["JAX_ENABLE_X64"] = "1"

# =======================================================================
# Main optimization function
# =======================================================================
def optimize_for_usat_designer(info: Dict[str, Any]) -> dict:
        
    output_layout = info[OPT_PD_OUTPUT_LAYOUT]
    current_state, T_flatten_initial = set_up_general(info)

    T_flatten_optimized = bfgs_optim(
        current_state,
        T_flatten_initial,
        info[OPT_PD_SHOW_RESULTS],
        info[OPT_PD_SAVE_RESULTS],
        info[OPT_PD_RESULTS_FILE_NAME],
    )

    T_optimized = np.array(T_flatten_optimized).reshape(
        current_state.transcoding_matrix_shape
    )
    
    D = T_optimized
    if OPT_PD_DSPK in info.keys():
        D = jnp.dot(info[OPT_PD_DSPK], T_optimized)

    if OPT_PD_CLOUD_PLOTS in info:
        G = info[OPT_PD_INPUT_MATRIX_PLOTS]
        cloud = info[OPT_PD_CLOUD_PLOTS]

    else:
        G = info[OPT_PD_INPUT_MATRIX_OPTIMIZATION]
        cloud = info[OPT_PD_CLOUD_OPTIMIZATION]    

    S = jnp.dot(G, D.T)
    
    output = {
        DSN_OUT_ENCODING_MATRIX: G,
        DSN_OUT_DECODING_MATRIX: D,
        DSN_OUT_TRANSCODING_MATRIX: T_optimized,
        DSN_OUT_SPEAKER_MATRIX: S,
        DSN_OUT_OUTPUT_LAYOUT: output_layout,
        DSN_OUT_CLOUD: cloud, 
    }
    
    return output