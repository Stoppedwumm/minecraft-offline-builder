# dependencies.py
from pathlib import Path

# --- Define Source Locations ---
# Using hardcoded paths based on the original script.
# Consider moving these to config.py if you prefer more central configuration.

_HOME = Path.home()
_MC_JAVA_HOME = Path("/Applications/MCreator.app/Contents/jdk.bundle/Contents/Home")
_WORKSPACE_BASE = _HOME / "MCreatorWorkspaces"
_MCREATOR_CACHE_BASE = _HOME / ".mcreator" / "gradle" / "caches" / "modules-2" / "files-2.1"
_WORKSPACE_NAME = "cool_new_stuff"
_MOD_PROJECT_SUBDIR = "packloader"

# --- Derived Source Paths ---

# Java Paths
MC_JAVA_BIN_SOURCE_DIR = _MC_JAVA_HOME / "bin"
MC_JAVA_SOURCE_EXEC = MC_JAVA_BIN_SOURCE_DIR / "java"
MC_JAVA_LIB_SOURCE_DIR = _MC_JAVA_HOME / "lib"
MC_JAVA_CONF_SOURCE_DIR = _MC_JAVA_HOME / "conf"

# Project/Build Paths
WORKSPACE_DIR = _WORKSPACE_BASE / _WORKSPACE_NAME
MOD_PROJECT_DIR = WORKSPACE_DIR / _MOD_PROJECT_SUBDIR
MOD_BUILD_DIR = MOD_PROJECT_DIR / "build"
MODDEV_DIR = MOD_BUILD_DIR / "moddev"

# Argument Files
CLIENT_RUN_VM_ARGS_FILE = MODDEV_DIR / "clientRunVmArgs.txt"
CLIENT_RUN_PROGRAM_ARGS_FILE = MODDEV_DIR / "clientRunProgramArgs.txt"

# --- Classpath Sources ---
# This long list defines all the JARs needed.

