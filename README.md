<p align="center">
    <img src="./docs/images/logo_rostok_long.png" width="600">
</p>


# Rostok

Rostok is an open source Python framework for generative design of linkage mechanisms for robotic purposes. It provides a framework to describe mechanisms as a graph, set an environment, perform simulation of generated mechanisms, get a reward as a quantitative value of the generated design, and search for the best possible design.

A user can utilize the entire framework as a pipeline to generate a set of suboptimal designs, or utilize the modules and submodules as independent parts. The framework allows to implement custom generative rules, modify search and optimization algorithms.

Currently the framework allows to perform co-design of open chain linkage mechanisms. Co-design consists in simultaneously searching for the mechanical structure and the trajectories of the robot to get the best possible performance.

<p align="center">
    <img src="./docs/images/brick_anim.gif" width="700">
</p>

## Project desription

There are four main blocks:  

* Graph Grammar -- is needed for creation, modification, and extraction of the data from the graphs that contain the entire information of generated mechanisms
* Virtual Experiment -- is the simulation needed for quantitative analysis of the behavior  and performance of generated mechanisms specified by grammar graphs
* Trajectory Optimization -- finds suboptimal joint trajectories needed to efficiently perform the desired motion
* Search Algorithm -- looks for optimal graph to represent mechanism topology

![project_general](./docs/images/general_scheme.jpg)
![project_algorithm](./docs/images/Algorithm_shceme.jpg)

More detailed description of the [algorithms and methods](https://licaibeerlab.github.io/rostok/advanced_usage/algorithm.html).

## Prerequisites

* Anaconda3
* Usage of the Docker reqires installation of Х-server for Windows <https://sourceforge.net/projects/vcxsrv/>

## Installation in development mode

To modify the modules of the Rostok framework a user should install it in development mode:  

* Create the environment using `conda env create -f environment.yml`
* Activate the environment `rostok`  
* Install the package in development mode `pip3 install -e .`  

### Known issues

At some PC's one can see a problem with the tcl module `version conflict for package "Tcl": have 8.6.12, need exactly 8.6.10`, try to install tk 8.6.10 using `conda install tk=8.6.10`

After the installation of the package one can get an error `Original error was: DLL load failed while importing _multiarray_umath: The specified module could not be found`, try to reinstall numpy in the rostok environment

## Documentation

The description of the project and tutorials are available [at project website](https://licaibeerlab.github.io/rostok).

## Publications

* I. I. Borisov, E. E. Khornutov, D. V. Ivolga, N. A. Molchanov, I. A. Maksimov and S. A. Kolyubin, "Reconfigurable Underactuated Adaptive Gripper Designed by Morphological Computation," 2022 International Conference on Robotics and Automation (ICRA), 2022, pp. 1130-1136, doi: 10.1109/ICRA46639.2022.9811738.

## Examples

An example of configuration and usage of the generative pipeline is in `rostok\app` directory.  
Examples of usage of independent modules is in `rostok\examples` directory.

## Acknowledgments

<img src="./docs/images/logo.png" width="200">

### Affiliation

The framework was developed in [ITMO University](https://en.itmo.ru/).

### Developers

* Ivan Borisov - researcher
* Kirill Zharkov - team leader
* Yefim Osipov - developer
* Dmitriy Ivolga - developer
* Kirill Nasonov - developer
* Sergey Kolyubin - chief scientist
<!-- * Mikhail Chaikovskii - reaserch developer -->

## Contacts

* Ivan Borisov borisovii@itmo.ru for scientific aspects of the project
* Kirill Zharkov kdzharkov@itmo.ru for technical questions of the project
* Sergey Kolyubin s.kolyubin@itmo.ru for collaboration aspects
