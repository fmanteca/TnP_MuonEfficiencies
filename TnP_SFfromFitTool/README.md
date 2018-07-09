# TnP_SFfromFitTool

#Recipe

1)
in MakePlotsExample.py

replace

plot_path

to the global path of your TnP_SFfromFitTool directory
2) python MakePlotsExample.py

This will create a 'Plots' directory containing 1D efficiencies and fits

#Features be implemented (ordered by priority)

- robust method to check quality of the fit
- make 1D efficiencies with 2 or more samples (can currently only take one sample)
- make 2D map for efficiencies and SF
- make SF jsons 
- initialise list of efficiencies from HistoReader using json as imput (will be used to compare efficiencies with other groups)

