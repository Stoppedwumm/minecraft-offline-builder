# packaging.py
import shutil
import os
from pathlib import Path
import platform

def modify_prog_args_username(content: str, username: str) -> str:
    """
    Modifies the program arguments content to set the username.
    Adds the --username argument if it doesn't exist.
    """
    lines = content.splitlines()
    modified_lines = []
    username_line_found = False
    username_arg = f"--username={username}"

    for line in lines:
        # Strip whitespace to handle potential indentation variations
        stripped_line = line.strip()
        if stripped_line.startswith("--username="):
            modified_lines.append(username_arg) # Replace with new arg
            username_line_found = True
            print(f"  Replaced username line in program args.")
        else:
            modified_lines.append(line) # Keep other lines

    # If the username argument was never found, add it
    if not username_line_found:
        modified_lines.append(username_arg)
        print(f"  Added username line to program args.")

    # Join lines back, preserving original line ending style if possible,
    # otherwise default to os.linesep
    if "\r\n" in content:
        return "\r\n".join(modified_lines)
    elif "\n" in content:
        return "\n".join(modified_lines)
    else: # Single line or unknown
        return os.linesep.join(modified_lines)


def copy_launch_dependencies(
    output_dir: Path,
    java_source_exec: Path,
    java_lib_source_dir: Path,
    java_conf_source_dir: Path,
    vm_args_source_file: Path,
    prog_args_source_file: Path,
    target_username: str, # New parameter for the desired username
    classpath_sources: list[Path],
    mod_build_dir: Path, # Needed to identify classes/resources dirs
    mcreator_cache_dir: Path, # Needed for relative path printing
    workspace_dir: Path # Needed for relative path printing
):
    """
    Copies all required files and directories into the specified output directory.
    Modifies the program arguments file to set the username.
    """
    print(f"Starting dependency copy process to: {output_dir}")

    # --- 1. Define Destination Paths ---
    libs_dir = output_dir / "libs"
    classes_dir = output_dir / "classes"
    resources_dir = output_dir / "resources"
    java_dir = output_dir / "java"
    java_bin_dir = java_dir / "bin"
    java_lib_dir = java_dir / "lib"
    java_conf_dir = java_dir / "conf"

    # --- 2. Create Output Directories ---
    print("Creating output directory structure...")
    for dir_path in [libs_dir, classes_dir, resources_dir, java_bin_dir, java_lib_dir, java_conf_dir]:
        dir_path.mkdir(parents=True, exist_ok=True)

    # --- Init Counters ---
    copied_files = 0
    skipped_files = 0
    copied_executables = 0
    skipped_executables = 0
    copied_dirs = 0
    skipped_dirs = 0

    # --- 3. Copy/Modify Argument Files ---
    print("\nProcessing Argument Files...")

    # --- VM Args (Simple Copy) ---
    vm_args_dest_path = output_dir / vm_args_source_file.name
    if vm_args_source_file.exists():
        try:
            shutil.copy2(vm_args_source_file, vm_args_dest_path)
            print(f"  Copied: {vm_args_source_file.name}")
            copied_files += 1
        except Exception as e:
            print(f"  ERROR copying {vm_args_source_file.name}: {e}")
            skipped_files += 1
    else:
        print(f"  WARNING: Source file not found, skipping: {vm_args_source_file}")
        skipped_files += 1

    # --- Program Args (Read -> Modify -> Write) ---
    prog_args_dest_path = output_dir / prog_args_source_file.name
    if prog_args_source_file.exists():
        try:
            print(f"  Processing program args: {prog_args_source_file.name}")
            original_content = prog_args_source_file.read_text(encoding='utf-8')
            modified_content = modify_prog_args_username(original_content, target_username)
            prog_args_dest_path.write_text(modified_content, encoding='utf-8')
            print(f"  Written modified: {prog_args_dest_path.name}")
            copied_files += 1 # Count as one "copied" file operation
        except FileNotFoundError:
             print(f"  WARNING: Source file not found during processing, skipping: {prog_args_source_file}")
             skipped_files += 1
        except Exception as e:
            print(f"  ERROR processing/writing {prog_args_source_file.name}: {e}")
            skipped_files += 1
    else:
        print(f"  WARNING: Source file not found, skipping: {prog_args_source_file}")
        # Optionally, create a new file with just the username if the source doesn't exist?
        # try:
        #     print(f"  WARNING: Source file {prog_args_source_file.name} not found. Creating new one with username.")
        #     prog_args_dest_path.write_text(f"--username={target_username}", encoding='utf-8')
        #     copied_files += 1
        # except Exception as e:
        #      print(f"  ERROR creating new program args file {prog_args_dest_path.name}: {e}")
        #      skipped_files += 1
        skipped_files += 1 # Keep it simple: if source missing, skip.


    # --- 4. Copy Java Components (bin/java, lib, conf) ---
    print("\nProcessing Java Runtime Components...")
    # (Executable, Lib, Conf copying logic remains the same as before)
    # Executable
    if java_source_exec.exists() and java_source_exec.is_file():
        try:
            dest_java_exec = java_bin_dir / java_source_exec.name
            shutil.copy2(java_source_exec, dest_java_exec)
            if platform.system() != "Windows":
                os.chmod(dest_java_exec, 0o755)
            print(f"  Copied executable: {java_source_exec.name} -> {dest_java_exec.relative_to(output_dir)}")
            copied_executables += 1
        except Exception as e:
            print(f"  ERROR copying Java executable {java_source_exec}: {e}")
            skipped_executables += 1
    else:
        print(f"  WARNING: Java executable not found or is not a file, skipping: {java_source_exec}")
        skipped_executables += 1

    # Lib Directory
    if java_lib_source_dir.exists() and java_lib_source_dir.is_dir():
        try:
            shutil.copytree(java_lib_source_dir, java_lib_dir, dirs_exist_ok=True)
            print(f"  Copied directory tree: {java_lib_source_dir.name} -> {java_lib_dir.relative_to(output_dir)}")
            copied_dirs += 1
        except Exception as e:
            print(f"  ERROR copying Java lib directory {java_lib_source_dir}: {e}")
            skipped_dirs += 1
    else:
        print(f"  WARNING: Java lib directory not found or is not a directory, skipping: {java_lib_source_dir}")
        skipped_dirs += 1

    # Conf Directory
    if java_conf_source_dir.exists() and java_conf_source_dir.is_dir():
        try:
            shutil.copytree(java_conf_source_dir, java_conf_dir, dirs_exist_ok=True)
            print(f"  Copied directory tree: {java_conf_source_dir.name} -> {java_conf_dir.relative_to(output_dir)}")
            copied_dirs += 1
        except Exception as e:
            print(f"  ERROR copying Java conf directory {java_conf_source_dir}: {e}")
            skipped_dirs += 1
    else:
        print(f"  WARNING: Java conf directory not found or is not a directory, skipping: {java_conf_source_dir}")
        # Don't count as skipped if it's optional and just not present

    # --- 5. Copy Classpath Items ---
    print("\nProcessing classpath items...")
    # (Classpath copying logic remains the same as before)
    classes_java_main_src = mod_build_dir / "classes" / "java" / "main"
    resources_main_src = mod_build_dir / "resources" / "main"

    for src_path in classpath_sources:
        if not src_path.exists():
            print(f"  WARNING: Source item not found, skipping: {src_path}")
            # Best guess for type if it doesn't exist
            if src_path.suffix in ['.jar', '.zip']:
                 skipped_files += 1
            elif not src_path.suffix: # Likely intended dir
                 skipped_dirs +=1
            else: # Other file types
                skipped_files += 1
            continue # Skip to next item

        try:
            # Handle specific build directories
            if src_path == classes_java_main_src:
                dest_dir = classes_dir / "java" / "main"
                dest_dir.parent.mkdir(parents=True, exist_ok=True)
                shutil.copytree(src_path, dest_dir, dirs_exist_ok=True)
                print(f"  Copied directory tree: classes/java/main")
                copied_dirs += 1
            elif src_path == resources_main_src:
                dest_dir = resources_dir / "main"
                dest_dir.parent.mkdir(parents=True, exist_ok=True)
                shutil.copytree(src_path, dest_dir, dirs_exist_ok=True)
                print(f"  Copied directory tree: resources/main")
                copied_dirs += 1
            # Handle JAR files
            elif src_path.is_file() and src_path.suffix == '.jar':
                dest_file = libs_dir / src_path.name
                shutil.copy2(src_path, dest_file)
                print(f"  Copied JAR: {src_path.name} -> libs/")
                copied_files += 1
            # Handle other files (like extra resources jar)
            elif src_path.is_file():
                 dest_file = libs_dir / src_path.name # Put other files in libs too
                 shutil.copy2(src_path, dest_file)
                 print(f"  Copied File: {src_path.name} -> libs/")
                 copied_files += 1
            # Warn about unexpected directories in classpath list
            elif src_path.is_dir():
                 print(f"  WARNING: Unexpected directory {src_path.name} found in classpath sources list, skipping.")
                 skipped_dirs += 1
            else:
                 print(f"  WARNING: Source item {src_path.name} is not a file or directory, skipping.")
                 skipped_files += 1

        except Exception as e:
            print(f"  ERROR copying {src_path.name}: {e}")
            if src_path.is_dir(): skipped_dirs += 1
            else: skipped_files += 1


    # --- 6. Summary ---
    print("\n--- Copy Summary ---")
    print(f"Output Directory: {output_dir.resolve()}")
    print(f"Copied Executables (Java): {copied_executables}")
    print(f"Copied/Modified Files (Args, JARs, Other): {copied_files}") # Updated desc
    print(f"Copied Directory Trees (java/lib, java/conf, classes, resources): {copied_dirs}")
    print(f"Skipped/Missing Executables: {skipped_executables}")
    print(f"Skipped/Missing Files: {skipped_files}")
    print(f"Skipped/Missing/Unexpected Dirs: {skipped_dirs}")
    print("--------------------\n")

    # --- 7. Return info needed for script generator ---
    return {
        "java_exec_name": java_source_exec.name,
        "vm_args_name": vm_args_source_file.name,
        "prog_args_name": prog_args_source_file.name
    }
