
# Describing multi-electron systems
### General considerations
##### Single electron
For an single electron, its wavefunction can be described by the principle quantum number $n$, orbital angular moment index $l$ and angular momentum along the z axis $m_l$

For spin part, the spin is given by spin angular momentum index $s$ and its value along z-axis $m_s$

The orbital and spin angular momentum are given by the expression $M = \hbar \sqrt{l(l+1)}$

##### Multiple electron 
Angular part: the addition of angular momentum from multiple electron are specified by $L$ and $M_L$, where $L=|l_1 - l_2|,\cdots,(l_1 + l_2)$ and $M_L$ can have $(2L + 1)$ values

Spin part: the addition of spin is given by the same rule of addition of angular momentum with quantum number $S$ and $M_S$. Specifically, for odd number of electrons, $S = \frac{1}{2},\frac{3}{2},\frac{5}{2},\cdots$, For even number of electrons: $S = 0, 1, 2,\cdots$. The case of S = 1/2 correspond to 1 electron system.

Total: Combining both the spin momentum and the angular momentum, we define the total angular momentum quantum number $J$, which take the value $(L+S),\cdots,|L-S|$. $M_J$ denotes the component along the z axis.

##### Spin Orbital coupling (LS coupling)
For the configurations with the same value of L and S, their energy could be different as a result of spin orbital coupling

### Term symbols and Hund's rule
##### Symbols
Term symbol are symbols denoting multielectron configuration and is written by:  $^{2S+1}L_J$. we call $(2S+1)$ the *multiplicity of the term*. 

When $(2S+1) = 1, 2, 3, \cdots$, we call the configuration “singlet”, “doublet”, “triplet” ..., for different L, we can replace it with different symbols according to its value: $L = 0, 1, 2, 3, 4$ are called $S$ term, $S$ term, $D$ term, $F$ term, $G$ term

The term symbol uniquely specifies the angular momentum quantum number of the combined system, and it is often used optical absorption

##### Hund’s rule
With LS coupling (also known as [Russell-Saunders coupling](https://www.tau.ac.il/~tsirel/dump/Static/knowino.org/wiki/Russell-Saunders_coupling.html)), the energy of different configuration can be determined by the following rule:
1. The term with the highest spin multiplicity has the lowest energy. i.e. highest $S$
2. If two or more terms have the same spin multiplicity, the term having the highest value of $L$ has the lowest energy
3. For terms having the same multiplicity and the same values of $L$. The level with the lowest value of $J$ is the lowest in energy if the sub-level is less than half-filled. The level with the highest value of $J$ is the more stable one if the sub-level is more than half-filled. If the level is half-filled, $L$ must be zero and $J = S$

### Example of denoting electronic configurations
##### Single electron $s^1$
For single electron in $s$ orbital, we only have two possible microstate, with electron spin up or down. This gives $L = 0; S = 1/2$. The only allowed value for $J$ is 1/2. Therefore, we write the term symbol as: $^2S_{1/2}$
![[term symbol one electron.png]]

##### Two electrons in $s$ orbital $s^2$
For two electrons occupying the $s$ orbital, their spin is necessary opposite. Therefore, $L = 0; S = 0; J = 0$ and we have the term symbol: $^1S_0$
![[term symbol two electrons.png]]

##### One electron in $p$ orbital $p^1$
The single electron could be in one of the $p$ states (+1, 0, -1), in all case, $L=1$. Spin can only be -1/2 or 1/2 and therefore $S = 1/2$. However, the value for $J$ can be either 1/2 or 3/2. Therefore, the term symbol for this configuration can be $^1P_{3/2}$ or $^1P_{1/2}$. 
![[term symbol one electron in p.png]]

Accoding to the Hunds rule, we can determine the relatively energy of different configurations and the ground state configuration will be $^1P_{1/2}$

##### Two electrons in $p$ orbital $p^2$
We have in total 15 configuration, as shown in the following table. The term table is: 
- Configurations with $L=2; S=0$ is denoted as $^1D_2$
- Configurations with $L=1; S=1$ can de denoted $^3P_2;^3P_1;^3P_0$
- Configurations with $L=2; S=0$ is specified by $^1S_0$

According to the Hund rule, the energy ordering is $^3P_0$ < $^3P_1$ < $^3P_2$ < $^1D_0$ < $^1S_0$
![[term symbol two electrons in p.png]]
