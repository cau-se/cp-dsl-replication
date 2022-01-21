# CP-DSL Limitations

The current available snapshot editor release and the herein contained LSP
editors and executables have a set of limitations and bugs, which we are working
on, but remain in the current release.

A up-to-date list of issues can be found here:
https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl/-/issues

## Eclipse Editor

- Checks for type compatibility insufficient: Users can assign single values
  to an array typed parameter without an error message.

- Context help does not work: Currently displaying context help for parameters
  does not work.

## Templates

- The current template examples do not handle single array values or ranges
  correctly und all circumstances. The template must be extended accordingly.

## Jupyter Kernel

Currently, the Jupyter-kernel project does produce an executable Jupyter-kernel.

## Command line compiler

The command line compiler project does not produce an executable program.




