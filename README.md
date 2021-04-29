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


## MITgcm Project Setup

MITgcm is a Earth System Climate Model (ESCM) available from 
`http://mitgcm.org/`. The documentation can be found at 
`https://mitgcm.readthedocs.io/en/latest/`.

To setup the model, you have to can get the code with:
`git clone https://github.com/MITgcm/MITgcm.git` 

Now you can select an example model. We recommend to use a mode from
the tutorial, e.g.,
`https://mitgcm.readthedocs.io/en/latest/examples/barotropic_gyre/barotropic_gyre.html`

Therefore, switch to `verification/tutorial_barotropic_gyre/` inside the
`MITgcm` code base.
Before continuing with OceanDSL's CP-DSL, you can have a look at the
setup files in `input` and `code` sub-directories of the example.

For the CP-DSL, you must create a `configuration.oconf` file in the
examples model directory. Lets assume this should be done in Eclipse.

- Open Eclipse with a clean workspace.
- Create a new project that should reside in
  `verification/tutorial_barotropic_gyre/`
- You can now copy the `barotropic_gyre.oconf` file to the project.
- Open the file in Eclipse. Eclipse might ask you to add the XText
  nature, please do so. In case the `barotropic_gyre.oconf` is opened
  in a plain text editor, choose *Open with ...* to select the right
  editor.
- You can no manipulate settings for the example.
- Save the file. This generates the necessary configuration files.
- You can now compile the project following the instructions in the
  tutorial's README file.

