# CP-DSL Replication Package

The CP-DSL provides a set of plugins for Eclipse integration,
an Language Server (LS) implementing the Language Server Protocol (LSP)
and a Jupyter kernel. In the following, we describe how to install
the CP-DSL in Eclipse, Vim, and Juypter. In addition, we provide 
instructions how to setup an experiment with MITgcm.

## Prerequisites

- Install Java 11 or newer
- A Python installation

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

**Prerequisites**
- Kernel sources `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-jupyter-kernel`
- LSP sources `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl`
- Docker setup for Jupyter `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-jupyter-setup`

Jupyter can be run in a docker container or setup natively on a machine.
We use the LSP extension for Jupyter which can also be found here:
`https://github.com/krassowski/jupyterlab-lsp`

For the Juypter setup we have three prerequisites:
- The language server for the CP-DSL
- The language kernel to compile CP-DSL artifacts which sources can be
  found here `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-jupyter-kernel.git`
- JupyterLab

For the general Jupyter setup including LSP support, please follow
the instructions in the following referenced documentation:

`https://jupyterlab-lsp.readthedocs.io/en/latest/Installation.html`

The installation of a language server is explained here:

`https://jupyterlab-lsp.readthedocs.io/en/latest/Configuring.html#language_servers`

To add a language server, you need to add a block of JSON configuration
code in `./jupyter_server_config.json`

```
"oconf": {
        "version": 2,
        "argv": ["java", "-cp", "javassist-3.12.1.GA.jar", "-jar", "org.oceandsl.configuration.ide-1.0.0-SNAPSHOT-ls.jar"],
        "languages": ["oconf"],
        "mime_types": ["text/oconf", "text/x-oconf"]
      }
```

Please note that Jupyter needs the fully qualified path to the two
referenced files `javassist-3.12.1.GA.jar` and 
`org.oceandsl.configuration.ide-1.0.0-SNAPSHOT-ls.jar`.

The language kernel must be placed in `share/jupyter/kernels` depending
on your Jupyter installation location. Create a new directory there
named `oconf` and create `logback.xml` in that place. Our default
content for the `logback.xml` is:

```
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
   <property value="path/to/log/file.log" name="HOME_LOG"/>
   <appender name="FILE-ROLLING" class="ch.qos.logback.core.FileAppender">
      <file>${HOME_LOG}</file>
      <encoder>
         <pattern>%date %level [%thread] %logger{10} [%file:%line] %msg%n</pattern>
      </encoder>
   </appender>
   <root level="debug">
      <appender-ref ref="FILE-ROLLING"/>
   </root>
</configuration>
```

Please change `path/to/log/file` to an appropriate name and location.

Create the `kernel.json` file an fill it with following content:
```
{
   "argv": ["path/to/cp-dsl-jupyter-kernel/bin/cp-dsl-jupyter-kernel", "{connection_file}" ],
   "display_name": "Configuration and Parametrization",
   "language": "oconf"
}

```
Place the file in your `share/jupyter/kernels/oconf/` directory.
Please adapt `path/to/` to the location of the jupyter kernel directory.

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

