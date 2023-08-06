# VaniDL

VaniDL is an tool for analyzing I/O patterns and behavior with Deep Learning Applications. It analyzes Darshan Extended traces to extract various I/O patterns with Deep Learning applications. The tool at it core uses vanidl which converts Darshan Profiler’s trace into knowledge for analysis. It is designed to provide low-level I/O behavior details to tensorflow applications in HPC. 

**VaniDL features include:**

-   Easy-to-use and understand high-level API for extracting I/O behavior of the applications.
-   Fast prototyping through highly modular data representation through pandas for easy plotting of graphs.
-   Full transparency over profiling data with access to internal data structures such as timeline of applications, aggregation functions, and drill up/down data views.
-   Powerful helper functions to build a visual understanding of how applications perform I/O such as request distributions, file access pattern, and extracting file specific summaries.
-   Easy to use File Summary and Job Summary extractors for understanding the data consumed by Deep Learning Applications
 

## Overview
```python
#Initialize class
profile = DLProfile()
#Load darshan file
status = profile.Load("./run1.darshan")
#Get Job Summary
summary = profile.GetSummary()
```

```python
#Application Timeline of data operations
tl = profile.CreateIOTimeline()
plt.figure(figsize=(20,4))
plt.grid()
plt.plot(tl['time_step'], tl['operation_count']);
```
![timeline](./images/IMG_0097.jpg)

More examples are [here](https://github.com/hariharan-devarajan/vanidl/tree/master/examples)

## Installation

### Requirements
- numpy==1.18.5
- pandas==1.0.4
- h5py==2.10.0
- tensorflow~=2.2.0

**VaniDL Installation**

To install VaniDL, the easiest way is to run

For the bleeding edge version (recommended):

```bash
pip install git+https://github.com/hariharan-devarajan/vanidl.git
```
For the latest stable version:
```bash
pip install vanidl
```
Otherwise, you can also install from source by running (from source folder):
```bash
python setup.py install
```
### On Theta
```bash
module load VaniDL
```
## Getting Started
See _[Getting Started with VaniDL](https://github.com/hariharan-devarajan/vanidl/wiki/Getting-Started)_ to learn about VaniDL basic functionalities or start browsing _[TFLearn APIs](https://github.com/hariharan-devarajan/vanidl/wiki/API)_.

### Examples
There are many examples of analysis available, see _[Examples](https://github.com/hariharan-devarajan/vanidl/tree/master/examples)_.

## Contributions
This is the first release of VaniDL, if you find any bug, please report it in the GitHub issues section.

Improvements and requests for new features are more than welcome! Do not hesitate to twist and tweak VaniDL, and send pull-requests.

For more info:  _[Contribute to VaniDL](https://github.com/hariharan-devarajan/vanidl/wiki/contributions)_.
## License

MIT License
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU4NTg3NDgzMywxMzI5MDI3OTYwLC0xNj
IyNTExMDMwLDg1MjY1NDIzMyw0MTI2MDY3NDYsLTE1MjczMDA1
MTVdfQ==
-->