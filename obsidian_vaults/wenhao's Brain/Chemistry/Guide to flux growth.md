# Beginner's guide to flux crystal growth
This is the book note from Tachibana's book, I focus on experimental techniques and growth mechanism, but ignored the phase diagram part. 

More information can be found in the book, for example:
- detail listing of typical flux for oxide or intermetallic system
- crucible and their properties
- details for furnace, and preparation of silica tubes.

### Mechanism of crystal growth
##### Morphology
The shape of the crystal depend on the crystal structure and the composition. 

According to the Bravais principle [ref](https://www.oxfordreference.com/view/10.1093/oi/authority.20110803095525101), the *crystal faces* are most likely to come from the most densely populated lattice planes.  Other than the lattice plane, direction of the chemical bonds also plan an important role in determining the shape of the growth crystal.

Other than crystal faces, the *habit* of the crystal (needle-like, plate-like) also affect the usage of the grown crystal. A change in habit modify the shape of the obtained crystal but does not change the face vectors. In a typical crystal growth, *fast growing face* disappear and the slowest growing face determines the final crystal habit.

##### Nucleation
The most important concept in flux growth is supersaturation which provide the driving force of nucleation. 

In a supersaturated solution, the solid is thermodynamically stable but require nucleation process to kick off the growth process. Atoms or moleculars move about randomly in a meta-stable, supersaturated solution and form clusters. In such process, we consider the change of total energy due to two factors:
1. Energy gain from forming stable solid phase ($r^3$)
2. Energy loss (increase in energy) when new surface is formed ($r^2$)

When the size of the formed solid cluster is small small, surface energy dominants so we only have net increase in energy, it is not utill a critical radius where the total energy start decreasing by forming clusters. 

With high supersaturations, gathering of more particles is encouraged and some clusters can reach the critical radius and become stable nuclei. This process is called *homogenerous nucleation*.

In real situation, most of the nucleation happens in *heterogeneous nucleation*, where nucleation happens on external substances, such as walls of dust particles.

Subsequent crystal growth does not require high supersaturations, therefore after the initial nucleation, crystal growth usually take place at low supersaturation to prevent the formation of additional nuclei formation.

##### Layer by layer growth
In layer by layer growth, the solute particle reaching the crystal surface and combine to form some *growth units* that are loosely absorbed on the surface. These units move along the surface to find suitable site for attachment. such as kinks or edges. In this case, the starting of nucleation of a new layer is the bottleneck, and require high supersaturation. 

The supersaturation of crystal at the corner of edges of a crystal is usually than in the face center, therefore, in a layer by layer growth, it is more common for a new layer to start at the edges and corners of a crystal face, than spread to the center. If the resulting crystal has uneven surface on a face because of the fast growth at the edges or corners, the resulting crystal is called *hopper crystal*.

Finally, in very high supersaturation, the crystal edge or corner growth much faster than the crystal face, resulting in *dendritic growth*.

At lower supersaturation, the *spiral growth* is dominant in which a screw dislocation provides a permanent step on the crystal surface. 

In summary, crystal with flat, smooth faces are grown when the supersaturation is kept low in the solution.

### Choosing a flux
##### Desired properties of a flux
The follows are some desired properties of a good flux
1. The flux has a high solubility for the solute, an appreciable change in solubility with temperature, and does not form a compound or solid solution with the solute
2. The flux has a low melting point
3. The flux has low volatility at growth temperatures
4. The flux has low viscosity at growth temperatures
5. The flux does not react with the crucible
6. The flux can easily separated from grown crystals
7. The flux has low toxicity
8. The flux is available in pure form at low cose 


>The flux has a high solubility for the solute, an appreciable change in solubility with temperature, and does not form a compound or solid solution with the solute

The dissolving power of a flux comes from its *ability to weaken the chemical bonds* that exist between the solute ions. For example, if the main bonding force of the compound is Coulomb interaction, than the flux must also be ionic. 

Frequently, a *useful flux forms a stable compound with the solution at lower temperature*, which usually indicate a high dissovling power. The strength of solute-flux interaction also controls the temperature dependence of solubility, which must change reasonably upon cooling. 

A large difference in ionic radius is usually effective in limiting solid solubility and prevent the formation of solid solution. For example, large ions (Pb, Bi) or small ions (B)

>The flux has low viscosity at growth temperatures

In practice, an ideal flux should have viscosity in the range of 1-10 cP to help transport the solute.

>The flux can easily separated from grown crystals

This can be accomplished if water or other reagent dissolves the flux without attacking the crystal.

##### Other considerations
1. Often, an optimal flux is often obtained by using a *mixture of compounds*.
2. If one of the typical fluxes is a constituent of the target compound (self-flux), or there is common metal betwen a typical flux and the target compound, that flux should be considered as a strong candidate.

##### Flux for intermetallic compounds:
For intermetallic compounds, flux of elements of simple metals are widely used. Combination of elements are not often to be used as flux for intermetallic compounds. 

If an element in the target compound is a typical flux, that metal elements should be a prime candidate as a self-flux. 

### Equipment and experimental procedures
##### Furnace
Furnace must have a high quality temperature controller. In general, the temperature controller must have a preision better than $0.3 ^{\circ}\text{C}$. 

##### Crucibles
To minimize corrosion, metallic crucible are often used to grow ionic crystals, and ionic crucibles are frequently used to grow metallic crystals.

*Platinum crucibles* are used to grow most oxides. They reacts readily with many elements and non-oxide materials, for example, C, S, Se, Te and it alloy with elements like Pb, Bi, Cu and Sn. 

*Silica glass* is stable against low-melting metals, sulfides, selenides and cholorides, but can be attacked by metaks at high temperature. For samples that react with silica but not with carbon, the inner surface can be coated with a layer of carbon, by heating organic liquid rapidly with a flame at $700 ^{\circ}\text{C}$.

*Alumina* (polycrystalline Al2O3) is often used for the flux growth of intermetallic compounds. It is not attacked by most low-melting-point metals. Alumina crucible can be sealed by gluing together the lid and crucible using alumina cement, which can be applied as regular glue. 

##### Growth
Typical groth involves a heating rate of 200-300 $^{\circ}\text{C}$ per hour to the highest temperature, soaking at the temperature for a period of 2-24 hr, and slow cooling to a specific temperature at the rate between 0.5 - 5 $^{\circ}\text{C}$  per hour. Some finaly temperature should be maintained for a certain period of time if experiment requires decanting the liquid (removing the liquid) at the end, otherwise, nature cooling inside the furnace with power off is OK.

The soaking temperature should be at least 50 $^{\circ}\text{C}$  above the liquidus temperature, but not too high to reduce adverse effect, such as increased volatility and reactivity. 

To reduce the number of nuclei, Oscillating temperature (10 $^{\circ}\text{C}$ temperature fluctuation in a 10 min period) can be used. It help redissolve the small crystals that nucleate during the initial process, keeping only the crystal that is large enough. 



