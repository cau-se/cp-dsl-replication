# CP-DSL Replication Package

The replication package for the CP-DSL provides instructions on how to install
CP-DSL and how to use it. Firstly, we address the installation of CP-DSL in 
Eclipse, Vim and Jupyter. Secondly, we provide a how-to for UVic and MITgcm
utilizing the three different editors.

The CP-DSL provides a set of plugins for Eclipse integration,
an Language Server (LS) implementing the Language Server Protocol (LSP)
and a Jupyter kernel. To run any example, only one of the three editor setup
is necessary.

*Note:* We are conducting extensive tests with our case studies that
will show technical issues with the DSL. Therefore, we will provide updates
to the replication package which will be uploaded to Zenodo, accordingly.

Current technical limitations are listed in: `Limitations.md`

## Sources

- CP-DSL  `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl`
- Replication package `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-replication`
- Jupyter Kernel `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-jupyter-kernel`
- Jupyter LSP `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-jupyter-setup`

## The remainder contains
- Setup of the Editors
  - Eclipse Setup
  - Vim Setup
  - Emacs Setup
  - Jupyter Setup
- Utilizing the CP-DSL
  - Using Eclipse

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
  - Click on the Download button for *Get Eclipse IDE 2022‑03*, this directs you
    to a download page for the current version of Eclipse. As of today this is
    the 2022-03 edition. However, CP-DSL should also work with previous and
    later versions of Eclipse.
  - Click on the Download button for the current version. This should start the
    download and show the donate page, which can be ignored.
  - Wait until the download is complete.
  - Depending on your platform you may have zip, exe, dmg or tar.gz archive.
  - Unpack the archive and run the installer within the archive. On Linux this
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
    default or use a different name. The documentation will use standart`eclipse-workspace`
    as the name for the workspace directory, under *home* directory.
  - Now Eclipse shows its start screen and we can start to install the CP-DSL
    extension.
  - Click on *Help* and then *Install new Software* menu entry. This opens up
    the *Install* dialog.
  - Here we need to add the update site for CP-DSL. Therefore, click on
    *Add ...* button on the ride side. This allows us to add a new repository.
  - Enter `cp-dsl` as name under *Name* and `https://maui.se.informatik.uni-kiel.de/repo/oceandsl/snapshot/`
    as URL for the repository under *Location*.
  - Click on *Add* 
  - Below the row with "Work with:" and the *Add* button, a list appears with
    the entry `CP-DSL`. Check the checkbox in front and click the
    *Next >* button. `CP-DSL` comprises of three features for
    `Configuration`, `Declaration` and `Templates`.
  - On the next page of the installation dialog these three features are shown. Plus some not any more required preinstalled packages.
  - Click on *Finish* to download them.
  - Now a *Security Warning* pops up indicating that our packages are not signed.
    Unfortunately, this is still true, as the signing process is not trivial,
    but will be fixed in future releases.
  - To proceed, check the box next to the source and click on *trust selected*.
  - Eclipse will install the extension and ask to restart.
  - Click on *Restart Now*. This ensures that the features are installed
    correctly.
  - Eclipse will try to install the uninstalled not any more needed packages again, just ignore these.
  - Now you are setup.
  - Create a new project in Eclipse or open an existing one and open or create a file name ending with `.oconf`, e.g., `example.oconf`
  This will start the LSP. Otherwise the LSP stays inactive.

## Vim Setup

For the Vim setup, we use its extension mechanism and a special LSP
plugins and Java. Please note, we provide Debian/Ubuntu compatible installation
commands in our documentation. The correct command for your distribution or
operating system may differ.

### Perquisites

- Install Java preferably Java 11.

### Installation
We provide an Python-Script for an easy installation. Just download the `VimSetupScript.py` and run it with `python3 VimSetupScript`.

Alternative manual installation:

- Install the Vim LSP plugin from `https://github.com/prabirshrestha/vim-lsp`
- Install vim, e.g., with `sudo apt install vim`
- Copy `org.oceandsl.configuration.ide-1.0.0-SNAPSHOT-ls.jar` to a tooling
  directory, e.g., `~/bin` in your home directory.
- Copy the `example.vimrc` to your home folder and rename it to
  `.vimrc`. In case you already have one, you need to merge both
  files accordingly.
- Open the `.vimrc` in an editor and fix the path to the jar file.
- Create a directory `~/.vim`
- Start `vim`
- Type `:PlugInstall`, this should install all necessary plugin parts.
- Exit `vim` with ESC :x (depending on the number of open buffers, you might
  have to do this twice).
- Merge or copy the `filetype.vim` to the `~/.vim` directory. This provides
  file type information to ensure the correct LSP is used.
- Start `vim` again with a file name ending with `.oconf`, e.g., `example.oconf`
  This will start the LSP. Otherwise the LSP stays inactive.
- You can check the status that the LS is available with `:LspStatus`.
  
  In case the status is offline or exited, some error might have occurred.
  One option is that the wrong java version is used. You can check this on
  command line with `java -version`. For a more detailed analysis of the error you can check the VimLSP-logs in `~/vim-lsp.log`

  In case the status is running, you are ready to go. Context help is available
  with CTRL-Space, similarly to Eclipse. 

