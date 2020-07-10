#MCDA

This repo contains several methods which can be useful for solving MCDA problems. Maybe someday in future I will rewrite it in appropriate way.


### MCDA methods:
* TOPSIS
* COPRAS
* VIKOR
* PROMETHEE I and II


There are also several wrappers, one for each method. Their purpose is to allow to use unified interface across all methods. Also with this wrappers it's possible to obtain ranking with `scipy.stats.rankdata`.


### Normalization methods:
* Linear
* Max
* Sum
* Vector
* Logarithmic


### Future plans
I am hoping that someday I will partially rewrite this code and get rid off this wrappers and other ugly things.


- [ ] Merge methods in one file or submodule
- [ ] Unify method interfaces, so wrappers become unnecessary
- [ ] Rewrite normalization methods
- [ ] Add more comments, references
