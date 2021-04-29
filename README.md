# CP-DSL Replication Package

The CP-DSL provides a set of plugins for Eclipse integration,
an Language Server (LS) implementing the Language Server Protocol (LSP)
and a Jupyter kernel. In the following, we describe how to install
the CP-DSL in Eclipse, Vim, and Juypter. In addition, we provide 
instructions how to setup an experiment with MITgcm.

## Eclipse Setup

The latest Eclipse plugins are hosted at
https://maui.se.informatik.uni-kiel.de/repo/oceandsl/

Whereas the latest snapshot is located in the `snapshot` directory and
releases in the respective release directories.

To install the language support
- open Eclipse
- click on *Help* > *Install New Software...*
  This opens the installer dialog.
- Add a new resource by clicking on *Add...*
- In the then opened dialog enter *cp-dsl* as name and a repository
  URL, e.g., https://maui.se.informatik.uni-kiel.de/repo/oceandsl/snapshot
- Click on *Add*
- Now in the installer a feature Configuration DSL is shown, select it.
- Click on *Next >*
- Click on *Finish*
- As our packages are not signed (yet), you may have to confirm installation.

## Vim Setup

For the Vim setup, we use its extension mechanism and a special LSP
plugins (https://github.com/prabirshrestha/vim-lsp).
Its installation is as follows:
- Copy `javassist-3.12.1.GA.jar` and 
  `org.oceandsl.configuration.ide-1.0.0-SNAPSHOT-ls.jar` to a tooling
  directory, e.g., `~/bin` in your home directory.
- Copy the `example.vimrc` to your home folder and rename it to
  `.vimrc`. In case you already have one, you need to merge both
  files accordingly.
- Open the `.vimrc` in an editor and fix the path to the two jar files.
- Create a directory `~/.vim`
- Start `vim`
- Type `:PlugInstall`, this should install all necessary plugin parts.
- Copy the `filetype.vim` to the `~/.vim` directory. This provides
  filetype information to ensure the correct LSP is used.
- You can check the status that the LS is available with `:LspStatus`.

## Jupyter Setup

Jupyter can be run in a docker container or setup natively on a machine.
Here, we describe the native Jupyter setup.

