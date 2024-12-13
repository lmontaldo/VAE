# VAE
Following the experiments in "Variational Autoencoders and Nonlinear ICA: A Unifying Framework".

Citation:
@misc{khemakhem2020variationalautoencodersnonlinearica,
      title={Variational Autoencoders and Nonlinear ICA: A Unifying Framework}, 
      author={Ilyes Khemakhem and Diederik P. Kingma and Ricardo Pio Monti and Aapo Hyvärinen},
      year={2020},
      eprint={1907.04809},
      archivePrefix={arXiv},
      primaryClass={stat.ML},
      url={https://arxiv.org/abs/1907.04809}, 

Explanation files:

cmd_utils.py :



* Parse command-line arguments for configuring machine learning tasks.
* Generate multiple variants of argument configurations by appending random seeds.
* Ensure that datasets required by configurations are created beforehand.
* Divide configurations into CPU and GPU workloads for efficient resource allocation.