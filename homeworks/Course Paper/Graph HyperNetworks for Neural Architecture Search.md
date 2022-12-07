#Graph-HyperNetwork #GHN #Neural-Architecture-Search #NAS

## TODO
---
- [x] Document all references I have collected
	- CORE:
		- Graph Theory:
			- [x] YouTube [Introduction to Graph Theory: A Computer Science Perspective](https://www.youtube.com/watch?v=LFKZLXVO-Dg)
			
		- Graph Neural Networks (GNN):
			- [ ] [Deep Learning For Symbolic Mathematics](https://openreview.net/forum?id=S1eZYeHFDS)
			- [x] [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/)
				- [ ] [Understanding Convolutions on Graphs](https://distill.pub/2021/understanding-gnns/#extending)
			- Convolution
				- [ ] YouTube [But what is a convolution?](https://www.youtube.com/watch?v=KuXjwB4LzSA)
				- [ ] [Convolution & Laplace](https://lpsa.swarthmore.edu/Convolution/ConvLaplace.html)
				- Laplace Transform
					- [ ] [Laplacian](https://mathworld.wolfram.com/Laplacian.html)
					- [ ] [A Short Tutorial on Graph Laplacians, Laplacian Embedding, and Spectral Clustering](https://csustan.csustan.edu/~tom/Clustering/GraphLaplacian-tutorial.pdf)
					- [ ] [Laplace Transform](https://www.wikiwand.com/en/Laplace_transform)
					- [ ] YouTube [Laplace Transform](https://www.youtube.com/watch?v=n2y7n6jw5d0)
			
		- [x] [HyperNetworks](https://openreview.net/forum?id=rkpACe1lx)
		- [x] [Graph HyperNetworks for Network Architectures Search (NAS)](https://arxiv.org/abs/1810.05749)
			
	- Extra:
		- Graph Theory:
			- [ ] [Everything you need to know about Graph Theory for Deep Learning](https://towardsdatascience.com/graph-theory-and-deep-learning-know-hows-6556b0e9891b)
			- [ ] [Graph Convolutional Networks — Explained](https://towardsdatascience.com/graph-convolutional-networks-explained-d88566682b8f)
			- [ ] [Graph Neural Network and Some of GNN Applications: Everything You Need to Know](https://neptune.ai/blog/graph-neural-network-and-some-of-gnn-applications)
			
		- Manifolds & Topology
			- [ ] [Neural Networks, Manifolds and Topology](https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/)
			
		- Markov Chains:
			- [ ] YouTube [Markov Chains: Recurrence, Irreducibility, Classes | Part - 2](https://www.youtube.com/watch?v=VNHeFp6zXKU&list=PLM8wYQRetTxBkdvBtz-gw8b9lcVkdXQKV&index=4)
			
	
- [ ] Read and ranklist which references will be used
- [ ] Plan out the structure of the paper
	- [ ] Narrative paper
	- [ ] Limit: 5 pages


## Prerequisite
---
#### 0. Graph Neural Networks (GNN)

- [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/)
- [Understanding Convolutions on Graphs](https://distill.pub/2021/understanding-gnns/)

*A GNN is a graph where each node is a RNN* that individually sends and receives messages along the edges, spanning the horizon of message passing.

> [!info] node embedding
> - is a way to represent nodes as vectors.
> - captures the topology of the network. Topology deals with meaningful structure, i.e. global geometric structure of the network. This is especially important for very large and complex network composed of a variety of neural networks.


Each node $v$ stores an internal node embedding vector $\boldsymbol{h}_v^{(t)}\in\mathbb{R}^D$, and is updated recurrently:
$$
\boldsymbol{h}_v^{(t+1)} = \cases{
U(\boldsymbol{h}_t^{(t)}, \boldsymbol{m}_v^{(t)}) & if node $v$ is active, \cr
\boldsymbol{h}_v^{(t)} & otherwise.
}
$$

where:
- $U$ is the recurrent cell function (often modeled with **LSTM** or **GRU** (Gated Recurrent Unit)), and
- $\boldsymbol{m}_v^{(t)}$ is the message received by $v$ at time step t:
$$
\begin{align}
&\boldsymbol{m}_v^{(t)} = \sum_{u\in N_{in}(v)} M\left(\boldsymbol{h}_u^{(t)}\right)\cr
\cr
&\text{where:}\cr
&\quad\quad\text{- $M$ is the message function, often modeled with \textbf{MLP}.}\cr
&\quad\quad\text{- $N_{in}(v)$ is the set of neighbors with incoming edges pointing towards $v$.}
\end{align}
$$

Given a graph $A$, we define the GNN operator $G_A$ to be a mapping from a set of initial node embeddings ${\{\boldsymbol{h}_v^{(0)}\}}$ to a set of different node embeddings ${\{\boldsymbol{h}_v^{(t)}\}}$, parametrized by some learnable parameters $\phi$:
$$
\left\{\boldsymbol{h}_v^{(t)}|v\in V\right\} =
G_A^{(t)}\left(\left\{\boldsymbol{h}_v^{0}|v\in V\right\}, \phi\right)
$$
Throughout propagation the node embeddings $\boldsymbol{h}_v^{(t)}$ continuously aggregate graph level information, which can be used for:
- node prediction
- graph prediction by further aggregation

**GNN are learned using backpropagation through time**, similar to RNN.

Represented as a **directed acyclic graph**:
$$
\begin{align}
&A = (V, E)\cr
\cr
&\text{where:}\cr
&\quad\text{- each node $v\in V$ is associated with}\cr
&\quad\text{- a computational operator $f_v$ parametrized by $w_v$, which}\cr
&\quad\quad\text{- produces an output activation tensor $x_v$}\cr
&\quad\text{- edges $e_{u\to v}\in E$ denote the flow of activation tensors from node $u$ to node $v$}\cr
&\quad\text{- the output $x_v$ is computed by}\cr
&\quad\quad\text{- applying associated $f_v$ on each of its inputs, and}\cr
&\quad\quad\text{- taking the summation:}\cr
\cr
&\quad\quad\quad\quad\quad x_v = \sum_{e_{u\to v}\in E} f_v(x_u, w_v), \forall v\in V
\end{align}
$$


#### 1. HyperNetworks (HN)

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

#### 2. Graph HyperNetworks for Network Architectures Search (NAS)

- **G**raph **H**yper-**N**etworks (GHN) predicts the performance of any unseen neural networks by operating their *computational graph representations*.
- GHN can be generalized and applied to *anytime-prediction*, and outperform existing manually designed models.
- Traditional NAS is expensive since **Stochastic Gradient Descent is expensive**.
- **A trained HN is well correlated with Stochastic Gradient Descent**, and thus can surrogate the weight generation for the main network.

In this work,
- we advocate for a *computation graph representation* as it *allows for the topology of an architecture to be explicitly modeled*.
- Furthermore, it is *intuitive to understand* and can be *easily extensible to various graph sizes*.

##### Prerequisites
- [[#0. Graph Neural Networks (GNN)|Graph Neural Networks (GNN)]]
- [[#1. HyperNetworks (HN)|Graph HyperNetworks (HN)]]

#### 4. Convolution on Graphs

> [!note]
> This is a core mathematic method in some models.



## PAPER
---
In recent years, neural networks have increasingly become the go-to modeling method for formulating and solving computationally complex problems of high-dimensionality. In this paper I will attempt to parse out why graphy theory is an essential component of this new generation of solutions.

Graphs are the perfect representation for a complex system. A graph is capable of denoting the critical nexuses and the traffic, i.e. input and output at towards and away from these nexuses. Furthermore, graphs are perfect tool to represent the hierarchical structure of a system.

For example, a tree is a very useful graph structure to represent a filtering or aggretating structure.

Another example, a Markov chain can be used to represent a probabilistic decision making model.


## References
---
- [Graph HyperNetworks for Neural Architecture Search](https://arxiv.org/abs/1810.05749)
- [HyperNetworks](https://openreview.net/forum?id=rkpACe1lx)