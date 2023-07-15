# Initial setup

## Important documentation links

- [Django docs](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)

## Installation and initial running

- I had set up virtual env and pip installed just django, yesterday. pip list was working normally I think. Today after activating the env, now it says django import error, and pip list is also giving the exception `ImportError: cannot import name 'CacheControlAdapter' from 'pip._vendor.cachecontrol' (unknown location)`

- Google wasn't giving satisfactory results about it, wasn't able to identify exact issue. I temporarily fixed the issue by deleting the entire venv folder and reinstalling django.

- Now a different error is some issue with virtual env and django. I keep getting `ImportError: cannot import name 'execute_from_command_line' from 'django.core.management' (unknown location)` whenever I try to run any django command.

- wow okay wtf. I thought of reinstalling django maybe because I couldn't find 'execute_from_command_line' in the docs? or maybe I didn't search hard enough. But now after uninstalling, when reinstalling I'm getting a completely different error `ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory:'c:\\users\\brian\\code\\summer-of-code-2023\\backend\\venv\\lib\\site-packages\\tzdata-2023.3.dist-info\\METADATA'`. Guess I'll nuke the venv once more and start again.

- The above issues had seem to be resolved by naming the virtual env folder as 'env' instead of 'venv', in hopes of not causeing name collisions with the venv library. Not 100% sure if this was what fixed it, but no issues so far!

- This may be useful occasionally, but the command for clearing pip cache is `py -m pip cache purge` or `pip cache purge`.

## Setting up databases on Windows

- Installed PostgreSQL but their default GUI pgAdmin isn't loading and always has complaints of being slow af. Saw many online recommendations of [DBeaver](https://dbeaver.io/), so I'll be trying that.
