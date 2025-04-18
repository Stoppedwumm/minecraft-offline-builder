# script_generator.py
import os
import platform
from pathlib import Path

def generate_example_script(
    output_dir: Path,
    java_exec_name: str,
    vm_args_name: str,
    prog_args_name: str
):
    """Generates a self-contained shell script to launch Java using the copied files."""
    target_os = platform.system()
    script_name = f"run_packaged_{target_os.lower()}.sh" if target_os != "Windows" else f"run_packaged_{target_os.lower()}.bat"
    script_path = output_dir / script_name

    # Define relative paths used inside the script structure
    relative_java_exec_dir = Path("java") / "bin"
    relative_java_exec = relative_java_exec_dir / java_exec_name
    libs_subdir = "libs"
    classes_subdir = "classes"
    resources_subdir = "resources"

    # --- Shell Script Content (Bash/Zsh for Linux/macOS) ---
    if target_os != "Windows":
        path_sep = ":"
        script_dir_logic = r"""
echo "Determining script directory..."
SOURCE="${BASH_SOURCE[0]:-$0}" # Handle zsh/bash differences for $0
while [ -L "$SOURCE" ]; do
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
done
SCRIPT_DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
echo "Script directory determined as: $SCRIPT_DIR"
"""
        # Define absolute paths based on SCRIPT_DIR
        java_exec_in_script = f"$SCRIPT_DIR/{relative_java_exec.as_posix()}"
        vm_args_file_in_script = f"$SCRIPT_DIR/{vm_args_name}"
        prog_args_file_in_script = f"$SCRIPT_DIR/{prog_args_name}"

        classpath_build_logic = f"""
echo "Building classpath..."
ABS_CLASSPATH="$SCRIPT_DIR/{classes_subdir}/java/main{path_sep}$SCRIPT_DIR/{resources_subdir}/main"
for item in "$SCRIPT_DIR"/{libs_subdir}/*; do
  if [ -f "$item" ]; then
      ABS_CLASSPATH="$ABS_CLASSPATH{path_sep}$item"
  fi
done
echo "Classpath built."
"""
        check_files_logic = f"""
echo "Checking required files..."
if [ ! -x "$JAVA_EXEC" ]; then echo "ERROR: Java executable not found or not executable at '$JAVA_EXEC'."; exit 1; fi
if [ ! -f "$VM_ARGS_FILE" ]; then echo "ERROR: VM arguments file not found at '$VM_ARGS_FILE'."; exit 1; fi
if [ ! -f "$PROG_ARGS_FILE" ]; then echo "ERROR: Program arguments file not found at '$PROG_ARGS_FILE'."; exit 1; fi
echo "Required files checked."
"""
        # Use escaped curly braces for shell variables inside f-string
        java_command = f"""
echo "Attempting to launch using absolute paths..."
echo "Using Java: $JAVA_EXEC"

"$JAVA_EXEC" \\
  @"$VM_ARGS_FILE" \\
  -Dfile.encoding=UTF-8 \\
  -Duser.country=US \\
  -Duser.language=en \\
  -Duser.variant \\
  -cp \\
  "$ABS_CLASSPATH" \\
  net.neoforged.devlaunch.Main \\
  @"$PROG_ARGS_FILE" 2>&1
"""
        script_content = f"""#!/bin/bash
# Launch script using packaged dependencies with runtime path resolution.

{script_dir_logic}

# --- Configuration (Absolute Paths) ---
JAVA_EXEC="{java_exec_in_script}"
VM_ARGS_FILE="{vm_args_file_in_script}"
PROG_ARGS_FILE="{prog_args_file_in_script}"

{classpath_build_logic}
{check_files_logic}
{java_command}

EXIT_CODE=$?
echo "Java process finished with exit code $EXIT_CODE."
exit $EXIT_CODE
"""

    # --- Batch Script Content (Windows) ---
    else:
        path_sep = ";"
        script_dir_logic = r"""
@echo off
echo Determining script directory...
set "SCRIPT_DIR=%~dp0"
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
echo Script directory determined as: %SCRIPT_DIR%
"""
        # FIX: Construct path string outside f-string
        java_exec_rel_path_win = str(relative_java_exec).replace('/', '\\')
        java_exec_in_script = f"%SCRIPT_DIR%\\{java_exec_rel_path_win}"
        vm_args_file_in_script = f"%SCRIPT_DIR%\\{vm_args_name}"
        prog_args_file_in_script = f"%SCRIPT_DIR%\\{prog_args_name}"

        classpath_build_logic = f"""
echo Building classpath...
set "ABS_CLASSPATH=%SCRIPT_DIR%\\{classes_subdir}\\java\\main{path_sep}%SCRIPT_DIR%\\{resources_subdir}\\main"
pushd "%SCRIPT_DIR%\\{libs_subdir}"
for %%j in (*) do (
    if exist "%%j" (
        call set "ABS_CLASSPATH=%%ABS_CLASSPATH%%{path_sep}%SCRIPT_DIR%\\{libs_subdir}\\%%j"
    )
)
popd
echo Classpath built.
"""
        check_files_logic = f"""
echo Checking required files...
if not exist "%JAVA_EXEC%" ( echo ERROR: Java executable not found at "%JAVA_EXEC%". & exit /b 1 )
if not exist "%VM_ARGS_FILE%" ( echo ERROR: VM arguments file not found at "%VM_ARGS_FILE%". & exit /b 1 )
if not exist "%PROG_ARGS_FILE%" ( echo ERROR: Program arguments file not found at "%PROG_ARGS_FILE%". & exit /b 1 )
echo Required files checked.
"""
        # Corrected variable usage for Batch @file syntax
        java_command = f"""
echo Attempting to launch using absolute paths...
echo Using Java: %JAVA_EXEC%

"%JAVA_EXEC%" ^
  @"%VM_ARGS_FILE%" ^
  -Dfile.encoding=UTF-8 ^
  -Duser.country=US ^
  -Duser.language=en ^
  -Duser.variant ^
  -cp ^
  "%ABS_CLASSPATH%" ^
  net.neoforged.devlaunch.Main ^
  @"%PROG_ARGS_FILE%"
"""
        script_content = f"""{script_dir_logic}

set "JAVA_EXEC={java_exec_in_script}"
set "VM_ARGS_FILE={vm_args_file_in_script}"
set "PROG_ARGS_FILE={prog_args_file_in_script}"

{classpath_build_logic}
{check_files_logic}
{java_command}

echo.
echo Java process finished with exit code %ERRORLEVEL%.
exit /b %ERRORLEVEL%
"""

    # --- Write the script ---
    print(f"Generating launch script: {script_path.name}")
    try:
        # Use UTF-8 encoding; use OS-native line endings for batch files.
        newline_mode = None if target_os == "Windows" else '\n'
        with open(script_path, "w", encoding='utf-8', newline=newline_mode) as f:
            f.write(script_content)
        # Make executable on Unix-like systems
        if target_os != "Windows":
            os.chmod(script_path, 0o755)
        print(f"Successfully wrote launch script.")
        if target_os != "Windows":
            print(f"To run (on Linux/macOS): ./{output_dir.name}/{script_name}")
        else:
            print(f"To run (on Windows): .\\{output_dir.name}\\{script_name}")

    except Exception as e:
        print(f"ERROR generating launch script: {e}")