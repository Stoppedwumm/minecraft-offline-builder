# main.py
import sys
from pathlib import Path

# Import from our modules
import config
import dependencies
import packaging
import script_generator

def run():
    """Main execution function."""
    print("--- MCreator Packager ---")

    # --- Configuration ---
    output_dir = config.OUTPUT_BASE_DIR.resolve()
    print(f"Target output directory: {output_dir}")

    # --- Dependencies ---
    # These are sourced from dependencies.py
    java_source_exec = dependencies.MC_JAVA_SOURCE_EXEC
    java_lib_source_dir = dependencies.MC_JAVA_LIB_SOURCE_DIR
    java_conf_source_dir = dependencies.MC_JAVA_CONF_SOURCE_DIR
    vm_args_source_file = dependencies.CLIENT_RUN_VM_ARGS_FILE
    prog_args_source_file = dependencies.CLIENT_RUN_PROGRAM_ARGS_FILE
    classpath_sources = dependencies.CLASSPATH_SOURCES
    mod_build_dir = dependencies.MOD_BUILD_DIR # Needed by packaging
    mcreator_cache_dir = dependencies._MCREATOR_CACHE_BASE # Needed by packaging
    workspace_dir = dependencies.WORKSPACE_DIR # Needed by packaging

    # --- Get Username ---
    target_username = ""
    try:
        target_username = input("Enter desired username (leave blank for default 'test'): ").strip()
        if not target_username:
            target_username = "test" # Default if blank
        print(f"Using username: {target_username}")
    except EOFError:
        print("No input detected, using default username 'test'.")
        target_username = "test"

    # --- Confirmation ---
    if output_dir.exists() and any(output_dir.iterdir()):
        try:
            confirm = input(f"Output directory '{output_dir}' exists and is not empty. Overwrite contents? (y/N): ")
            if confirm.lower() != 'y':
                print("Operation cancelled by user.")
                sys.exit(0) # Use sys.exit for cleaner exit
            else:
                print("Proceeding with overwrite...")
        except EOFError: # Handle case where input is piped or unavailable
             print("No input detected, cancelling overwrite.")
             sys.exit(1)


    # --- Packaging ---
    try:
        package_info = packaging.copy_launch_dependencies(
            output_dir=output_dir,
            java_source_exec=java_source_exec,
            java_lib_source_dir=java_lib_source_dir,
            java_conf_source_dir=java_conf_source_dir,
            vm_args_source_file=vm_args_source_file,
            prog_args_source_file=prog_args_source_file,
            # Pass the collected username
            target_username=target_username,
            classpath_sources=classpath_sources,
            mod_build_dir=mod_build_dir,
            mcreator_cache_dir=mcreator_cache_dir,
            workspace_dir=workspace_dir
        )
    except Exception as e:
        print(f"\nFATAL ERROR during packaging: {e}")
        # You might want to add more specific error handling or logging here
        import traceback
        traceback.print_exc()
        sys.exit(1)

    # --- Script Generation ---
    try:
        script_generator.generate_example_script(
            output_dir=output_dir,
            java_exec_name=package_info["java_exec_name"],
            vm_args_name=package_info["vm_args_name"],
            prog_args_name=package_info["prog_args_name"]
        )
    except Exception as e:
        print(f"\nFATAL ERROR during script generation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


    print("\nPackaging complete.")
    print(f"Package created at: {output_dir}")

# --- Script Entry Point ---
if __name__ == "__main__":
    run()
