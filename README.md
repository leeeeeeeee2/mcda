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

 Acronym          	| Method Name                                                                 	| Reference  	|
------------------	|-----------------------------------------------------------------------------	|------------	|
 TOPSIS           	| Technique for the Order of Prioritisation by Similarity to Ideal Solution   	| [1]        	|
 VIKOR            	| VIseKriterijumska Optimizacija I Kompromisno Resenje                        	| [2]        	|
 COPRAS           	| COmplex PRoportional ASsessment                                             	| [3]        	|
 PROMETHEE I & II 	| Preference Ranking Organization METHod for Enrichment of Evaluations I & II 	| [4]        	|
 COMET            	| Characteristic Objects Method                                               	| [5]        	|
 SPOTIS           	| Stable Preference Ordering Towards Ideal Solution                           	| [6]        	|
 ARAS             	| Additive Ratio ASsessment                                                   	| [7,8]      	|
 COCOSO           	| COmbined COmpromise SOlution                                                	| [9]        	|
 CODAS            	| COmbinative Distance-based ASsessment                                       	| [10]       	|
 EDAS             	| Evaluation based on Distance from Average Solution                          	| [11,12]    	|
 MABAC            	| Multi-Attributive Border Approximation area Comparison                      	| [13]       	|
 MAIRCA           	| MultiAttributive Ideal-Real Comparative Analysis                            	| [14,15,16] 	|
 MARCOS           	| Measurement Alternatives and Ranking according to COmpromise Solution       	| [17,18]    	|
 OCRA             	| Operational Competitiveness Ratings                                         	| [19,20]    	|
 MOORA            	| Multi-Objective Optimization Method by Ratio Analysis                       	| [21,22]    	|

* Weighting methods:


| Acronym 	| Method Name                                           	|  Reference 	|
|---------	|-------------------------------------------------------	|:----------:	|
| -       	| Equal/Mean weights                                    	|    [23]    	|
| -       	| Entropy weights                                       	| [23,24,25] 	|
| STD     	| Standard Deviation weights                            	|   [23,26]  	|
| MEREC   	| MEthod based on the Removal Effects of Criteria       	|    [27]    	|
| CRITIC  	| CRiteria Importance Through Intercriteria Correlation 	|  [28, 29]  	|
| CILOS   	| Criterion Impact LOS                                  	|    [30]    	|
| IDOCRIW 	| Integrated Determination of Objective CRIteria Weight 	|    [30]    	|
| -       	| Angular/Angle weights                                 	|    [31]    	|
| -       	| Gini Coeficient weights                               	|    [32]    	|
| -       	| Statistical variance weights                          	|    [33]    	|
  
* Normalization methods:

| Method Name                        	| Reference 	|
|------------------------------------	|:---------:	|
| Weitendorf’s Linear Normalization  	|    [34]   	|
| Maximum - Linear Normalization     	|    [35]   	|
| Sum-Based Linear Normalization     	|    [36]   	|
| Vector Normalization               	|  [36,37]  	|
| Logarithmic Normalization          	|  [36, 37] 	|
| Linear Normalization (Max-Min)     	|  [34,38]  	|
| Non-linear Normalization (Max-Min) 	|    [39]   	|
| Enhanced Accuracy Normalization    	|    [40]   	|

* Correlation coefficients:

| Coefficient name                                 	| Reference 	|
|--------------------------------------------------	|:---------:	|
| Spearman's rank correlation coefficient          	|  [41,41]  	|
| Pearson correlation coefficient                  	|    [43]   	|
| Weighted Spearman’s rank correlation coefficient 	|    [44]   	|
| Rank Similarity Coefficient                      	|    [45]   	|
| Kendall rank correlation coefficient             	|    [46]   	|
| Goodman and Kruskal's gamma                      	|    [47]   	|


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

[23] Sałabun, W., Wątróbski, J., & Shekhovtsov, A. (2020). Are mcda methods benchmarkable? a comparative study of topsis, vikor, copras, and promethee ii methods. Symmetry, 12(9), 1549.

[24] Lotfi, F. H., & Fallahnejad, R. (2010). Imprecise Shannon’s entropy and multi attribute decision making. Entropy, 12(1), 53-62.

