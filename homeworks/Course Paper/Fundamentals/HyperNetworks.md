#HyperNetworks

A neural network that generates the parameters of another network. A HN is an abstraction, similar to how a phenotype is parametrized by a genotype.

The focus of the *Google paper* is to show that HN is a useful for deep CNN and long RNN as a relaxed form of weight-sharing across layers.

HN can generate non-shared weights for LSTM.

They use a small network to generate weights for a larger network (main net).

> [!info] Review
> - A Main Net: maps some raw inputs to their desired target
> - HyperNet: takes a set of inputs that contain information about the structure of the weights and generates the weight for that layer.

> [!important] CNN and RNN as two ends of a spectrum
> - **RNN imposes weight-sharing across layers**, inflexible and difficult to learn due to *vanishing gradient*.
> - **CNN enjoy the flexibility of not having weight-sharing**, at the *expense of having redundant parameters when the networks are deep*.
>   **HN as a form of relaxed weight-sharing**, therefore strikes a balance between the two ends.

##### a. Static HN: Weight Factorization for Deep CNN
###### Construction
- majority of model params are in  the kernels of convolutional layers
- kernel dimension: $N_{in} \times N_{out}$ filters
	- filter dimension:
$$f_{size} \times f_{size}$$
- network structure:
	- parameters are stored in a matrix
		$$K^j\in \mathbb{R}^{N_{in}f_{size}\times N_{out}f_{size}}$$
	- for each layer $j$, where $j = 1,\dots, D$ where $D$ is the depth of the main net, the HN recevies a layer embedding
	$$z^j\in\mathbb{R}^{N_z}$$
	- written as:
	$$K^j = g(z^j), \forall j=1,\dots,D$$


> [!note] Curse of Dimensionality
> 	Given the sizes of the network, which is composed of matrices of kernels, which in turn are  composed of matrices of filters, it is imperative to represent the network as a graph in the form of a hypernetwork.

> [!important] Linear Projection
> The matrix $K^j$ can be broken down as $N_{in}$ slices of a smaller matrix with dimensions
> $$f_{size}\times N_{out}f_{size}$$
> each slice as
> $$K_i^j\in f_{size}\times N_{out}f_{size}$$
>
> **effectively turning the network into a 2-layered linear main net.**
>
> #### 1. Layer 1
> - takes the input vector $z^j$ and *linearly projects* it into the $N_{in}$ inputs, with
> - $N_{in}$ different matrices:
>   $$W_i\in\mathbb{R}^{d\times N_z}$$
>  - bias vectors with $d$ as the size of the hidden layers in the HN:
> 	 $$B_i\in\mathbb{R}^d$$
> 	 - $d$ is fixed to $N_z$ for this paper
> #### 2. Layer 2
> is a linear operation which
> - takes an input vector $a_i$ of size $d$, and
> - *linearly projects* that into $K_i$
> 	- using a common tensor
> 	   $$W_{out}\in\mathbb{R}^{f_{size}\times N_{out}f_{size}\times d}$$
> 	 - and a bias matrix
> 	   $$B_{out}\in\mathbb{R}^{f_{size}\times N_{out}f_{size}}$$
> - the final kernel $K^j$ is a concatenation of every $K_i^j$
> - thus, $g(z^j)$ becomes:
$$
\begin{align}
a_i^j &= W_iz^j + B_i,\cr
K_i^j &= \langle W_{out}, a_i^j\rangle + B_{out}, \cr
K^j &= \left[K_1^j\quad K_2^j\quad \dots\quad K_i^j\quad \dots\quad K_{N_{in}}^j\right]
\end{align}
$$


##### b. Dynamic HN: Adaptive Weight Generation for RNN

The Long Short-Term Memory (LSTM) architecture (Hochreiter & Schmidhuber, 1997) is usually better than the Basic RNN at storing and retrieving information over longer time steps.
