#!/media/GRSync/GRsync/work/dataincubator/milestone_app/venv/bin/python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2008-2014 California Institute of Technology.
# License: 3-clause BSD.  The full license text is available at:
#  - http://trac.mystic.cacr.caltech.edu/project/pathos/browser/dill/LICENSE
"""
use objgraph to plot the reference paths for types found in dill.types
"""
#XXX: useful if could read .pkl file and generate the graph... ?

import dill as pickle
#pickle.debug.trace(True)
#import pickle

# get all objects for testing
from dill import load_types
load_types(pickleable=True,unpickleable=True)
from dill import objects

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print ("Please provide exactly one type name (e.g. 'IntType')")
        msg = "\n"
        for objtype in list(objects.keys())[:40]:
            msg += objtype + ', '
        print (msg + "...")
    else:
        objtype = str(sys.argv[-1])
        obj = objects[objtype]
        try:
            import objgraph
            objgraph.show_refs(obj, filename=objtype+'.png')
        except ImportError:
            print ("Please install 'objgraph' to view object graphs")


# EOF
