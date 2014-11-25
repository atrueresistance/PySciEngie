Numpy on Yosemite
==================

Ran into multiple issues on freetype
	changed line 961 setupext.py, compiled, and installed. 

data_plot.py appeared to hang when generating the numbers. 

Solution found on Stackoverflow

http://stackoverflow.com/users/1011930/burak-demirtas
Go to matlablib rep by doing  
    cd  ~/.matplotlib/
    fc-list

This will take approximately 2 min and then when you import import matplotlib.pyplot as pl it sould work perfectly. This is the link to github issue and the solution. It seems the bug is related to the fontCache.