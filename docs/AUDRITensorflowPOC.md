# AUDRI Tensorflow - Proof of Concept
## Details
This involves identifying methods and guidelines for the implementation of AUDRI using Tensorflow.
## Deliverables 

Preparation for coding using Tensorflow and IRL

Initial code in place (untested)
## Requirements
Coding in place (testing) 

 - First attempt code
  
 - Able to access training data
  
 - Able to generate reward function using training data
  
 - Able to access controls for vehicle control 
	
Initial Training data (testing)

 - Vehicle State (State crashed to be used to mark the end/restart of a drive)
    	
 - Actions depend on position in road, and other vehicle positions
	
 - New set of data generated per simulator frame 
	
Generate reward function based on training data

 - Use state crashed to calculate reward function
	
Generate random training data 

 - Could be generated using a different algorithm and fed into AUDRI 

## Potential Additions/Changes
 - Additional Positions

 - Additional Actions 
 
 - Access to training data may change
