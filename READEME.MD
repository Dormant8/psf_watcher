# Usage
$py psf_watcher.py <Working/psf directory> <Distiller Directory> [<seconds sleep=1>]
Example : py psf_watcher.py .\SVN_ps\8x\mck .\watched_ps 2
 - ".\SVN_ps\8x\mck" is my working directory where I'm making psf changes
 - ".\watched_ps" is distiller's directory containing "in" and "out" folders
 - "2" at the end is an optional parameter.  It is seconds to wait before checking again.  Default=1

".\" is optional at the start of the parameters.  "SVN_ps\8x\mck" and "watched_ps" would work just as well
sleep time reccomended to be the same or smaller than distiller's sleep time

# requirements
script must be ran higher in the directory heirarchy than both your working and distiller directories
Acrobat's executable must be on your path env var
Distiller's folders must be default names "in" and "out"
python packages:
  pip install watchdog

# Other docs
https://pdfobject.com/pdf/pdf_open_parameters_acro8.pdf 
https://pypi.org/project/watchdog/#description
https://python-watchdog.readthedocs.io/en/stable/api.html#module-watchdog.observers

# Consider
consider a way to take absolute paths as well, or set up simple gui ( yuk )
clean up how paths are assigned... ( @ paths list... ) 

# TODO 
