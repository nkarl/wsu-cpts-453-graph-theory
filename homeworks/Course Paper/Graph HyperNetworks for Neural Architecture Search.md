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

A convolution is traditionally applied on images. However, images in turn can be represented by matrices. Graphs are also represented by matrices. Thus, it is possible to extend convolution to graph.

First we need a graph Laplacian.

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