# config.py
from pathlib import Path

# !!! IMPORTANT: Set the desired output directory !!!
# This is where all the copied files will be placed.
OUTPUT_BASE_DIR = Path("./mcreator_launch_package")

# --- Optional: Define source paths here if preferred ---
# If you uncomment these, remove the corresponding definitions from dependencies.py
# MC_JAVA_HOME = Path("/Applications/MCreator.app/Contents/jdk.bundle/Contents/Home")
# WORKSPACE_BASE = Path.home() / "MCreatorWorkspaces"
# MCREATOR_CACHE_BASE = Path.home() / ".mcreator" / "gradle" / "caches" / "modules-2" / "files-2.1"
# WORKSPACE_NAME = "cool_new_stuff"
# MOD_PROJECT_SUBDIR = "packloader" # Used to find moddev, even if not packaging the mod itself