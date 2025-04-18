# MCreator NeoForge Standalone Packager

This project provides a set of Python scripts to package the necessary runtime files (Java executable, libraries, arguments, built classes/resources) from an MCreator NeoForge workspace into a portable, self-contained directory. The goal is to allow running the MCreator-configured Minecraft instance outside of the MCreator IDE, for example, for testing distribution or running on a different machine (with compatible architecture).

## Features

*   Copies the specific Java runtime bundled with MCreator.
*   Copies required libraries from the MCreator cache and build directories.
*   Copies necessary configuration/argument files (`clientRunVmArgs.txt`, `clientRunProgramArgs.txt`).
*   Copies the compiled mod classes and resources.
*   Prompts for a username and modifies the program arguments file accordingly.
*   Generates an OS-specific launch script (`.sh` or `.bat`) within the package that uses runtime path resolution for portability.
*   Modular code structure (`config.py`, `dependencies.py`, `packaging.py`, `script_generator.py`, `main.py`).

## Prerequisites

*   **Python 3:** Version 3.8 or higher is recommended (due to f-string usage and modern `pathlib` features).
*   **Existing MCreator Workspace:** You need a functional MCreator NeoForge workspace that you can successfully run from within the MCreator IDE. The script reads files directly from this workspace and its associated cache.
*   **MCreator Installation:** The script relies on finding the bundled Java runtime within your MCreator installation directory.

## Configuration

Before running the script, you **must** configure the source paths to match your system setup.

1.  **`config.py`:**
    *   `OUTPUT_BASE_DIR`: Set this variable to the desired path where the packaged output directory will be created (e.g., `./my_mc_package`).

2.  **`dependencies.py`:**
    *   **Crucial:** Verify the paths defined near the top of this file:
        *   `_MC_JAVA_HOME`: Path to the `Home` directory *inside* the MCreator bundled JDK (e.g., `/Applications/MCreator.app/Contents/jdk.bundle/Contents/Home` on macOS).
        *   `_WORKSPACE_BASE`: The parent directory where your MCreator workspaces are stored (e.g., `Path.home() / "MCreatorWorkspaces"`).
        *   `_MCREATOR_CACHE_BASE`: Path to the relevant MCreator Gradle cache directory (usually `~/.mcreator/gradle/caches/modules-2/files-2.1`).
        *   `_WORKSPACE_NAME`: The specific name of the workspace folder you want to package.
        *   `_MOD_PROJECT_SUBDIR`: The subdirectory name within the workspace that contains the `build/moddev` directory (often the mod name, like `packloader`).
    *   **Classpath Conflicts:** This file also contains the `CLASSPATH_SOURCES` list. If you encounter Java module errors (`ResolutionException`) when running the packaged instance, you may need to comment out potentially redundant JARs in this list (as was done for `fml_loader` and `fml_earlydisplay`).

## Usage

1.  **Configure:** Ensure `config.py` and `dependencies.py` are set up correctly for your environment.
2.  **Run:** Open a terminal or command prompt in the project's root directory (where `__main__.py` is located) and run:
    ```bash
    python3 __main__.py
    # or on Windows:
    # python main.py
    ```
3.  **Prompts:**
    *   The script will ask for the desired **username**. Enter one or press Enter to default to "test".
    *   If the configured `OUTPUT_BASE_DIR` already exists and is not empty, it will ask for **confirmation to overwrite**. Type `y` and press Enter to proceed.

## Output Structure

After successful execution, the configured `OUTPUT_BASE_DIR` will contain the following
