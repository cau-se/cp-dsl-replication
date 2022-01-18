# CP-DSL Replication Package

The replication package for the CP-DSL provides instructions on how to install
CP-DSL and how to use it. Firstly, we address the installation of CP-DSL in 
Eclipse, Vim and Jupyter. Secondly, we provide a how-to for UVic and MITgcm
utilizing the three different editors.

The CP-DSL provides a set of plugins for Eclipse integration,
an Language Server (LS) implementing the Language Server Protocol (LSP)
and a Jupyter kernel. To run any example, only one of the three editor setup
is necessary.

## Sources

- CP-DSL  `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl`
- Replication package `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-replication`
- Jupyter Kernel `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-jupyter-kernel`
- Jupyter LSP `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-jupyter-setup`


# Setup of Editors

## Eclipse Setup

Eclipse is a versatile Integrated Development Environment (IDE) based on Java.
Before you can install the CP-DSL in Eclipse you need to install Eclipse.

- *Installing Java*
  - Most Linux distributions come with packages for Java. Install Java 11 or later.
  - For Windows and Mac, you find installers at
    https://www.oracle.com/java/technologies/downloads/#java11
- *Installing Eclipse*
  - Download Eclipse from the Eclipse website https://www.eclipse.org/downloads/
  - Click on the Download button for *Get Eclipse IDE 2021‑12*, this directs you
    to a download page for the current version of Eclipse. As of today this is
    the 2021-12 edition. Howver, CP-DSL should also work with previous and
    later versions of Eclipse.
  - Click on the Download button for the current version. This should start the
    download and show the donate page, which can be ignored.
  - Wait until the download is complete.
  - Depending on your platform you may have zip, dmg or tar.gz archive.
  - Upack the archive and run the installer within the archive. On Linux this
    can be done with:
    - `tar -xvzpf eclipse-inst-jre-linux64.tar.gz`  (unpack archive)
    - `eclipse-installer/eclipse-inst` (run installer)
  - The installer will present different options of IDE setups. You can choose
    any one of them, as installing CP-DSL later will automatically install all
    dependencies. However, to speed things up, select *Eclipse Modeling Tools*.
  - Start the installation. This may take a while.
  - After downloading, the installer will ask you whether you trust the Eclipse
    certificates. Check both of them and check "Remember accepted certificates".
  - Click on "Trust selected".
  - Click on "Launch" (or terminate and use regular startup options for Eclipse
    from you systems menu)
- *Install CP-DSL*
  - Open Eclipse. If you pressed on "Launch" in the previous step, this will
    automatically happen.
  - Eclipse starts up and asks for a workspace directory. You may take the
    default or use a different name. The documentation will use `eclipse-workspace`
    as the name for the workspace directory.
  - Now Eclipse shows its start screen and we can start to install the CP-DSL
    extension.
  - Click on *Help* and then *Install new Software* menu entry. This opens up
    the Install dialog.
  - Here we need to add the update site for CP-DSL. Therefore, click on
    *Add ...* button on the ride side. This allows us to add a new repository.
  - Enter `cp-dsl` as name and `https://maui.se.informatik.uni-kiel.de/repo/oceandsl/snapshot/`
    as URL for the repository.
  - Click on *Add* 
  - Below the row with "Work with:" and the *Add* button, a list appears with
    the entry `Configuration DSL`. Check the checkbox in front and click the
    *Next >* button. `Configuration DSL` comprises of three features for
    `Configuration`, `Declaration` and `Templates`.
  - On the next page of the installation dialog these three features are shown.
  - Click on *Finish* to download them.
  - Now a *Security Warning* pops up indicating that our packages are not signed.
    Unfortunately, this is still true, as the signing process is not trivial,
    but will be fixed in future releases.
  - To proceed with clicking on *Install Anyway*.
  - Eclipse will install the extension and ask to restart.
  - Click on *Restart Now*. This ensures that the features are installed
    correctly.
  - Now you are setup.


## Vim Setup

