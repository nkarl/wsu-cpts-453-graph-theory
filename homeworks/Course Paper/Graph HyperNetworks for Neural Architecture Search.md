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
			- Convolution
				- [ ] [Understanding Convolutions on Graphs](https://distill.pub/2021/understanding-gnns/#extending)
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
			- [x] [Everything you need to know about Graph Theory for Deep Learning](https://towardsdatascience.com/graph-theory-and-deep-learning-know-hows-6556b0e9891b)
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
[[Graph Neural Networks]]

#### 1. HyperNetworks (HN)
[[HyperNetworks]]

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
> 
> *Convolution is essential in preserving the topology of graphs.*

A convolution is traditionally applied on images. However, images in turn can be represented by matrices. Graphs are also represented by matrices. Thus, it is possible to extend convolution to graph.

First we need a graph Laplacian.

## PAPER
---
In recent years, neural networks have increasingly become the go-to modeling method for formulating and solving computationally complex problems of high-dimensionality. In this paper I will attempt to parse out why graphy theory is an essential component of this new generation of solutions.

In this paper I am going to explore a form of graph isomorphism, *topology*. I think this is a very interesting topic, the understanding of which can facilitate solving these high-dimensional problems.

Graphs are the perfect representation for a complex system. A graph is capable of denoting the critical nexuses and the traffic, i.e. input and output at towards and away from these nexuses. Furthermore, graphs are perfect tool to represent the hierarchical structure of a system.

For example, a tree is a very useful graph structure to represent a filtering or aggretating structure.

Another example, a Markov chain can be used to represent a probabilistic decision making model.

The math required for maintaining *topology* between graphs:
- Laplace transformation and Laplacian matrix
- [Convolution](obsidian://open?vault=437-machine-learning&file=notes%2Fmath%2FConvolution)

1. Convolution

Convolution has been adopted widely in the field of machine learning, in neural networks for image processing. At the end of the day, an image can be represented by a matrix. In other words, a matrix is a special kind of graph. An image is a graph with a very regular grid-like structure, where the individual pixels are nodes, and the RGB channel values at each pixel are the node features.

The [convolution](https://www.wikiwand.com/en/Convolution) of $f$ and $g$ is written $f ∗ g$, denoting the operator with the symbol ∗.

It is defined as *the integral of the product of the two functions **after one is reflected about the y-axis and shifted***. As such, it is a particular kind of [integral transform](https://www.wikiwand.com/en/Integral_transform "Integral transform"):
$$
(f * g)(t) := \int_{-\infty}^{\infty} f(\tau)\cdot g(t-\tau)\cdot d\tau
$$

or (due to commutativity):
$$
(f * g)(t) := \int_{-\infty}^{\infty} f(t-\tau)\cdot g(\tau)\cdot d\tau
$$

where **$\boldsymbol{t}$ is the amount at which the function $\boldsymbol{f(\tau)}$ weighted by the function $\boldsymbol{g(-\tau)}$ is shifted**. As $t$ changes, the weighting function $\boldsymbol{g(t-\tau)}$ *emphasizes different parts of the input function* $\boldsymbol{f(\tau)}$:

- **for** $t > 0$:
	- $\boldsymbol{g(t-\tau)=g(-\tau)}$ that shifts by the amount $t$ along the $\tau$-axis towards $+\infty$
- **for** $t < 0$:
	- $\boldsymbol{g(t-\tau)=g(-\tau)}$ that shifts by the amount $|t|$ along the $\tau$-axis towards $-\infty$

> [!note]
> The convolution at node $v$ occurs only with nodes $u$ which are not more than $d$ hops away. Thus, these polynomial filters are localized. The degree of the localization is governed completely by d.
> 
> In other words, *topology is preserved*.

*This extension of convolution to graphs is a breakthrough*, because it allows for the localization of group neurons aggregated together by a distance $d$. The immediate applications are the following graph neural networks:
- Graph Convolutional Networks (GCN)
- Graph Attention Networks (GAT)
- Graph Sample and Aggregate (GraphSAGE)
- Graph Isomorphism Networks (GIN)

2. 


## References
---
- [Graph HyperNetworks for Neural Architecture Search](https://arxiv.org/abs/1810.05749)
- [HyperNetworks](https://openreview.net/forum?id=rkpACe1lx)