[25] Li, X., Wang, K., Liu, L., Xin, J., Yang, H., & Gao, C. (2011). Application of the entropy weight and TOPSIS method in safety evaluation of coal mines. Procedia engineering, 26, 2085-2091.

[26] Wang, Y. M., & Luo, Y. (2010). Integration of correlations with standard deviations for determining attribute weights in multiple attribute decision making. Mathematical and Computer Modelling, 51(1-2), 1-12.

[27] Keshavarz-Ghorabaee, M., Amiri, M., Zavadskas, E. K., Turskis, Z., & Antucheviciene, J. (2021). Determination of Objective Weights Using a New Method Based on the Removal Effects of Criteria (MEREC). Symmetry, 13(4), 525.

[28] Diakoulaki, D., Mavrotas, G., & Papayannakis, L. (1995). Determining objective weights in multiple criteria problems: The critic method. Computers & Operations Research, 22(7), 763-770.

[29] Tuş, A., & Adalı, E. A. (2019). The new combination with CRITIC and WASPAS methods for the time and attendance software selection problem. Opsearch, 56(2), 528-538.

[30] Zavadskas, E. K., & Podvezko, V. (2016). Integrated determination of objective criteria weights in MCDM. International Journal of Information Technology & Decision Making, 15(02), 267-283.

[31] Shuai, D., Zongzhun, Z., Yongji, W., & Lei, L. (2012, May). A new angular method to determine the objective weights. In 2012 24th Chinese Control and Decision Conference (CCDC) (pp. 3889-3892). IEEE.

[32] Li, G., & Chi, G. (2009, December). A new determining objective weights method-gini coefficient weight. In 2009 First International Conference on Information Science and Engineering (pp. 3726-3729). IEEE.

[33] Rao, R. V., & Patel, B. K. (2010). A subjective and objective integrated multiple attribute decision making method for material selection. Materials & Design, 31(10), 4738-4747.

[34] Brauers, W. K., & Zavadskas, E. K. (2006). The MOORA method and its application to privatization in a transition economy. Control and cybernetics, 35, 445-469.

[35] Jahan, A., & Edwards, K. L. (2015). A state-of-the-art survey on the influence of normalization techniques in ranking: Improving the materials selection process in engineering design. Materials & Design (1980-2015), 65, 335-342.

[36] Gardziejczyk, W., & Zabicki, P. (2017). Normalization and variant assessment methods in selection of road alignment variants–case study. Journal of civil engineering and management, 23(4), 510-523.

[37] Zavadskas, E. K., & Turskis, Z. (2008). A new logarithmic normalization method in games theory. Informatica, 19(2), 303-314.

[38] Jahan, A., & Edwards, K. L. (2015). A state-of-the-art survey on the influence of normalization techniques in ranking: Improving the materials selection process in engineering design. Materials & Design (1980-2015), 65, 335-342.

[39] Peldschus, F., Vaigauskas, E., & Zavadskas, E. K. (1983). Technologische entscheidungen bei der berücksichtigung mehrerer Ziehle. Bauplanung Bautechnik, 37(4), 173-175.

[40] Zeng, Q. L., Li, D. D., & Yang, Y. B. (2013). VIKOR method with enhanced accuracy for multiple criteria decision making in healthcare management. Journal of medical systems, 37(2), 1-9.

[41] Binet, A., & Henri, V. (1898). La fatigue intellectuelle (Vol. 1). Schleicher frères.

[42] Spearman, C. (1910). Correlation calculated from faulty data. British Journal of Psychology, 1904‐1920, 3(3), 271-295.

[43] Pearson, K. (1895). VII. Note on regression and inheritance in the case of two parents. proceedings of the royal society of London, 58(347-352), 240-242.

[44] Dancelli, L., Manisera, M., & Vezzoli, M. (2013). On two classes of Weighted Rank Correlation measures deriving from the Spearman’s ρ. In Statistical Models for Data Analysis (pp. 107-114). Springer, Heidelberg.

[45] Sałabun, W., & Urbaniak, K. (2020, June). A new coefficient of rankings similarity in decision-making problems. In International Conference on Computational Science (pp. 632-645). Springer, Cham.

[46] Kendall, M. G. (1938). A new measure of rank correlation. Biometrika, 30(1/2), 81-93.

[47] Goodman, L. A., & Kruskal, W. H. (1979). Measures of association for cross classifications. Measures of association for cross classifications, 2-34.
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

