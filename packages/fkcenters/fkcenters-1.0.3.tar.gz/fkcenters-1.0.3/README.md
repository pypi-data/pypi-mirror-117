Python implementations of the FuzzykCenters algorithms for fuzzy clustering categorical data:

## Installation:
### Using pip: 
```shell
pip install fkcenters
```

### Import the packages:
```shell
from FkCenters.FkCenters import FkCenters
from FkCenters import TDef
import numpy as np
```
### Generate a simple categorical dataset:

```shell
X = np.array([[0,0,0],[0,1,1],[0,0,0],[1,0,1],[2,2,2],[2,3,2],[2,3,2]])
y = np.array([0,0,0,0,1,1,1])
```

### LSHk-Representatives (Init): 

```shell
algo = FkCenters(X,y ,k=TDef.k, alpha=TDef.alpha)
algo.SetupMeasure("Overlap")
algo.DoCluster()
algo.CalcScore()


```

### Built-in evaluattion metrics:
```shell
algo.CalcFuzzyScore()
```

### Outcome:
```shell
SKIP LOADING distMatrix because: True bd=None yellow
Saving Overlap to: saved_dist_matrices/json/Overlap_None.json
Purity: 1.00 NMI: 1.00 ARI: 1.00 Sil:  0.59 Acc: 1.00 Recall: 1.00 Precision: 1.00
Fuzzy scores PC:1.00 NPC:1.00 FHV↓:0.02 FS↓:-2000.00 XB↓:0.11 BH↓:0.06 BWS:-2000.00 FPC:3.50 SIL_R:0.70 FSIL:0.70 MPO:12.15 NPE:0.01 PE:0.01 PEB:0.01
```

## Parameters:
X: Categorical dataset\
y: Labels of object (for evaluation only)\
n_init: Number of initializations \
n_clusters: Number of target clusters\
max_iter: Maximum iterations\
verbose: \
random_state: 

If the variable MeasureManager.IS_LOAD_AUTO is set to "True": The DILCA will get the pre-caculated matrix
 
## Outputs:
cluster_representatives: List of final representatives\
labels_: Prediction labels\
u: Fuzzy membership
cost_: Final sum of squared distance from objects to their centroids\
n_iter_: Number of iterations

## References:
T. N. Mau and V. -N. Huynh, ``Kernel-Based k-Representatives Algorithm for Fuzzy Clustering of Categorical Data," 2021 IEEE International Conference on Fuzzy Systems (FUZZ-IEEE), 2021, pp. 1-6, doi: 10.1109/FUZZ45933.2021.9494597.

