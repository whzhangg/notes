#!/bin/bash

# this script simply create a symbolic link of the latex folder to
# obsidian vaults

vault="/obsidian_vaults/wenhao's Brain"
current=$(pwd)

target=$current$vault
source="$current/Latex Notes"

echo $source
echo $target

ln -s "$source" "$target"