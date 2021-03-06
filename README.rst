=====
Rally
=====

Introduction
------------

Rally is a Benchmark-as-a-Service project for OpenStack.

Rally is intended to provide the community with a benchmarking tool that is capable of performing **specific**, **complicated** and **reproducible** test cases on **real deployment** scenarios.

In the OpenStack ecosystem there are currently several tools that are helpful in carrying out the benchmarking process for an OpenStack deployment. To name a few, there are *DevStack* and *FUEL*, which are intended for deploying and managing OpenStack clouds, the *Tempest* testing framework which validates OpenStack APIs, some tracing facilities like *Tomograph* with *Zipkin*. The challenge, however, is to compile all these tools together on a reproducible basis. That can be a rather difficult task since the number of compute nodes in a practical deployment can easily be large and also because one may be willing to use many different deployment strategies that pursue different goals (e.g., while benchmarking the Nova Scheduler, one usually does not care of virtualization details, but is more concerned with the infrastructure topologies; while in other specific cases it may be the virtualization technology that matters). What Rally aims to do is Compile many already existing benchmarking facilities into one project, making it flexible to user requirements and ensuring the reproducibility of test results.


Architecture
------------

Rally is split into 4 main components:

1. **Deployment Engine**, which is responsible for processing and deploying VM images (using DevStack or FUEL according to user’s preferences). The engine can do one of the following:

    + deploy an Operating System (OS) on already existing VMs;
    + starting VMs from a VM image with pre-installed OS and OpenStack;
    + delpoying multiple VMs inside each OpenStack compute node based on a VM image.
2. **VM Provider**, which interacts with cloud provider-specific interfaces to load and destroy VM images;
3. **Benchmarking Tool**, which carries out the benchmarking process in several stages:

    + runs *Tempest* tests, reduced to 5-minute length (to save the usually expensive computing time);
    + runs the user-defined test scenarios (using the Rally testing framework);
    + collects all the test results and processes the by *Zipkin* tracer;
    + puts together a benchmarking report and stores it on the machine Rally was lauched on.
4. **Orchestrator**, which is the central component of the system. It uses the Deployment Engine, to run control and compute nodes, in addition to launching an OpenStack distribution. After that, it calls the Benchmarking Tool to start the benchmarking process.


Links
----------------------

Wiki page:

    https://wiki.openstack.org/wiki/Rally

Launchpad page:

    https://launchpad.net/rally

Code is hosted on github:

    https://github.com/stackforge/rally
