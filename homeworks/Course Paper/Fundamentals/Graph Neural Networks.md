#GraphNeuralNetworks #GNN

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

