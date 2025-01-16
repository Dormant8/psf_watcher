work in progress...

# Usage
$py psf_watcher.py <Working psf, copy from directory> <Distiller Directory>] 
Example : py psf_watcher.py .\SVN_ps\8x\mck .\watched_ps
 - ".\SVN_ps\8x\mck" is my working directory where I'm making psf changes
 - ".\watched_ps" is distiller's directory containing in and out folders
 - 2 at the end is an optional parameter.  It is seconds to wait before checking again.  Default=1

watchdog observer executes each cycle of the while loop
sleep time reccomended to be the same or smaller than distiller's sleep time

# requirements
this must be run above 
Acrobat's executable must be on path
Distiller's folders must be default names "in" and "out"
python packages:
  pip install keyboard
  pip install watchdog

# Other docs
https://pdfobject.com/pdf/pdf_open_parameters_acro8.pdf 
https://pypi.org/project/watchdog/#description
https://python-watchdog.readthedocs.io/en/stable/api.html#module-watchdog.observers

# Consider
consider a way to take absolute paths as well, or set up simple gui ( yuk )

# TODO 
confirm argument changes work
confirm pathing logic works
confirm scheduler changes work