CLASSPATH_SOURCES = [
    # Directories from build output (handle separately in packaging)
    MOD_BUILD_DIR / "classes" / "java" / "main",
    MOD_BUILD_DIR / "resources" / "main",

    # --- Start of JARs and other files ---
    MODDEV_DIR / "artifacts" / "neoforge-21.4.123.jar",
    MODDEV_DIR / "artifacts" / "neoforge-21.4.123-client-extra-aka-minecraft-resources.jar",
    _MCREATOR_CACHE_BASE / "net.neoforged" / "DevLaunch" / "1.0.1" / "48617810523f426d42430867894faa7fe1b933dd" / "DevLaunch-1.0.1.jar",
    # !!! REMOVED potential duplicate earlydisplay JAR to resolve JPMS conflict !!!
    # _MCREATOR_CACHE_BASE / "net.neoforged.fancymodloader" / "earlydisplay" / "6.0.11" / "caa7da96be4843d6399d44704dff98fe4e7c93ec" / "earlydisplay-6.0.11.jar",
    # !!! REMOVED potential duplicate loader JAR to resolve JPMS conflict !!!
    # _MCREATOR_CACHE_BASE / "net.neoforged.fancymodloader" / "loader" / "6.0.11" / "3ea5476a836130ec300ac20107b661a57f9ec71a" / "loader-6.0.11.jar",
    _MCREATOR_CACHE_BASE / "net.neoforged.accesstransformers" / "at-modlauncher" / "11.0.1" / "c3bab0ab738f57325df7be7d7cb71868b775cffc" / "at-modlauncher-11.0.1.jar",
    _MCREATOR_CACHE_BASE / "net.neoforged" / "accesstransformers" / "11.0.1" / "41c41b1cd9800f0fea16c89a5e21f83d34bd9b87" / "accesstransformers-11.0.1.jar",
    _MCREATOR_CACHE_BASE / "net.neoforged" / "bus" / "8.0.2" / "163c9ef7c4bcca6d850c34e95261b606af91fe06" / "bus-8.0.2.jar",
    _MCREATOR_CACHE_BASE / "net.neoforged" / "coremods" / "7.0.3" / "9147e6f638b4272b3bd5fc8f92ad37802512c6c" / "coremods-7.0.3.jar",
    _MCREATOR_CACHE_BASE / "cpw.mods" / "modlauncher" / "11.0.4" / "6619d4812a3c092310d521ebc4c9503727563df7" / "modlauncher-11.0.4.jar",
    _MCREATOR_CACHE_BASE / "net.neoforged" / "mergetool" / "2.0.0" / "52fe1949be64e3303aabaaa21e315f551db9c9f4" / "mergetool-2.0.0-api.jar",
    _MCREATOR_CACHE_BASE / "com.electronwill.night-config" / "toml" / "3.8.1" / "fb0731789fc50ddeb3ad43e48ef65008b777b2ec" / "toml-3.8.1.jar",
    _MCREATOR_CACHE_BASE / "com.electronwill.night-config" / "core" / "3.8.1" / "530d608fc238350f00c815d562f21a5d79939972" / "core-3.8.1.jar",
    _MCREATOR_CACHE_BASE / "net.neoforged" / "JarJarSelector" / "0.4.1" / "fb3cc7a58af22ad2880adb98af6d518128c47dae" / "JarJarSelector-0.4.1.jar",
    _MCREATOR_CACHE_BASE / "net.neoforged" / "JarJarMetadata" / "0.4.1" / "f8da03683dc81694556dc3e177c5e3bb77ae6fcb" / "JarJarMetadata-0.4.1.jar",
    _MCREATOR_CACHE_BASE / "org.apache.maven" / "maven-artifact" / "3.9.9" / "a130ec431ef32e12a4424f9b074735bb58e15d2d" / "maven-artifact-3.9.9.jar",
    _MCREATOR_CACHE_BASE / "net.jodah" / "typetools" / "0.6.3" / "a01aaa6ddaea9ec07ec4f209487b7a46a526283a" / "typetools-0.6.3.jar",
    _MCREATOR_CACHE_BASE / "net.minecrell" / "terminalconsoleappender" / "1.3.0" / "b562e9bb61235c9520e26282cdee71f8f802d1fc" / "terminalconsoleappender-1.3.0.jar",
    _MCREATOR_CACHE_BASE / "net.fabricmc" / "sponge-mixin" / "0.15.2+mixin.0.8.7" / "2af2f021d8e02a0220dc27a7a72b4666d66d44ca" / "sponge-mixin-0.15.2+mixin.0.8.7.jar",
    _MCREATOR_CACHE_BASE / "org.openjdk.nashorn" / "nashorn-core" / "15.4" / "f67f5ffaa5f5130cf6fb9b133da00c7df3b532a5" / "nashorn-core-15.4.jar",
    _MCREATOR_CACHE_BASE / "cpw.mods" / "bootstraplauncher" / "2.0.2" / "1a2d076cbc33b0520cbacd591224427b2a20047d" / "bootstraplauncher-2.0.2.jar",
    _MCREATOR_CACHE_BASE / "cpw.mods" / "securejarhandler" / "3.0.8" / "c0ef95cecd8699a0449053ac7d9c160748d902cd" / "securejarhandler-3.0.8.jar",
    _MCREATOR_CACHE_BASE / "org.ow2.asm" / "asm-commons" / "9.7" / "e86dda4696d3c185fcc95d8d311904e7ce38a53f" / "asm-commons-9.7.jar",
    _MCREATOR_CACHE_BASE / "org.ow2.asm" / "asm-util" / "9.7" / "c0655519f24d92af2202cb681cd7c1569df6ead6" / "asm-util-9.7.jar",
    _MCREATOR_CACHE_BASE / "org.ow2.asm" / "asm-analysis" / "9.7" / "e4a258b7eb96107106c0599f0061cfc1832fe07a" / "asm-analysis-9.7.jar",
    _MCREATOR_CACHE_BASE / "org.ow2.asm" / "asm-tree" / "9.7" / "e446a17b175bfb733b87c5c2560ccb4e57d69f1a" / "asm-tree-9.7.jar",
    _MCREATOR_CACHE_BASE / "org.ow2.asm" / "asm" / "9.7" / "73d7b3086e14beb604ced229c302feff6449723" / "asm-9.7.jar",
    _MCREATOR_CACHE_BASE / "net.neoforged" / "JarJarFileSystems" / "0.4.1" / "78f59f89defcd032ed788b151ca6a0d40ace796a" / "JarJarFileSystems-0.4.1.jar",
    _MCREATOR_CACHE_BASE / "net.sf.jopt-simple" / "jopt-simple" / "5.0.4" / "4fdac2fbe92dfad86aa6e9301736f6b4342a3f5c" / "jopt-simple-5.0.4.jar",
    _MCREATOR_CACHE_BASE / "commons-io" / "commons-io" / "2.17.0" / "ddcc8433eb019fb48fe25207c0278143f3e1d7e2" / "commons-io-2.17.0.jar",
    _MCREATOR_CACHE_BASE / "com.mojang" / "logging" / "1.5.10" / "9ab1202793717af9df9c1704d0a02892067001eb" / "logging-1.5.10.jar",
    _MCREATOR_CACHE_BASE / "org.apache.logging.log4j" / "log4j-slf4j2-impl" / "2.24.1" / "8e3ddc96464ef7f768823e7e001a52b23de8cd0a" / "log4j-slf4j2-impl-2.24.1.jar",
    _MCREATOR_CACHE_BASE / "org.apache.logging.log4j" / "log4j-core" / "2.24.1" / "c85285146f28d8c8962384f786e2dff04172fb43" / "log4j-core-2.24.1.jar",
    _MCREATOR_CACHE_BASE / "org.apache.logging.log4j" / "log4j-api" / "2.24.1" / "7ebeb12c20606373005af4232cd0ecca72613dda" / "log4j-api-2.24.1.jar",
    _MCREATOR_CACHE_BASE / "com.google.guava" / "guava" / "33.3.1-jre" / "852f8b363da0111e819460021ca693cacca3e8db" / "guava-33.3.1-jre.jar",
    _MCREATOR_CACHE_BASE / "com.google.code.gson" / "gson" / "2.11.0" / "527175ca6d81050b53bdd4c457a6d6e017626b0e" / "gson-2.11.0.jar",
    _MCREATOR_CACHE_BASE / "org.apache.commons" / "commons-lang3" / "3.17.0" / "b17d2136f0460dcc0d2016ceefca8723bdf4ee70" / "commons-lang3-3.17.0.jar",
    _MCREATOR_CACHE_BASE / "net.neoforged.accesstransformers" / "at-parser" / "11.0.1" / "124789359511c100a88ab0ba90adc80a8fd7db36" / "at-parser-11.0.1.jar",
    _MCREATOR_CACHE_BASE / "org.slf4j" / "slf4j-api" / "2.0.16" / "172931663a09a1fa515567af5fbef00897d3c04" / "slf4j-api-2.0.16.jar",
    _MCREATOR_CACHE_BASE / "net.minecraftforge" / "srgutils" / "0.4.15" / "ca408b131759478f164e010fae0d73997e125fb5" / "srgutils-0.4.15.jar",
    _MCREATOR_CACHE_BASE / "org.codehaus.plexus" / "plexus-utils" / "3.5.1" / "c6bfb17c97ecc8863e88778ea301be742c62b06d" / "plexus-utils-3.5.1.jar",
    _MCREATOR_CACHE_BASE / "org.jline" / "jline-reader" / "3.20.0" / "8f15415b022a25b473e8e16c28ae913186ffb9c4" / "jline-reader-3.20.0.jar",
    _MCREATOR_CACHE_BASE / "com.machinezoo.noexception" / "noexception" / "1.7.1" / "b65330c98e38a1f915fa54a6e5eca496505e3f0a" / "noexception-1.7.1.jar",
    _MCREATOR_CACHE_BASE / "com.fasterxml.jackson.core" / "jackson-annotations" / "2.13.4" / "858c6cc78e1f08a885b1613e1d817c829df70a6e" / "jackson-annotations-2.13.4.jar",
    _MCREATOR_CACHE_BASE / "com.fasterxml.jackson.core" / "jackson-core" / "2.13.4" / "cf934c681294b97ef6d80082faeefbe1edadf56" / "jackson-core-2.13.4.jar",
    _MCREATOR_CACHE_BASE / "com.fasterxml.jackson.core" / "jackson-databind" / "2.13.4.2" / "325c06bdfeb628cfb80ebaaf1a26cc1eb558a585" / "jackson-databind-2.13.4.2.jar",
    _MCREATOR_CACHE_BASE / "com.github.oshi" / "oshi-core" / "6.6.5" / "e1099981fd15dc4236c4499d82aba1276fb43a9a" / "oshi-core-6.6.5.jar",
    _MCREATOR_CACHE_BASE / "com.github.stephenc.jcip" / "jcip-annotations" / "1.0-1" / "ef31541dd28ae2cefdd17c7ebf352d93e9058c63" / "jcip-annotations-1.0-1.jar",
    _MCREATOR_CACHE_BASE / "com.google.guava" / "failureaccess" / "1.0.2" / "c4a06a64e650562f30b7bf9aaec1bfed43aca12b" / "failureaccess-1.0.2.jar",
    _MCREATOR_CACHE_BASE / "com.ibm.icu" / "icu4j" / "76.1" / "215f3a8e936d4069344bd75f2b1368fd58112894" / "icu4j-76.1.jar",
    _MCREATOR_CACHE_BASE / "com.microsoft.azure" / "msal4j" / "1.17.2" / "a6211e3d71d0388929babaa0ff0951b30d001852" / "msal4j-1.17.2.jar",
    _MCREATOR_CACHE_BASE / "com.mojang" / "authlib" / "6.0.57" / "bded3161a7346de32213da750388ec6529fe4f6b" / "authlib-6.0.57.jar",
    _MCREATOR_CACHE_BASE / "com.mojang" / "blocklist" / "1.0.10" / "5c685c5ffa94c4cd39496c7184c1d122e515ecef" / "blocklist-1.0.10.jar",
    _MCREATOR_CACHE_BASE / "com.mojang" / "brigadier" / "1.3.10" / "d15b53a14cf20fdcaa98f731af5dda654452c010" / "brigadier-1.3.10.jar",
    _MCREATOR_CACHE_BASE / "com.mojang" / "datafixerupper" / "8.0.16" / "67d4de6d7f95d89bcf5862995fb854ebaec02a34" / "datafixerupper-8.0.16.jar",
    _MCREATOR_CACHE_BASE / "com.mojang" / "jtracy" / "1.0.29" / "6f07dcb6a2e595c7ee2ca43b67e5d1c018ca0770" / "jtracy-1.0.29.jar",
    _MCREATOR_CACHE_BASE / "com.mojang" / "jtracy" / "1.0.29" / "d620e5b94ca81783b409d50c48b73e0ee7fdcb7d" / "jtracy-1.0.29-natives-macos.jar", # Adjust natives if needed
    _MCREATOR_CACHE_BASE / "com.mojang" / "patchy" / "2.2.10" / "da05971b07cbb379d002cf7eaec6a2048211fefc" / "patchy-2.2.10.jar",
    _MCREATOR_CACHE_BASE / "com.mojang" / "text2speech" / "1.17.9" / "3cad216e3a7f0c19b4b394388bc9ffc446f13b14" / "text2speech-1.17.9.jar",
    _MCREATOR_CACHE_BASE / "com.nimbusds" / "content-type" / "2.3" / "e3aa0be212d7a42839a8f3f506f5b990bcce0222" / "content-type-2.3.jar",
    _MCREATOR_CACHE_BASE / "com.nimbusds" / "lang-tag" / "1.7" / "97c73ecd70bc7e8eefb26c5eea84f251a63f1031" / "lang-tag-1.7.jar",
    _MCREATOR_CACHE_BASE / "com.nimbusds" / "nimbus-jose-jwt" / "9.40" / "42b1dfa0360e4062951b070bac52dd8d96fd7b38" / "nimbus-jose-jwt-9.40.jar",
    _MCREATOR_CACHE_BASE / "com.nimbusds" / "oauth2-oidc-sdk" / "11.18" / "7c7ec4f4066625ff07a711ad856fa04da1ff9de" / "oauth2-oidc-sdk-11.18.jar",
    _MCREATOR_CACHE_BASE / "commons-codec" / "commons-codec" / "1.17.1" / "973638b7149d333563584137ebf13a691bb60579" / "commons-codec-1.17.1.jar",
    _MCREATOR_CACHE_BASE / "commons-logging" / "commons-logging" / "1.3.4" / "b9fc14968d63a8b8a8a2c1885fe3e90564239708" / "commons-logging-1.3.4.jar",
    _MCREATOR_CACHE_BASE / "io.netty" / "netty-buffer" / "4.1.115.Final" / "d5daf1030e5c36d198caf7562da2441a97ec0df6" / "netty-buffer-4.1.115.Final.jar",
    _MCREATOR_CACHE_BASE / "io.netty" / "netty-codec" / "4.1.115.Final" / "d326bf3a4c785b272da3db6941779a1bd5448378" / "netty-codec-4.1.115.Final.jar",
    _MCREATOR_CACHE_BASE / "io.netty" / "netty-common" / "4.1.115.Final" / "9da10a9f72e3f87e181d91b525174007a6fc4f11" / "netty-common-4.1.115.Final.jar",
    _MCREATOR_CACHE_BASE / "io.netty" / "netty-handler" / "4.1.115.Final" / "d54dbf68b9d88a98240107758c6b63da5e46e23a" / "netty-handler-4.1.115.Final.jar",
    _MCREATOR_CACHE_BASE / "io.netty" / "netty-resolver" / "4.1.115.Final" / "e33b4d476c03975957f5d8d0319d592bf2bc5e96" / "netty-resolver-4.1.115.Final.jar",
    _MCREATOR_CACHE_BASE / "io.netty" / "netty-transport-classes-epoll" / "4.1.115.Final" / "11fea00408ecbd8b8d1f0698d708e37db4a01841" / "netty-transport-classes-epoll-4.1.115.Final.jar",
    _MCREATOR_CACHE_BASE / "io.netty" / "netty-transport-native-unix-common" / "4.1.115.Final" / "dc96c67d06cd6b5eb677f2728f27bf2e3d9a7284" / "netty-transport-native-unix-common-4.1.115.Final.jar",
    _MCREATOR_CACHE_BASE / "io.netty" / "netty-transport" / "4.1.115.Final" / "39cef77c1a25908ac1abf4960c2e789f0bf70ff9" / "netty-transport-4.1.115.Final.jar",
    _MCREATOR_CACHE_BASE / "it.unimi.dsi" / "fastutil" / "8.5.15" / "1e885b40c9563ab0d3899b871fd0b30e958705dc" / "fastutil-8.5.15.jar",
    _MCREATOR_CACHE_BASE / "net.java.dev.jna" / "jna-platform" / "5.15.0" / "86b502cad57d45da172b5e3231c537b042e296ef" / "jna-platform-5.15.0.jar",
    _MCREATOR_CACHE_BASE / "net.java.dev.jna" / "jna" / "5.15.0" / "1ee1d80ff44f08280188f7c0e740d57207841ac" / "jna-5.15.0.jar",
    _MCREATOR_CACHE_BASE / "net.minidev" / "accessors-smart" / "2.5.1" / "19b820261eb2e7de7d5bde11d1c06e4501dd7e5f" / "accessors-smart-2.5.1.jar",
    _MCREATOR_CACHE_BASE / "net.minidev" / "json-smart" / "2.5.1" / "4c11d2808d009132dfbbf947ebf37de6bf266c8e" / "json-smart-2.5.1.jar",
    _MCREATOR_CACHE_BASE / "org.apache.commons" / "commons-compress" / "1.27.1" / "a19151084758e2fbb6b41eddaa88e7b8ff4e6599" / "commons-compress-1.27.1.jar",
    _MCREATOR_CACHE_BASE / "org.apache.httpcomponents" / "httpclient" / "4.5.14" / "1194890e6f56ec29177673f2f12d0b8e627dec98" / "httpclient-4.5.14.jar",
    _MCREATOR_CACHE_BASE / "org.apache.httpcomponents" / "httpcore" / "4.4.16" / "51cf043c87253c9f58b539c9f7e44c8894223850" / "httpcore-4.4.16.jar",
    _MCREATOR_CACHE_BASE / "org.jcraft" / "jorbis" / "0.0.17" / "8872d22b293e8f5d7d56ff92be966e6dc28ebdc6" / "jorbis-0.0.17.jar",
    _MCREATOR_CACHE_BASE / "org.joml" / "joml" / "1.10.8" / "fc0a71dad90a2cf41d82a76156a0e700af8e4f8d" / "joml-1.10.8.jar",
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-freetype" / "3.3.3" / "a0db6c84a8becc8ca05f9dbfa985edc348a824c7" / "lwjgl-freetype-3.3.3.jar",
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-freetype" / "3.3.3" / "b0a8c9baa9d1f54ac61e1ab9640c7659e7fa700c" / "lwjgl-freetype-3.3.3-natives-macos-arm64.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-freetype" / "3.3.3" / "806d869f37ce0df388a24e17aaaf5ca0894d851b" / "lwjgl-freetype-3.3.3-natives-macos-patch.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-glfw" / "3.3.3" / "efa1eb78c5ccd840e9f329717109b5e892d72f8e" / "lwjgl-glfw-3.3.3.jar",
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-glfw" / "3.3.3" / "a1bf400f6bc64e6195596cb1430dafda46090751" / "lwjgl-glfw-3.3.3-natives-macos.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-glfw" / "3.3.3" / "ee8cc78d0a4a5b3b4600fade6d927c9fc320c858" / "lwjgl-glfw-3.3.3-natives-macos-arm64.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-jemalloc" / "3.3.3" / "b543467b7ff3c6920539a88ee602d34098628be5" / "lwjgl-jemalloc-3.3.3.jar",
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-jemalloc" / "3.3.3" / "2906637657a57579847238c9c72d2c4bde7083f8" / "lwjgl-jemalloc-3.3.3-natives-macos.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-jemalloc" / "3.3.3" / "e9412c3ff8cb3a3bad1d3f52909ad74d8a5bdad1" / "lwjgl-jemalloc-3.3.3-natives-macos-arm64.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-openal" / "3.3.3" / "daada81ceb5fc0c291fbfdd4433cb8d9423577f2" / "lwjgl-openal-3.3.3.jar",
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-openal" / "3.3.3" / "8df8338bfa77f2ebabef4e58964bd04d24805cbf" / "lwjgl-openal-3.3.3-natives-macos.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-openal" / "3.3.3" / "c78b078de2fb52f45aa55d04db889a560f3544f" / "lwjgl-openal-3.3.3-natives-macos-arm64.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-opengl" / "3.3.3" / "2f6b0147078396a58979125a4c947664e98293a" / "lwjgl-opengl-3.3.3.jar",
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-opengl" / "3.3.3" / "1bd45997551ae8a28469f3a2b678f4b7289e12c0" / "lwjgl-opengl-3.3.3-natives-macos.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-opengl" / "3.3.3" / "d213ddef27637b1af87961ffa94d6b27036becc8" / "lwjgl-opengl-3.3.3-natives-macos-arm64.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-stb" / "3.3.3" / "25dd6161988d7e65f71d5065c99902402ee32746" / "lwjgl-stb-3.3.3.jar",
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-stb" / "3.3.3" / "472792c98fb2c1557c060cb9da5fca6a9773621f" / "lwjgl-stb-3.3.3-natives-macos.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-stb" / "3.3.3" / "51c6955571fbcdb7bb538c6aa589b953b584c6af" / "lwjgl-stb-3.3.3-natives-macos-arm64.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-tinyfd" / "3.3.3" / "82d755ca94b102e9ca77283b9e2dc46d1b15fbe5" / "lwjgl-tinyfd-3.3.3.jar",
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-tinyfd" / "3.3.3" / "6598081e346a03038a8be68eb2de614a1c2eac68" / "lwjgl-tinyfd-3.3.3-natives-macos.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl-tinyfd" / "3.3.3" / "406feedb977372085a61eb0fee358183f4f4c67a" / "lwjgl-tinyfd-3.3.3-natives-macos-arm64.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl" / "3.3.3" / "29589b5f87ed335a6c7e7ee6a5775f81f97ecb84" / "lwjgl-3.3.3.jar",
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl" / "3.3.3" / "33a6efa288390490ce6eb6c3df47ac21ecf648cf" / "lwjgl-3.3.3-natives-macos.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lwjgl" / "lwjgl" / "3.3.3" / "226246e75f6bd8d4e1895bdce8638ef87808d114" / "lwjgl-3.3.3-natives-macos-arm64.jar", # Adjust natives
    _MCREATOR_CACHE_BASE / "org.lz4" / "lz4-java" / "1.8.0" / "4b986a99445e49ea5fbf5d149c4b63f6ed6c6780" / "lz4-java-1.8.0.jar",
    _MCREATOR_CACHE_BASE / "org.jline" / "jline-terminal" / "3.20.0" / "d0ddcc708ddf527a3454c941b7b9225cc83a15ff" / "jline-terminal-3.20.0.jar",
    _MCREATOR_CACHE_BASE / "ca.weblite" / "java-objc-bridge" / "1.1" / "1227f9e0666314f9de41477e3ec277e542ed7f7b" / "java-objc-bridge-1.1.jar",
    _MCREATOR_CACHE_BASE / "com.google.errorprone" / "error_prone_annotations" / "2.28.0" / "59fc00087ce372de42e394d2c789295dff2d19f0" / "error_prone_annotations-2.28.0.jar",
    _MCREATOR_CACHE_BASE / "com.google.guava" / "listenablefuture" / "9999.0-empty-to-avoid-conflict-with-guava" / "b421526c5f297295adef1c886e5246c39d4ac629" / "listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar",
    _MCREATOR_CACHE_BASE / "com.google.code.findbugs" / "jsr305" / "3.0.2" / "25ea2e8b0c338a877313bd4672d3fe056ea78f0d" / "jsr305-3.0.2.jar",
    _MCREATOR_CACHE_BASE / "org.checkerframework" / "checker-qual" / "3.43.0" / "9425eee39e56b116d2b998b7c2cebcbd11a3c98b" / "checker-qual-3.43.0.jar",
    _MCREATOR_CACHE_BASE / "com.google.j2objc" / "j2objc-annotations" / "3.0.0" / "7399e65dd7e9ff3404f4535b2f017093bdb134c7" / "j2objc-annotations-3.0.0.jar",
]