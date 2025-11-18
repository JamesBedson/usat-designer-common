# COEFFICIENTS
DSN_COEFF_ENERGY                  = "energy"
DSN_COEFF_RADIAL_INTENSITY        = "radialIntensity"
DSN_COEFF_TRANSVERSE_INTENSITY    = "transverseIntensity"
DSN_COEFF_PRESSURE                = "pressure"
DSN_COEFF_RADIAL_VELOCITY         = "radialVelocity"
DSN_COEFF_TRANSVERSE_VELOCITY     = "transverseVelocity"
DSN_COEFF_IN_PHASE_QUADRATIC      = "inPhaseQuadratic"
DSN_COEFF_SYMMETRY_QUADRATIC      = "symmetryQuadratic"
DSN_COEFF_IN_PHASE_LINEAR         = "inPhaseLinear"
DSN_COEFF_SYMMETRY_LINEAR         = "symmetryLinear"
DSN_COEFF_TOTAL_GAINS_LINEAR      = "totalGainsLinear"
DSN_COEFF_TOTAL_GAINS_QUADRATIC   = "totalGainsQuadratic"

OPT_COEFF_ENERGY                  = "energy"
OPT_COEFF_RADIAL_INTENSITY        = "radial_intensity"
OPT_COEFF_TRANSVERSE_INTENSITY    = "transverse_intensity"
OPT_COEFF_PRESSURE                = "pressure"
OPT_COEFF_RADIAL_VELOCITY         = "radial_velocity"
OPT_COEFF_TRANSVERSE_VELOCITY     = "transverse_velocity"
OPT_COEFF_IN_PHASE_QUADRATIC      = "in_phase_quad"
OPT_COEFF_SYMMETRY_QUADRATIC      = "symmetry_quad"
OPT_COEFF_IN_PHASE_LINEAR         = "in_phase_lin"
OPT_COEFF_SYMMETRY_LINEAR         = "symmetry_lin"
OPT_COEFF_TOTAL_GAINS_LINEAR      = "total_gains_lin"
OPT_COEFF_TOTAL_GAINS_QUADRATIC   = "total_gains_quad"

# camel case to snake case translation
parameter_to_coefficient_key = {
    DSN_COEFF_ENERGY: OPT_COEFF_ENERGY,
    DSN_COEFF_RADIAL_INTENSITY: OPT_COEFF_RADIAL_INTENSITY,
    DSN_COEFF_TRANSVERSE_INTENSITY: OPT_COEFF_TRANSVERSE_INTENSITY,
    DSN_COEFF_PRESSURE: OPT_COEFF_PRESSURE,
    DSN_COEFF_RADIAL_VELOCITY: OPT_COEFF_RADIAL_VELOCITY,
    DSN_COEFF_TRANSVERSE_VELOCITY: OPT_COEFF_TRANSVERSE_VELOCITY,
    DSN_COEFF_IN_PHASE_QUADRATIC: OPT_COEFF_IN_PHASE_QUADRATIC,
    DSN_COEFF_SYMMETRY_QUADRATIC: OPT_COEFF_SYMMETRY_QUADRATIC,
    DSN_COEFF_TOTAL_GAINS_QUADRATIC: OPT_COEFF_TOTAL_GAINS_QUADRATIC,
    DSN_COEFF_IN_PHASE_LINEAR: OPT_COEFF_TOTAL_GAINS_LINEAR,
    DSN_COEFF_SYMMETRY_LINEAR: OPT_COEFF_SYMMETRY_LINEAR,
    DSN_COEFF_TOTAL_GAINS_LINEAR: OPT_COEFF_TOTAL_GAINS_LINEAR
}

# Optimisation Dictionary Keys
# PARAMETER DICTIONARY
OPT_PD_INPUT_MATRIX_PLOTS          = "input_matrix_plots"
OPT_PD_INPUT_MATRIX_OPTIMIZATION   = "input_matrix_optimization"
OPT_PD_CLOUD_PLOTS                 = "cloud_plots"
OPT_PD_CLOUD_OPTIMIZATION          = "cloud_optimization"
OPT_PD_OUTPUT_LAYOUT               = "output_layout"
OPT_PD_T_OPTIMIZED                 = "T_optimized"
OPT_PD_SHOW_RESULTS                = "show_results"
OPT_PD_SAVE_RESULTS                = "save_results"
OPT_PD_RESULTS_FILE_NAME           = "results_file_name"
OPT_PD_COEFFICIENTS                = "coefficients"
OPT_PD_DIRECTIONAL_WEIGHTS         = "directional_weights"
OPT_PD_DSPK                        = "Dspk"