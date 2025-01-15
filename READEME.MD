work in progress...

# Usage
Example : py psf_watcher.py SVN_ps\8x\mck\extra_all watched_ps\in watched_ps\out 2
 - psf_watcher.py is main.py renamed
 - ...\extra_all is my working directory where I'm making psf changes
 - watched_ps\in is distiller's in directory
 - watched_ps\out is distiller's out directory
 - 2 at the end is an optional parameter.  It is seconds to wait before checking again.  Default=1

navigate to this directory s.t. it can see the things ? check this 
watchdog executes each cycle of the while loop
sleep time reccomended to be the same or smaller than distiller's sleep time

# Packages
pip install keyboard
pip install watchdog

# Other docs
https://pdfobject.com/pdf/pdf_open_parameters_acro8.pdf 
https://pypi.org/project/watchdog/#description
https://python-watchdog.readthedocs.io/en/stable/api.html#module-watchdog.observers
