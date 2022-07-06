# notes
collection of latex notes, as well as obsidian vaults
Wenhao Zhang ( 2021 ~

### Plan
I plan to work on this "stack" of notes at least two 
times a week, each time an one hour session, main:
- Organize the notes to better shape (clean notes)
- Proof read the notes
- Organize the obsidian vaults for quite searching and linking

### TODO
- [ ] Clean up the Machine Learning scripts in `latex/`
- [ ] A good Makefile for the entire latex note collection

### Latex Rules
##### File and Folder names
Let's use one-level folder structure with each folder containing a self consistent topics. *Folder names contain space with capital letters* for clarity. *For each files, we use underscore*.

##### Latex structure
The main file should produced by gathering each components using `docmute` package, they consist of:
1. Contents of the main body named as `M01_`, where numbers are used if sequence of content is important. 
2. Appendix file named as `A_`
3. Figures named as `F_`
4. Notes under work can be named as `U_`