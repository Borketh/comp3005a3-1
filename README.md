# this thingy

This is a small demo project for a university course. 
If you see this while it's public... no you don't!

## For the TA

Tools needed:
 
- Python 3.13
- Docker, with Compose (included in modern builds)
- Poetry (python package manager)

Everything else will be taken care of by the latter two.

First step: be in the directory this file is in. 

To set up the database and pgAdmin (this is irrelevant but useful to me), run the `setup.sh` script.
**You will need superuser permission** (or admin permission on windows? no idea.) unless you have set up 
rootless docker on your system (if you don't know what that means, you haven't).

Then, you can run the program with `python comp3005a3/main.py`. Hit enter to go through 
all the demonstration steps.

To shut down the database, run the `teardown.sh` script, again with root permissions.

If you want to get all of this off your system now that you're done, 
- `sudo docker system prune -af` 
- uninstall docker
- delete the .venv directory (or all of this project)
- uninstall poetry
