# PyMCDM

Python 3 library for solving multi-criteria decision-making (MCDM) problems.

___
# Installation

You can download and install `pymcdm` library using pip:

```Bash
pip install pymcdm
```
___
# Available methods

The library contains:
* MCDA methods:

| Acronym          	| Method Name                                                                 	|  Reference 	|
|------------------	|-----------------------------------------------------------------------------	|:----------:	|
| TOPSIS           	| Technique for the Order of Prioritisation by Similarity to Ideal Solution   	|     [1]    	|
| VIKOR            	| VIseKriterijumska Optimizacija I Kompromisno Resenje                        	|     [2]    	|
| COPRAS           	| COmplex PRoportional ASsessment                                             	|     [3]    	|
| PROMETHEE I & II 	| Preference Ranking Organization METHod for Enrichment of Evaluations I & II 	|     [4]    	|
| COMET            	| Characteristic Objects Method                                               	|     [5]    	|
| SPOTIS           	| Stable Preference Ordering Towards Ideal Solution                           	|     [6]    	|
| ARAS             	| Additive Ratio ASsessment                                                   	|    [7,8]   	|
| COCOSO           	| COmbined COmpromise SOlution                                                	|     [9]    	|
| CODAS            	| COmbinative Distance-based ASsessment                                       	|    [10]    	|
| EDAS             	| Evaluation based on Distance from Average Solution                          	|   [11,12]  	|
| MABAC            	| Multi-Attributive Border Approximation area Comparison                      	|    [13]    	|
| MAIRCA           	| MultiAttributive Ideal-Real Comparative Analysis                            	| [14,15,16] 	|
| MARCOS           	| Measurement Alternatives and Ranking according to COmpromise Solution       	|   [17,18]  	|
| OCRA             	| Operational Competitiveness Ratings                                         	|   [19,20]  	|
| MOORA            	| Multi-Objective Optimization Method by Ratio Analysis                       	|   [21,22]  	|

* Weighting methods:
  * Equal weights
  * Entropy method
  * Std method
  * MEREC method
  * CRITIC method
  * CILOS method
  * IDOCRIW method
  * Angle method
  * Gini method
 
 
* Normalization methods:
  * Linear
  * Max
  * Sum
  * Vector
  * Logarithmic
  * Linear
  * Nonlinear
  * Enhanced accuracy


* Correlation coefficients:
    * Spearman
    * Pearson
    * Weighted Spearman
    * Rank Similarity Coefficient
    * Kendall Tau
    * Goodman and Kruskal Gamma


* Helpers
    * rankdata
    * rrankdata
  

### References

[1] Hwang, C. L., & Yoon, K. (1981). Methods for multiple attribute decision making. In Multiple attribute decision making (pp. 58-191). Springer, Berlin, Heidelberg.

[2] Duckstein, L., & Opricovic, S. (1980). Multiobjective optimization in river basin development. Water resources research, 16(1), 14-20.

[3] Zavadskas, E. K., Kaklauskas, A., Peldschus, F., & Turskis, Z. (2007). Multi-attribute assessment of road design solutions by using the COPRAS method. The Baltic Journal of Road and Bridge Engineering, 2(4), 195-203.

[4] Brans, J. P., Vincke, P., & Mareschal, B. (1986). How to select and how to rank projects: The PROMETHEE method. European journal of operational research, 24(2), 228-238.

[5] Sałabun, W., Karczmarczyk, A., Wątróbski, J., & Jankowski, J. (2018, November). Handling data uncertainty in decision making with COMET. In 2018 IEEE Symposium Series on Computational Intelligence (SSCI) (pp. 1478-1484). IEEE.

[6] Dezert, J., Tchamova, A., Han, D., & Tacnet, J. M. (2020, July). The spotis rank reversal free method for multi-criteria decision-making support. In 2020 IEEE 23rd International Conference on Information Fusion (FUSION) (pp. 1-8). IEEE.

[7] Zavadskas, E. K., & Turskis, Z. (2010). A new additive ratio assessment (ARAS) method in multicriteria decision‐making. Technological and economic development of economy, 16(2), 159-172.

[8] Stanujkic, D., Djordjevic, B., & Karabasevic, D. (2015). Selection of candidates in the process of recruitment and selection of personnel based on the SWARA and ARAS methods. Quaestus, (7), 53.