For the Vim setup, we use its extension mechanism and a special LSP
plugins (https://github.com/prabirshrestha/vim-lsp).
Its installation is as follows:
- Install vim, e.g., with `sudo apt install vim`
- Copy `javassist-3.26.0.GA.jar` and 
  `org.oceandsl.configuration.ide-1.0.0-SNAPSHOT-ls.jar` to a tooling
  directory, e.g., `~/bin` in your home directory.
- Copy the `example.vimrc` to your home folder and rename it to
  `.vimrc`. In case you already have one, you need to merge both
  files accordingly.
- Open the `.vimrc` in an editor and fix the path to the two jar files.
- Create a directory `~/.vim`
- Start `vim`
- Type `:PlugInstall`, this should install all necessary plugin parts.
- Exit `vim` with ESC :x (depending on the number of open buffers, you might
  have to do this twice).
- Merge or copy the `filetype.vim` to the `~/.vim` directory. This provides
  filetype information to ensure the correct LSP is used.
- Start `vim` again with a file name ending with `.oconf`, e.g., `example.oconf`
  This will start the LSP. Otherwise the LSP stays inactive.
- You can check the status that the LS is available with `:LspStatus`.
  
  In case the status is offline or exited, some error might have occured.
  One option is that the wrong java version is used. You can check this on
  command line with `java -version`.

  In case the status is online, you are ready to go. Context help is available
  with CTRL-Space, similarily to Eclipse. 

**Notes:**
- Vim only provides editing capabilites. Compilation must be performed
  by a command-line compiler.

## Jupyter Setup

The Jupyter setup requires not only

**Prerequisites**
- Kernel sources `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-jupyter-kernel`
- Docker setup (optional) for Jupyter `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-jupyter-setup`
- LSP for Jupyter `https://github.com/krassowski/jupyterlab-lsp`
- JuypterLab

Jupyter can be run in a docker container or setup natively on a machine.
For this use the docker setup. However, to run the system in your own
Jupyter installation, you can follow the steps below.

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
        "argv": ["java", "-cp", "javassist-3.26.0-GA.jar", "-jar", "org.oceandsl.configuration.ide-1.0.0-SNAPSHOT-ls.jar"],
        "languages": ["oconf"],
        "mime_types": ["text/oconf", "text/x-oconf"]
      }
```

Please note that Jupyter needs the fully qualified path to the two
referenced files `javassist-3.26.0.GA.jar` and 
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

# Setup of Scientific Models

We use two Earth System Climate Models as case studies for the CP-DSL.
In the following we instruct how to use them.

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
- You can now manipulate settings for the example.
- Save the file. This generates the necessary configuration files.
- You can now compile the project following the instructions in the
  tutorial's README file.

## UVic Project Setup

UVic is a Earth System Climate Model (ESCM) from the University of
Victoria Canada. It can be obtained at http://terra.seos.uvic.ca/model/

To get the code you have to request access to the code from the
public model contact (email address available on the website of the
model). 

Download the code and extract it into a folder. UVic does not come
with a set of test and example configurations. Thus, you have to
use the one provided in this replication package. Lets assume
your model resides in `uvic-model/uvic-run-1`.

- Open Eclipse with a clean workspace.
- Create a new project that should reside in
  `uvic-model/uvic-run-1`
- You can now copy the `uvic.oconf` file from the replication package
  to the project.
- Open the file in Eclipse. Eclipse might ask you to add the XText
  nature, please do so. In case the `uvic.oconf` is opened in a plain
  text editor, choose *Open with ...* to select the right editor.
- You can now manipulate settings for the example.
- Save the file. This generates the necessary configuration files.
- You can now compile the project following the instructions in the
  respective `uvic-installation.md`
  
# Utilizing the CP-DSL

Depending on the editor there are some minor differences in how to use the
different editors with the CP-DSL tooling. The prepared specifications and
declaration for UVic and MITgcm can be found in this repository/archive in the
`projects` directory.

## Using Eclipse 

We will illustrate how to use Eclipse with the UVic case study. However, most
steps are identical for the MITgcm setup. Differences will be noted below.

- Startup Eclipse with the installed CP-DSL (see above)
- Click on *File* > *Import...*
- This opens the *Import Wizard*
- Click on the arrow or plus sign informt of the entry *General*
- Select *Existing Projects into Workspace*
- Click *Next>*
- This opens the *Import Projects* dialog
- Click on the *Browse...* button to select the directory of the UVic project.
- This opens a file dialog.
- Navigate to the `cp-dsl-replication/projects/` directory.
- Select `UVic` and click *Open*.
- Now there should be one project listed under projects.
- Click *Finish*
- If the welcome pane is still shown, close it by clicking on the X new the
  label *Welcome*.
- Now you should see the IDE with a *Model Explorer* and an *Outline* on the
  left, a large empty area (for the editor) and a *Properties* and *Problem*
  view at the bottom.
- Click in the *Model Explorer* on the arrow/plus sign in front of the word
  UVic. This unfolds the project and you can see 4 files labeled:
  - configuration.oconf
  - control.in.template
  - mk.in.template
  - uvic.decl 
  There might also be a `src-gen` folder. Ignore that for now.
- Double clicking on `configuration.oconf` open the editor for the 
  configuration and parameter selection editor of the CP-DSL. Here you can
  explore the settings we currently use with UVic.
- The file uvic.decl contains the declaration of all features, settings and
  parameters UVic has.
- The files `control.in.template` and `mk.in.template` contain the templates
  for the `control.in` and `mk.in` files used to configure UVic.
- To translate the `configuration.oconf` into a valid UVic setup, you can either
  build the project under the menu *Project* > *Build Project* (which might
  be grayed out when the IDE is set to automatically build the project) or
  by opening `configuration.oconf`, editing something (e.g., adding one white
  space) and saving again (Ctrl-S) which triggers the automatic build.
- The generated files can be found in `src-gen`.

MITgcm can be imported in the same way. However, the MITgcm project contains
multiple oconf files. The translate in different subdirectories under src-gen.


