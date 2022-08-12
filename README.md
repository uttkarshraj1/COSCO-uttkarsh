<h1 align="center">Enhancing QoS score for Fog Computing</h1>
<div align="center">
  <a href="https://github.com/uttkarshraj1/COSCO-uttkarsh/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203--Clause-red.svg" alt="License">
  </a>
   <a>
    <img src="https://img.shields.io/badge/python-3.7%20%7C%203.8-blue.svg" alt="Python 3.7, 3.8">
  </a>
   <a>
    <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fimperial-qore%2FCOSCO&count_bg=%23FFC401&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false" alt="Hits">
  </a>
   <a href="https://github.com/imperial-qore/COSCO/actions">
    <img src="https://github.com/imperial-qore/SimpleFogSim/workflows/DeFog-Benchmarks/badge.svg" alt="Actions Status">
  </a>
  </a>
   <a href="https://doi.org/10.5281/zenodo.4897944">
    <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.4897944.svg" alt="Zenodo">
  </a>
 <br>
   <a>
    <img src="https://img.shields.io/docker/pulls/shreshthtuli/yolo?label=docker%20pulls%3A%20yolo" alt="Docker pulls yolo">
  </a>
   <a>
    <img src="https://img.shields.io/docker/pulls/shreshthtuli/pocketsphinx?label=docker%20pulls%3A%20pocketsphinx" alt="Docker pulls pocketsphinx">
  </a>
   <a>
    <img src="https://img.shields.io/docker/pulls/shreshthtuli/aeneas?label=docker%20pulls%3A%20aeneas" alt="Docker pulls aeneas">
  </a>
 <br>
   <a href="https://gitpod.io/#https://github.com/uttkarshraj1/COSCO-uttkarsh/">
    <img src="https://gitpod.io/button/open-in-gitpod.svg" alt="Open in gitpod">
  </a>
</div>

COSCO is an AI based coupled-simulation and container orchestration framework for integrated Edge, Fog and Cloud Computing Environments. It's a simple python based software solution, where academics or practitioners can develop, simulate, test and deploy their scheduling policies. Further, this repo presents a novel gradient-based optimization strategy using deep neural networks as surrogate functions and co-simulations to facilitate decision making. A tutorial of the COSCO framework was presented at the International Conference of Performance Engineering (ICPE) 2022. Recording available [here](https://youtu.be/osjpaNmkm_w).

<img src="https://github.com/imperial-qore/COSCO/blob/master/wiki/COSCO.jpg" width="900" align="middle">


## Advantages of Multi_Simulation technique
1. Hassle free development of AI based scheduling algorithms in integrated edge, fog and cloud infrastructures.
2. Provides seamless integration of scheduling policies with simulated back-end for enhanced decision making.
3. Supports container migration physical deployments (not supported by other frameworks) using CRIU utility.
4. Multiple deployment support as per needs of the developers. (Vagrant VM testbed, VLAN Fog environment, Cloud based deployment using Azure/AWS/OpenStack)
5. Equipped with a smart real-time graph generation of utilization metrics using InfluxDB and Grafana.
6. Real time metrics monitoring, logging and consolidated graph generation using custom Stats logger.

The basic architecture of COSCO has two main packages: <br>
**Simulator:** It's a discrete event simulator and runs in a standalone system. <br>
**Framework:** It’s a kind of tool to test the scheduling algorithms in a physical(real time) fog/cloud environment with real world applications.




## Novel Scheduling Algorithms
We present two 


## Quick Start Guide
To run the COSCO framework, install required packages using
```bash
python3 install.py
```
To run the code with the required scheduler, modify line 106 of `main.py` to one of the several options including LRMMTR, RF, RL, RM, Random, RLRMMTR, TMCR, TMMR, TMMTR, GA, GOBI.
```python
scheduler = GOBIScheduler('energy_latency_'+str(HOSTS))
```

To run the simulator, use the following command
```bash
python3 main.py
```


