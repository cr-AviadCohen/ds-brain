Meta ~~-~~ Threat Intelligence Algorithm


Author: @Tal Waitzenberg (Deactivated) ~~-~~ for questions and help contact me via mail





Design a high performance Threat Intelligence classifier ~~.~~ The Meta model is divided into 2 phases, phase one a binary


(malicious/benign) classifier and phase two a multi ~~-~~ class classifier ~~.~~ Meta is a configuration based model that can be


configured and controlled by a configuration file (json format) ~~.~~


Algorithm Description


The Meta threat intelligence algorithm consists of 2 phases and a pre ~~-~~ phase (choosing appropriate referees):


In this pre ~~-~~ phase we want to choose referees, referees are antivirus engines that we believe are not bad engines ~~.~~ By saying not bad we


mean that we don’t know if they are the best but we think they are suitable enough to count on ~~.~~ For this purpose we develop a new class


`VirusTotalReferees` which calculates the referees engines, by selecting engines that detected malicious files early and the detections


increased over a period of time ~~.~~ The selection is based on the highest F ~~-~~ beta score where beta is set to 0 ~~.~~ 5 ~~.~~

is



We also enriched our data set ~~.~~ As we realized that most of our trained data is malicious we decided to add records that we are almost sure

is



are benign data ~~.~~ We selected records that have a low number of positives and combined all our data to reduce the effect of low activity


engines with high precision ~~.~~


Phase one is responsible for classifying the VirusTotal reports as benign/malicious (binary classification) ~~.~~ This phase is built from a few key

is


is



Reading the data from vt_feed (BigQuery) ~~-~~ the query pull all reports with the correct file type (PDF of MS Docs) and selects the


scans


The query selects reports that their first_seen field is at least 30 days from today ~~.~~ This means that those reports are mature and the


number of positives is unlikely to change ~~.~~

is



Then the data from BigQuery is preprocessed:


Read the data in bulks for reducing memory consumption

in



Drop duplicates records by sha1 index


Parse verdict each bulk ~~-~~ converting the data to binary matrix where each row index is sha1 and each column is VT engine ~~.~~


Finally all the preprocessed data is combined together and dropped duplicates by sha1 index again ~~.~~


When the data is preprocessed we remove low activity vendors ~~.~~ Means vendors with activity of less than 5% of the data size is

is


is



Filling nan’s with false, the assumption that if we will fill the nan’s with false it won’t harm the engine precision (will affect only the recall) ~~.~~


Filtering reports (sha1’s) that their number of positives count is unique, we do that in order to split the data to train and test in a stratified


Splitting the data to Train set and Test set with ratio of 0.8 train and 0.2 test ~~.~~


Creating a VTAnaylzer instance with the referees we found and a grouping ratio of 0.025 ~~.~~ We picked this ratio by examining a range of


ratios from 0.01 ~~-~~ 0.05 ~~.~~ Our picked ration 0.025 is ensuring a reasonable variance in each number of positives ~~.~~ Means the ratio is


not too soft and not too aggressive ~~.~~


Fitting the VTAnaylzer with our Train set data ~~.~~


Predicting on the Test set data ~~.~~

in



Mapping the vendors to their matching groups that have been created by the trained VTAnalyzer ~~.~~

is



Normalizing the number of positives of each file ( sha1 ) ~~-~~ the grouping the have been created by the VTAnaylzer are groups that vote


the same for each file, therefore we want to reduce their effect because if one of the engine vote for a file the rest of the group will vote


the same ~~.~~ So in our view if the group consists of 3 vendors which means the number of positives of the file is at least 3 it should be

in



counted as at least one ~~.~~


that each file with a number of normalized positives less than the lower bound threshold is classified as benign and an upper bound


threshold that each file with a number of normalized positives greater than the upper bound threshold is classified as malicious ~~.~~


In order to pick the malicious score threshold for files that sits in the range between the normalized positives lower bound threshold and


the upper bound threshold, we want to clean outliers from each normalized positives dimension of the lower bound and the upper bound


Then we select a threshold for the malicious score which is the mean value of the maximum malicious score of the normalized positives


lower bound threshold and the minimum malicious score of the upper bound threshold ~~.~~


