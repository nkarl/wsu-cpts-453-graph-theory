#Graph-HyperNetwork #GHN #Neural-Architecture-Search #NAS

## TODO
---
- [ ] Graph Neural Networks (GNN)
- [ ] HyperNetworks (HN)


- **G**raph **H**yper-**N**etworks (GHN) predicts the performance of any unseen neural networks by operating their *computational graph representations*.

- GHN can be generalized and applied to *anytime-prediction*, and outperform existing manually designed models.

## Prerequisite
##### Graph Neural Networks (GNN)
- [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/)
- [Understanding Convolutions on Graphs](https://distill.pub/2021/understanding-gnns/)

##### HyperNetworks (HN)
A neural network that generates the parameters of another network. A HN is an abstraction, similar to a phenotype is parametrized by a genotype.

The focus of the *Google paper* is to show that HN is a useful for deep CNN and long RNN as a relaxed form of weight-sharing across layers.

HN can generate non-shared weights for LSTM.

They use a small network to generate weights for a larger network (main net).

> [!info] Review
> - A Main Net: maps some raw inputs to their desired target
> - HyperNet: takes a set of inputs that contain information about the structure of the weights and generates the weight for that layer.



## PAPER
---
- [ ] Plan out the structure of the paper
	- [ ] Narrative paper
	- [ ] Limit: 5 pages
