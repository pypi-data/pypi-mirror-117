#!/bin/bash

set -e

dirname=$(readlink -f "$(dirname "$0")")
project_folder=$(readlink -f "$dirname/..")

env=$1
if [[ $env = "" ]]; then
    echo >&2 "! You need to specify an environment for which you want to create an virtualenv"
    echo >&2 "! Usage: '<command> environment_name'"
    echo >&2 "! Example: '<command> local'"
    exit 1
fi

if [[ $VIRTUAL_ENV != "" ]]; then
  echo >&2 "! You are in a virtualenv: $VIRTUAL_ENV"
  echo >&2 "! Use deactivate first, and retry"
    exit 1
fi

function ask_for_permission {
    while true; do
        read -rp "[Y]es/[n]o? " yn
        case $yn in
            [Yy]* | "" ) break;;
            [Nn]* )  echo >&2 "Cancelling"; exit 1;;
            * ) ;;
        esac
    done
}


venv=$project_folder/.env_$env
if [[ -d $venv ]]; then
  echo >&2 "! Virtualenv already exists at $venv"
  echo >&2 "! You can already activate it."
  echo >&2 "! Do you want to delete the folder and create it again?"
  ask_for_permission
  rm -rf "$venv";
fi


python_version=3.6
default_python_exec=python$python_version
if [[ $2 = "" ]]; then
  python=$(which "$default_python_exec" || true)
  if [[ $python = "" ]]; then
    python_version=3.6.3
    python_remote_location=https://www.python.org/ftp/python/$python_version/Python-$python_version.tgz

    python_source_location=$project_folder/.python
    python_location=$python_source_location/Python-$python_version
    python=$python_location/python
    echo >&2 "! WARNING: Python 3.6 is not in your path whereas it is a requirement."

    if [[ ! -f $python ]]; then
      echo >&2 "! Do you want to install a version locally?"
      echo >&2 "! From $python_remote_location"
      echo >&2 "! To $python_location"
      echo >&2 "! You can also use <command> $env /path/to/python3.6"
      ask_for_permission
      echo "Downloading Python $python_version in $python_source_location"
      current_dir=$PWD
      rm -r "$python_location" || true
      mkdir -p "$python_location"
      cd "$python_source_location"
      wget "$python_remote_location"
      tar xfz "Python-$python_version.tgz"
      rm "Python-$python_version.tgz"
      cd "$python_location"
      echo "Running ./configure for Python $python_version"
      ./configure
      echo "Running make for Python $python_version"
      make
      cd "$current_dir"
    else
      echo "Python $python_version was previously installed in $python_source_location, will use it"
    fi
  fi
else
  python=$2
fi

# Main install
#
"$python" -m venv "$venv"
if [[ $python_location = ""  ]]; then
  lib_python_36_location=$(locate libpython3.6m.a | head -n 1)
  if [[ $lib_python_36_location = ""  ]]; then
    lib_python_36_location=${python%/*}/libpython3.6m.a
    while [[ ! -f $lib_python_36_location ]];
    do
      echo >&2 "! uwsgi requires  a file named libpython3.6m.a which is often located in \$PYTHON_HOME/libpython3.6m.a"
      echo >&2 "! we were not able to find it in $lib_python_36_location"
      read -rp "Where is the file located? " lib_python_36_location
    done
  fi
else
  lib_python_36_location=$python_location/libpython3.6m.a
fi
######### Work around for uswgi ############
mkdir "$venv/lib/python3.6/config-3.6m"
cp "$lib_python_36_location" "$venv/lib/python3.6/config-3.6m"


source "$venv/bin/activate"
python "$venv/bin/pip" install --upgrade pip
python "$venv/bin/pip" install -e .["$env"]

echo
echo "* Finished, now you should do:"
echo "source $venv/bin/activate"