Each file which is in the range of the normalized positives and below the malicious score threshold is classified as benign and all files

is



above the threshold is classified as malicious ~~.~~


Classes score features calculation:


Create scoring features for each class, create a dictionary for each class that contains words that have high co ~~-~~ occurrences with the


specific class ~~.~~ To find those co ~~-~~ occurrences words we calculates the number of shared occurrences of the candidate word and the class


in all reports and divide it with the total occurrences of the candidate in all data ~~.~~

in


in



We assign the candidate word to a specific class if it fulfill the condition: find **​** the appearance percentage of the word in each class


if contained in one class more than the others and pass some threshold: assign to the most contained class

in



else: drop word ~~.~~


Virustotal tags by classes:

in


by



We group VT tags under the relevant class for each class int the multi classification tags according to security anlyasts ~~.~~ each group


represents the class tags feature, where the value of that feature is the sum of the tags that belongs to the same feautre group of the


current file (VT report) ~~.~~ so if we have 3 classes, for example snitch ( downloader, dropper and exploit ) you will have 3 tags


features where each feautre vector is the number of tags of the relevant class for each file ~~.~~


We are giving much more weight to the VT tags than the vendors tokens ~~-~~ we assume that the tags are more reliable ~~.~~











description: The positive upper bound to calculate


the maliciousness score (This number will indicate



description: The mlflow regisrty uri to store


port ~~-~~ or none for default mlflow uri ~~.~~


description: A flag if to store the model object in a








default value: "benign"



description: the model type that is stored in


BigQuery in order to pull the relevant model







description: The output label for a malicious


default value: "malicious"



description: The BiqQuery client name to use







description: The minimum distance between 2


AV’s that below it the AV’s will be considered echo


values: [0, 1]



description: {‘micro’, ‘macro’, ‘samples’,


‘weighted’, ‘binary’} or None, default=’binary’ (took



average='binary' and the data is binary ~~.~~ If the data


are multiclass or multilabel, this will be ignored;


setting labels=[pos_label] and average != 'binary'





1]





description: The minimum number of detections


to suspect the file as malicious ~~.~~ (less detections


values: [0, inf]







description: The maximum number of detections


to suspect the file as benign ~~.~~ (more detections


than that the file will be tagged as malicious) ~~.~~


values: [0, inf]



values: [0, inf]


description: The file path to load train data ~~-~~ local


description: A positive number to sample records


description: the strating date to pull data from db


in format % ~~Y-~~ %m ~~-~~ %d


description: the ending date to pull data from db


in format % ~~Y-~~ %m ~~-~~ %d


description: The minimun number of positives


allowed for VT files when pulling data from


description: the strating date to pull data from db


in format % ~~Y-~~ %m ~~-~~ %d



description: A dataset path in format of pickle to


description: The starting date to pull malicious


description: Determine the percentage of null


values: [0, 1]

1]



A complete binary file example: ginger



description: The mlflow experiment name to


required ~~-~~ to use mlflow









description: The mlflow tracking server uri ~~-~~ if


server is deployed the url and exposed port ~~-~~ or




description: The ending date to pull malicious


description: The starting date to pull benign data


from db in format % ~~Y-~~ %m ~~-~~ %d ~~.~~


description: The ending date to pull benign data


from db in format % ~~Y-~~ %m ~~-~~ %d ~~.~~




A complete multi ~~-~~ class file example: ginger




Additional Configuration Parameter for Multi ~~-~~ Classification Task:









description: The operator to perform on all sub ~~-~~


values: “all”, “any”



description: The confidence level to accept a


values: [0, 1]



description: The default\alternative label for a


sample that don't much to any of the classes ~~.~~


default value: “malicious”









1]



description: The multi ~~-~~ classification labels ~~.~~



description: A list of conditions with a structure





description: A dictionary that the keys are


features names and the values is the condition on


values: “bigger_than_one”,


“bigger_than_threshold_and_smaller_or_equal_to_o


ne” ~~.~~


description: A dictionary that the keys are the


multi ~~-~~ classification labels and the values are


dictionaries of List with all VT tags that related to



required conditions.list.item.label


description: The output label of this particular


