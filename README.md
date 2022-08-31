# Z-Roads

This repository contains a Python script (ZRoads_CNN_prediction.py) and the corresponding trained models to make predictions regarding new imagery, implemented on the [Z-Roads project](https://medium.com/frontier-technology-livestreaming/case-study-machine-learning-for-classifying-road-conditions-in-tanzania-95d186a0451e): "Machine learning for classifying road conditions in Tanzania". This work was created in partnership with FTL, DfID and the Zanzibar Department of Roads. Four trained predictions models are  made openly available here:

1. The model trained all available imagery (this is what the script will use by default)

2. Three additional models, one per evaluation fold used to arrive at the results discussed in the report and in the Medium posts (linked below)

These models can be employed to consider new imagery. Sadly, a fully automated training pipeline, through which to generate /new/ models, is not currently producible due to the significant challenges faced in processing input data, that led to several manual interventions (please see details in the accompany blogs below). Due to issues faced in "stitching" drone imagery by the data generator (in turn due account of lack of geo-referencing in the data), the Z-roads project had to implement several non-automated steps to translate imagery data and models into an effective state. Many of these steps are specific to the challenges with this particular drone imagery dataset (including an extensive quality control filtering process, road network realignment, and image de-warping). For more details please contact the team / see the technical report.

The drone imagery used in the project can be examined here [here](https://opendri.org/project/zanzibar/). Organisations who have been granted permission to use the project's dataset are encouraged to contact with us if they have any further questions about the pipeline, after reading the project's technil report and accompanying Medium posts (which detail the processing challenges and recommended solutions).

The project is detailed as part of a four part blog post on Medium:

Part 1: [Machine Learning for Road Condition Analysis Part 1: Partnerships](https://medium.com/frontier-technology-livestreaming/machine-learning-for-road-condition-analysis-part-1-partnerships-f625caf970a9)

Part 2: [When Data Attacks: The challenges of using drones for AI](https://medium.com/frontier-technology-livestreaming/machine-learning-for-road-condition-analysis-part-2-when-data-attacks-645cd01a763f)

Part 3: No-Surrender Machine Learning: a real-world AI workflow [Available shortly]

Part 4: Turning Models into Interfaces: the Z-Roads system [Available shortly]

The full report is available on request.

A demonstration version of the road condition system is [available online](http://www.cs.nott.ac.uk/~pszgss/zroads/). If you would like access please contact us.

Contact details:  
Dr. Gavin Smith  
gavin.smith@nottingham.ac.uk

Dr. James Goulding  
james.goulding@nottingham.ac.uk  

Dr. Bertrand Perrat  
(now at Huawei, Edinburgh)

