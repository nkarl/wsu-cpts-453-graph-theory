## 1.
---
Give details – two paragraphs will suffice – about your choice for the end-of-semester project.

*I am researching the application of graph theory in neural network models.* I am planning to put together some kind of relationship between the following topics:

- Graph Theory
- Graph Neural Networks
- [HyperNetworks](https://arxiv.org/abs/1609.09106)
- [Graph HyperNetworks for Neural Architecture Search](https://openreview.net/forum?id=rkgW0oA9FX)

In recent years neural network modeling has become increasingly the go-to choice for solving high-dimensional problems which are highly computationally complex. Being able to relate graph theory and neural network is a very important to me in order to begin tackling these problems.

## 2.
---
In the current era, *media beyond written sources* have been effective in communicating complex mathematical ideas to a broad audience. Shining examples of this include YouTube videos such as the 3Blue1Brown videos produced by Grant Sanderson. **Find and provide a short synopsis of two YouTube videos each effectively explaining a problem that involves graph theory**. A “short synopsis” includes ***the URL along with at least two paragraphs*** of explanation and/or narrative.

> [!link] [Markov Chain for Stochastic Decision Making](https://www.youtube.com/watch?v=i3AkTO9HLXo)
> 
> A Markov chain is a probability distribution wherein the next state is dependent only on the previous state, not the entire sequence of previous states.
> 
> A Markove chain is a very useful construct when we need to deal with non-determinism, i.e. stochastic decision making. For example, let's say we want to go on a pizza date, but our favorite restaurant only serve one type of food out of three everyday (pizza, hot dog, and burger). That means each day is different, with a caveat: the food served today is dependent on what is served on the previous day:
> 
> ```mermaid
> graph LR
> pizza -->|0.3| burger
> burger -->|0.6| pizza
> burger -->|0.2| burger
> burger -->|0.5| hotdog
> hotdog -->|0.2| burger
> hotdog -->|0.5| hotdog
> pizza -->|0.7| hotdog
> ```
> 
> Using a Markov chain we can estimate the probability distribution for the three types of food possibly served every day.
> 
> To do that, we map these *states* and their probabilitistic relations to a directed graph, and thus have our Markov chain for this decision making problem. Given a Markov chain mapped to an adjacency matrix (also called a transition matrix), there exists a state vector $\pi$, called the *stationary distribution*, composed of the probability distributions of all nodes in the chain, and is the convergence of all the state vectors $\pi_i$ where $i = 0, 1, \dots N$.
> 
> $$
> \pi\cdot A = \pi
> $$
> 

> [!link] [Mapping of Manifolds to Decision Making](https://www.youtube.com/watch?v=v6VJ2RO66Ag)
> 
> One important property associated with manifolds is *homeomorphism*, which is an isomorphism from some subdivision of a graph $G$ to some subdivision of another graph $G'$. In other words, where the graphic structure is preserved in *isomorphism*, the topological structure is preserved in *homeomorphism*. For example, performing a subdivision (adding a new node) on some edge in graph $G$ should mean that the same action happens on some edge in the graph $G'$ and simultaneously preserve their isomorphic relation, and thus preserving their local topological mapping.
> 
> Another important thing to be noted about manifolds is that high-dimensional topologies are very often mapped to low-dimensional topologies. For example, the topological gradient of a 3D object is a simple point on a 2D plane in space (which can be obtained via a linear transformation). Similarly, some $N$-dimensional manifold mapped out from some $N$ neurons can represent the overall neural activities (i.e. local states in space-time and various biological feedbacks such as temperature, humidity, and so on). This manifold in turn can be localized to a decision making process in Euclidian space. 
> 
> Furthermore, the graph of $N$ neurons are indeed composed of some $M$ subgraphs of related neurons (neurons that are typically in close proximity and activate on the same input). Thus, it could be further be mapped to a sort of hypernetwork of connected components. 
