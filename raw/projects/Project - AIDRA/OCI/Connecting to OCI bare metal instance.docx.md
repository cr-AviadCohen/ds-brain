# Connecting to OCI bare metal instance.docx

main

Connecting to OCI bare metal instance

# Connecting to Server

# opens a persistent terminal session

*screen -S jupyterlab*

# SSH to the remote machine

*ssh -i /Users/aviad.cohen/Downloads/oci\_gpu\_machine.key opc@161.153.18.227*

## Installations of JupyterLab (once)

# Install UV (using brew or else)

# Create an virtual environment

*uv venv .venv*

*# export cuda devices*

export CUDA\_VISIBLE\_DEVICES="0,1,2,3,4,5,6,7"; conda (or python) activate jupyterlab425

# Activate virtual environment

*source .venv/bin/activate*

*# Install JupyterLab*

*Uv pip install jupyterlab*

## Start Jupyter Lab

# Start Jupyter Lab

jupyter lab --no-browser --port=8888

## Get TokenID

sudo systemctl status jupyterlab

![](data:image/png;base64...)

token=6de3823ea216680ad32c9a64ac43035d558505d3a4f461de

# Connecting the JupyterLab Server from Local Host

## Set Port Forwarding

* In a new terminal window

# Port forwarding from local to remote server

*ssh -i /Users/aviad.cohen/Downloads/oci\_gpu\_machine.key opc@161.153.18.227 -L 8888:localhost:8888*

## On Browser

<http://localhost:8888/?token=><token you got above>

<http://localhost:8888/?token=>6de3823ea216680ad32c9a64ac43035d558505d3a4f461de

archive

**OCI**

# opens a persistent terminal session

*screen -S jupyterlab*

# SSH to the remote machine

*ssh -i /Users/aviad.cohen/Downloads/oci\_gpu\_machine.key opc@161.153.18.227*

# Install UV

# Create an virtual environment

*uv venv .venv*

*# export cuda devices*

export CUDA\_VISIBLE\_DEVICES="0,1,2,3,4,5,6,7"; conda (or python) activate jupyterlab425

# Activate virtual environment

*source .venv/bin/activate*

##Start Jupyter Lab

jupyter lab --no-browser --port=8888

——————————

In a new tab

# Port forwarding from local to remote server

*ssh -i /Users/aviad.cohen/Downloads/oci\_gpu\_machine.key opc@161.153.18.227 -L 8888:localhost:8888*

*————*

In another tab, connect to the server:

Jupyter server list

http://localhost:8888/?token=6de3823ea216680ad32c9a64ac43035d558505d3a4f461de :: /home/opc/.venv/etc/jupyter

———————