**Notes:**
- Vim only provides editing capabilities. Compilation must be performed
  by a command-line compiler.
  
## Emacs Setup

For the Emacs setup, we use the lsp-mode package and Java. 
As in the Vim Installation, we provide Debian/Ubuntu compatible installation
commands in our documentation. The correct command for your distribution or
operating system may differ.

### Perquisites

- Install the Emacs lsp-mode from `https://emacs-lsp.github.io/lsp-mode/`
- Install Java preferably Java 11.

### Installation

We provide an Python-Script for an easy installation. Just download the `EmacsSetupScript.py` and run it with `python3 EmacsSetupScript`.

Alternative manual installation:
- Install `Emacs` with e.g. `sudo apt update && sudo apt install emacs`
- Run `Emacs` for the first time, so that it can create some standart folder, etc.
- To run `Emacs` within the console, type `emacs -nw` "nw" for "no-window"
- Download the latest version of the OceanDSL Language Server and put it in a folder (ex. `~/bin/`)
- Download the latest oceandsl-mode.el file and place it in i.e. the same folder (`~/bin/`)
edit the path to the jar file, so that it is correct
(make sure to use absolute path ex. `/home/user/bin/example.jar`)
- Merge or use the `init.el` as initial-instruction for `Emacs`
usally it is located at (`~/.emacs.d/init.el` or `~/.emacs`) if it is not there, than just create one.
Make sure, that the path in the init.el is the path to the folder where "oceandsl-mode.el" is located (ex. `~/bin/`)
- Open Emacs
The rest of the instructions use `M-x` as instruction for:
Press `ESC` and then `x` (`M-x`)

- install package lsp: `M-x` type `package-install` ENTER `lsp-mode` ENTER
if `Emacs` shows you ("could not found lsp-mode.[vers-number].tar") type: `M-x` `package-refresh-contents` ENTER
After Installation close `Emacs`

-Usage:
open an OceanDSL file
Just start the lsp-mode with `M-x` `lsp`

The LS should be started and you are good to go.

**Notes:**
- Should lsp-mode show you a bunch of warnings, type: `M-x` `load-library` ENTER `oceandsl-mode` ENTER (you can use tabulator for autocompletion). 
If you cannot use auto-completion you configured the path to `oceandsl-mode.el` in `init.el` wrong.
- As in the Vim installation mentioned: Compilation must be performed by a command-line compiler.

## Jupyter Setup

The Jupyter setup requires a working kernel. Unfortunately, currently the
kernel is not operational. Thus, the setup does not function. We will fix this
issue and provide an update of the replication package.

### Prerequisites
- Kernel sources `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-jupyter-kernel`
- Docker setup (optional) for Jupyter `https://git.se.informatik.uni-kiel.de/oceandsl/cp-dsl-jupyter-setup`
- LSP for Jupyter `https://github.com/krassowski/jupyterlab-lsp`
- JuypterLab

Jupyter can be run in a docker container or directly on a machine.
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
        "argv": ["java", "-cp", "javassist-3.26.0-GA.jar", "-jar", "org.oceandsl.configuration.ide-1.3.0-SNAPSHOT-ls.jar"],
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
Please adapt `path/to/` to the location of the Jupyter kernel directory.

# Setup of Scientific Models

We use two Earth System Climate Models as case studies for the CP-DSL.
In the following we instruct how to use them.

## MITgcm Installation

MITgcm is a Earth System Climate Model (ESCM) available from 
`http://mitgcm.org/`. The documentation can be found at 
`https://mitgcm.readthedocs.io/en/latest/`.

To setup the model, you have to can get the code with:
`git clone https://github.com/MITgcm/MITgcm.git` 

## MITgcm Configuration

MITgcm has a set of prepared configurations in its verification directory.
You can create configuration files for most tutorial project based on the
example configurations, we provide in the projects/MITgcm directory.

See below in **Using Eclipse** how to import the project and generate code.

The generated code has then to be moved to the prepared configuration
directories. Alternatively, you set the Eclipse output directory to your
MITgcm verification directory.

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
declarations for UVic and MITgcm can be found in this repository/archive in the
`projects` directory.

## Using Eclipse 

We will illustrate how to use Eclipse with the UVic case study. However, most
steps are identical for the MITgcm setup. Differences will be noted below.

- Startup Eclipse with the installed CP-DSL (see above)
- Click on *File* > *Import...*
- This opens the *Import Wizard*
- Click on the arrow or plus sign infront of the entry *General*
- Select *Existing Projects into Workspace*
- Click *Next>*
- This opens the *Import Projects* dialog
- Click on the *Browse...* button to select the directory of the UVic project.
- This opens a file dialog.
- Navigate to the UVic project example in the `cp-dsl-replication/projects/`
  directory of the replication package.
- Select `UVic` directory and click *Open*.
- Now the UVic Project should be listed under *Projects*.
- Click *Finish*
- If the welcome pane is still shown, close it by clicking on the X new the
  label *Welcome*.
- Now you should see the IDE with a *Model Explorer* and an *Outline* on the
  left, a large empty area (for the editor) and a *Properties* and *Problem*
  view at the bottom, depending on your Eclipse layout.
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


