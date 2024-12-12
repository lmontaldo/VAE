import os
import subprocess

# Configuration based on the described setup
args = {
    "nps": 1000,         # Number of samples (L) per segment
    "ns": 20,            # Number of segments (M)
    "dl": 3,             # Dimension of the latent sources
    "dd": 6,             # Dimension of the mixed data
    "nl": 3,             # Number of layers in the MLP
    "s": 42,             # Random seed for reproducibility
    "p": 'gauss',        # Prior distribution ('gauss' for Gaussian, 'lap' for Laplace)
    "a": 'xtanh',        # Activation function for MLP
    "uncentered": False, # Centering of the sources
    "noisy": True        # Whether to add noise to observations
}

# Ensure the output directory exists
output_dir = 'VAE/data'
os.makedirs(output_dir, exist_ok=True)

# Function to simulate data for specific conditions
def simulate_data(p, noisy, suffix):
    command = [
        'python', 'data.py', 
        str(args["nps"]), str(args["ns"]), str(args["dl"]), str(args["dd"]),
        '-l', str(args["nl"]), '-s', str(args["s"]), '-p', p, '-a', args["a"]
    ]

    if args["uncentered"]:
        command.append('-u')
    if noisy:
        command.append('-n')

    # Run the simulation
    print(f"Running simulation: Prior={p}, Noisy={noisy}")
    subprocess.run(command, check=True)

    print(f"Simulation complete for {p}, noisy={noisy}. Check the output folder.")

# Run simulations for different configurations
simulate_data('gauss', True, 'gauss_noisy')
simulate_data('lap', True, 'lap_noisy')
simulate_data('gauss', False, 'gauss_clean')