[9] Yazdani, M., Zarate, P., Zavadskas, E. K., & Turskis, Z. (2019). A Combined Compromise Solution (CoCoSo) method for multi-criteria decision-making problems. Management Decision.

[10] Badi, I., Shetwan, A. G., & Abdulshahed, A. M. (2017, September). Supplier selection using COmbinative Distance-based ASsessment (CODAS) method for multi-criteria decision-making. In Proceedings of The 1st International Conference on Management, Engineering and Environment (ICMNEE) (pp. 395-407).

[11] Keshavarz Ghorabaee, M., Zavadskas, E. K., Olfat, L., & Turskis, Z. (2015). Multi-criteria inventory classification using a new method of evaluation based on distance from average solution (EDAS). Informatica, 26(3), 435-451.

[12] Yazdani, M., Torkayesh, A. E., Santibanez-Gonzalez, E. D., & Otaghsara, S. K. (2020). Evaluation of renewable energy resources using integrated Shannon Entropy—EDAS model. Sustainable Operations and Computers, 1, 35-42.

[13] Pamučar, D., & Ćirović, G. (2015). The selection of transport and handling resources in logistics centers using Multi-Attributive Border Approximation area Comparison (MABAC). Expert systems with applications, 42(6), 3016-3028.

[14] Gigović, L., Pamučar, D., Bajić, Z., & Milićević, M. (2016). The combination of expert judgment and GIS-MAIRCA analysis for the selection of sites for ammunition depots. Sustainability, 8(4), 372.

[15] Pamucar, D. S., Pejcic Tarle, S., & Parezanovic, T. (2018). New hybrid multi-criteria decision-making DEMATELMAIRCA model: sustainable selection of a location for the development of multimodal logistics centre. Economic research-Ekonomska istraživanja, 31(1), 1641-1665.

[16] Aksoy, E. (2021). An Analysis on Turkey's Merger and Acquisition Activities: MAIRCA Method. Gümüşhane Üniversitesi Sosyal Bilimler Enstitüsü Elektronik Dergisi, 12(1), 1-11.

[17] Stević, Ž., Pamučar, D., Puška, A., & Chatterjee, P. (2020). Sustainable supplier selection in healthcare industries using a new MCDM method: Measurement of alternatives and ranking according to COmpromise solution (MARCOS). Computers & Industrial Engineering, 140, 106231.

[18] Ulutaş, A., Karabasevic, D., Popovic, G., Stanujkic, D., Nguyen, P. T., & Karaköy, Ç. (2020). Development of a novel integrated CCSD-ITARA-MARCOS decision-making approach for stackers selection in a logistics system. Mathematics, 8(10), 1672.

[19] Parkan, C. (1994). Operational competitiveness ratings of production units. Managerial and Decision Economics, 15(3), 201-221.

[20] Işık, A. T., & Adalı, E. A. (2016). A new integrated decision making approach based on SWARA and OCRA methods for the hotel selection problem. International Journal of Advanced Operations Management, 8(2), 140-151.

[21] Brauers, W. K. (2003). Optimization methods for a stakeholder society: a revolution in economic thinking by multi-objective optimization (Vol. 73). Springer Science & Business Media.

[22] Hussain, S. A. I., & Mandal, U. K. (2016). Entropy based MCDM approach for Selection of material. In National Level Conference on Engineering Problems and Application of Mathematics (pp. 1-6).
___
# Usage example

Here's a small example of how use this library to solve MCDM problem.
For more examples with explanation see [examples](https://gitlab.com/shekhand/mcda/-/blob/master/examples/examples.ipynb).

```python
import numpy as np
from pymcdm.methods import TOPSIS
from pymcdm.helpers import rrankdata

# Define decision matrix (2 criteria, 4 alternative)
alts = np.array([
    [4, 4],
    [1, 5],
    [3, 2],
    [4, 2]
], dtype='float')

# Define weights and types
weights = np.array([0.5, 0.5])
types = np.array([1, -1])

# Create object of the method
topsis = TOPSIS()

# Determine preferences and ranking for alternatives
pref = topsis(alts, weights, types)
ranking = rrankdata(pref)

for r, p in zip(ranking, pref):
    print(r, p)
```

And the output of this example (numbers are rounded):

```bash
3 0.6126
4 0.0
2 0.7829
1 1.0
```

