# DBADV

This repository contains the source code for the paper **"Density-Based Clustering for Adaptive Density Variation"**, which has been published at ICDM 2021.

## Requirements

- Python 3.7 (https://www.python.org/)
- NumPy 1.19.2 (https://numpy.org/)
- SciPy 1.6.1 (https://www.scipy.org/)
- scikit-learn 0.24.1 (https://scikit-learn.org/)



## Datasets

- Synthetic datasets can be downloaded from `synthetic_datasets/`

- Real-world datasets can be downloaded from the following list:

​       UCI: <https://archive.ics.uci.edu/ml/index.php>

​       Feature Selection Datasets: <https://jundongl.github.io/scikit-feature/datasets.html>



## Baselines

- DBSCAN: <https://scikit-learn.org/stable/modules/clustering.html>
- OPTICS: https://scikit-learn.org/stable/modules/clustering.html
- HDBSCAN: <https://github.com/scikit-learn-contrib/hdbscan>
- CRAD: <https://github.com/DataMining-ClusteringAnalysis/CRAD-Clustering/>
- DBSCAN-DScale: <https://sourceforge.net/projects/distance-scaling/>
- SpectACl : <https://sfb876.tu-dortmund.de/spectacl/index.html>
- $k$-means: https://scikit-learn.org/stable/modules/clustering.html
- Spectral Clustering: <http://www.vision.caltech.edu/lihi/Demos/SelfTuningClustering.html>
- Self-tuning Spectral Clustering: <http://www.vision.caltech.edu/lihi/Demos/SelfTuningClustering.html>
- Affinity Propagation: https://scikit-learn.org/stable/modules/clustering.html
- Sync: <http://dm.uestc.edu.cn/publication/>



## Demos

Run the code by executing:

`python Demo_Seeds.py` for real-world data set or `python Demo_Shape5.py` for synthetic data set.

## Citation

If you used DBADV in your publication or utilized the implementation from this repository, please cite our paper:

```bibtex
@inproceedings{qian2021dbadv,
  title={Density-based clustering for adaptive density variation},
  author={Qian, Li and Plant, Claudia and Böhm, Christian},
  booktitle={2021 IEEE International Conference on Data Mining (ICDM)},
  pages={1282--1287},
  year={2021},
  organization={IEEE},
  doi={10.1109/ICDM51629.2021.00158}
}
