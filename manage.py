#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    import signal
    import pdb

        # NOTE: This make app breaks to PDB once Ctrl-C pressed
        # signal.signal(signal.SIGABRT, handle_pdb)
        # signal.signal(signal.SIGBREAK, handle_pdb)
    signal.signal(signal.SIGINT,lambda sig, frame: pdb.Pdb().set_trace(frame))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cl.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
