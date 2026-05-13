# CrossGuard: NGAV Binary Classifier ⚔️

CrossGuard is endpoint protection technology for static detection of malicious Windows PE binaries before their


execution ~~.~~ It is based on applying Machine Learning algorithms on a large set of manually engineered features and


relies on various tangent efforts for developing data sets, evaluation methods and technical infrastructure ~~.~~ It is at


the core of our VirusTotal scanning engine and the upcoming Cybereason PROTECT endpoint protection product ~~.~~


TOC


Sklearn transform ~~-~~ predict pipeline


Step 2: pre ~~-~~ process


Extracting the model information for PROTECT


Practical Information


is many times referred to simply as "ngav" or נגב, or as "static analysis"


has its research python code in [research](https://github.com/cybereason-labs/research) repo under 'ngav' package



with some engineering C++ code in





is continuously built in Jenkins (irelease) at




To train a production model:


launch ngav ~~-~~ ci ~~-~~ pipeline with "master" as SCM_BRANCH,


version (as seen at the end of ngav ~~-~~ train ~~-~~ [build](http://irelease:8080/view/Projects/view/ngav/job/ngav-train-build-python/) ~~-~~ python's console output) such as 0.0.1060






Next ~~-~~ gen AV is at its best when it detects and prevents threats pre ~~-~~ execution on a single offline endpoint ~~.~~ We went

it



with ML to get a meaningful product out there as fast as possible ~~.~~





(security performance objectives)




VirusTotal provider ("VT box"):



internal doc →





Objective: build a service that would add "Cybereason" to Virus Total, saying "malicious" or "benign", and being


good enough so as not to embarrass our brand


Motivation: we need a VT scanner to keep using VT's feed ~~.~~ We also wanted some publicity boost by being there,


but apparently that ship has sailed with too many new additions


Current assumptions and limitations


We run on Windows only


We scan EXE binaries (no DLLs yet)


We have BitDefender scanner at our disposal to use as we will


We are not relying yet on enterprise contextual data (statistics etc)


We use one product for all customers, i ~~.~~ e ~~.~~ we don't tailor ~~-~~ train


Data path


Very high level overview of the data path involved in training and evaluating a model:


Source for diagram:



~~https://www.draw.io/#G1X_JqwRgExiZq0pIstJd-Da6c9BouR8v1~~



VT ~~-~~ feed indexing


This process was built for CrossGuard but is actually an independent research process ~~.~~ It involves a couple of AWS


lambdas working in unison to consume the VT [Feed](https://www.virustotal.com/en/documentation/private-api/#file-feed) API and save all reports and binary (EXE+DLL) samples to S3,


and an on ~~-~~ demand script that creates daily V ~~T-~~ index files that provide a concentrated way of choosing samples for


further processing ~~.~~ Note that the indexing aspect is very much in parallel to [InnovationDB,](https://cybereason.atlassian.net/wiki/spaces/IN/pages/160891017) so use whatever's more


First day of reliable EXE data is 10/FEB/201 ~~7.~~ First day of reliable DLL data is 10/MAR/201 ~~7.~~


Technical details:


scans all the VT feed report json files from S3 over a date range and creates msgz index files (one per day)


calculates labels using both Cruvit and Broccoli for every sample


under perrylab, indexes are occasionally updated under /data/vtindex/latest


for more information: python -m ngav.vtindex.create_index --help


running behind the scenes to collect data used by the above script


you don't interact with them directly


deployed using serverless framework from code that lives in research repo under "ngav/apps/ngav ~~-~~


triggered once every minute, and each time looks into the VT feed from one hour ago (a safety buffer)


reads each minute's feeds and saves its reports to S3, and triggers the next lambda to download new


data is saved (e ~~.~~ g ~~.~~ for 2017/12/31 18:05) under s3://cybereason ~~-~~ labs/vt ~~-~~ feed ~~-~~ storage ~~-~~


prod/20171231/20171231T18/20171231T1805/ ~~...~~


the file "jsons" contains all reports (one flat json per line, includes docs, MacOS, ELF, ps1 ~~...~~ )


the file "jsons_of_peexes" contains reports of Win PE EXE files (thus tagged)


the file "jsons_of_pedlls" contains reports of Win PE DLL files (thus tagged)


the file "metadata ~~.~~ json" contains a summary of the lambda's results


useful metrics are reported to cloudwatch


downloads new binaries encountered in the feed consumption


binaries are saved to s3://cybereason ~~-~~ labs/vt ~~-~~ feed ~~-~~ storage ~~-~~ prod/samples/<sha1>


useful metrics are reported to cloudwatch


Dataset building


Once we have convenient indexed access to VT files, we can sample ourselves a dataset for training or evaluation


(reporting) purposes ~~.~~ This is done using the build_dataset script ~~.~~


Properties of a selected sample set:


contains the specified number of rows


spread evenly across the specified date range (inclusive)


with unique samples (for training) or with duplicates (for reporting)


Running the script creates four files (name based on ~~--~~ out ~~-~~ name parameter):




a pickled pandas Index object with "s3://cybereason ~~-~~ labs/vt ~~-~~ feed ~~-~~ storage ~~-~~ prod/samples/<sha1>" values





the rows from the original VT index data (previous step) containing report metadata, submission information,


engine scan results and label values






note that the labels filename is derived from the ~~--~~ label parameter (i ~~.~~ e ~~.~~ would be





a pickled series detailing for each unique sample how many times is was scanned (individual report count)


within the specified date range


specify either ~~--~~ for ~~-~~ training (to get a 50:50 malicious:benign ratio) or ~~--~~ for ~~-~~ dncreport (to get a fixed


random amount per day without skewing natural rates)


also, a selection for training is unique by sha1, whereas a selection for reporting may contain duplicates


specify zero or more conditions:


specify ~~--~~ cond ~~-~~ post ~~-~~ bd to avoid selecting all those that VT's BD scan detects as malicious


specify ~~--~~ cond ~~-~~ stark ~~-~~ labels to avoid selecting any sample labeled as "unwanted" by the chosen label


specify ~~--~~ cond ~~-~~ dotnet to select only samples having the "assembly" tag (good for dotnet research)


specify ~~--~~ label to select the VT classifier you want to use for your label (default is broccoli in recent code


versions, so stay with the default)


specify ~~--~~ from for the location of the "VT index" from the previous step (if you're running on perrylab, the


default will just work)


Feature generation


If the heart of the pipline is the prediction algorithm, then features are the lungs, liver and at least one of the


kidneys ~~.~~ Our feature generation process is basically a function from a buffer of bytes (the PE file contents) into a


dictionary (or Series, or a row in a DataFrame) of feature ~~-~~ to ~~-~~ value assignments ~~.~~





To run the feature generation process for production purposes, use the jenkins job ngav ~~-~~ [generate](http://irelease:8080/view/Projects/view/ngav/job/ngav-generate-features/) ~~-~~ features ~~.~~ You will


be asked to provide the task name regex (to specify which data set you want to generate on, and with which


parameters etc) and the already ~~-~~ built ngav code version to generate features with ~~.~~ Normally though, you'll be


running the entire pipeline at once (see below at the section dedicated for production Jenkins pipeline usage) ~~.~~


There are several parts to the feature generation process:


the script that triggers generation of features


the infrastructure for feature generation (which started out as a crossguard thing, but became an infra for several


the actual domain ~~-~~ specific individual features generation code


Documenting the features themselves is beyond the scope of this article ~~.~~ They are most accurately documented in



the research repo under ngav/classify/features ~~.~~ They are also documented extensively in and under







(note: documentation will naturally always remain a bit behind the python code) ~~.~~




pe_sections_code_entropy : entropy for the aggregate of all code ~~-~~ containing PE sections (numeric)


yara_rules_yara_matches : which individual yara rules (bundled with our features code) were matched on


the file data (multi ~~-~~ categorical)


digital_signature_signature_status : the verification status of the digital signature, if exists (single ~~-~~


The featuresinfra top ~~-~~ level package is small but relatively flexible ~~.~~ It deserves its own documentation, but


roughly it let's you write feature sets like this:



it





And then have them sets aggregated hierarchically like so:





So that running my_features(file_data) will generate a dictionary of features:





The featuregen script can be found under crossguard/features/featuregen in the research repo ~~.~~


It is launched using the package ~~-~~ level crossguard launcher ~~.~~


The script itself is nothing fancy ~~.~~ Here is what it can do for you:

it



it takes a file ( .pkl, .idx, .msgz etc) containing an Index or an Indexed object


it expects the values on the Index to be strings, where each one is in one of these sample formats:





best format, uses any available S3 sources and goes to VT if not found, and caches back results (if you


have permissions) in S3







it



any S3 URL works here (depending on your permissions)


vt://0cef4d21fb891033f5e9a68ffbe9abada9682d791eb2f06099203be6086f862b


any V ~~T-~~ approved hash works here (MD5, SHA ~~-~~ 1, SHA ~~-~~ 256)


the path to a local binary filename


it generates features in multiprocessing (deafult is use all cores, but ~~--~~ n ~~-~~ jobs is your friend)

it



it saves the results into a time ~~-~~ stamped file:





it



the pickle file will contain a dataframe whose index reflects the samples (as originally specified) and whose


columns represent the features


feature values are numeric (for numeric features) or either np.nan or None or a list or tuple of zero or more


category values (for single ~~-~~ or multi ~~-~~ categorical features)


Model Training


Given a nice pickled dataframe of features, generated from either the python pipeline or the C++ PROTECT


processes, we can take a bunch of objective parameters and train ourselves a predictive model ~~.~~


Sklearn transform ~~-~~ predict pipeline


The "model" is actually a pickled series of steps made of transformers followed by a predictor:


Source for diagram:



~~https://www.draw.io/#G1X_JqwRgExiZq0pIstJd-Da6c9BouR8v1~~



Implemented at crossguard.train.trainer.NgavTrainer._cleanup


Drops columns that are completely null ("bad features")


Marks rows that have null values in non ~~-~~ categorical feature columns as invalid


A SampleSplitter sends invalid rows to a fixed "error" ~~-~~ labeler


All valid rows continue onwards


Step 2: pre ~~-~~ process


Implemented at crossguard.train.trainer.NgavTrainer._preprocess


Processes raw featurs into a matrix of flat numeric values ready for classification


For multi ~~-~~ categorical features:


Use ManyHotEncoder to hot ~~-~~ encode the features into boolean columns


For other features (numeric or boolean):


Convert them into float columns (doesn't really do much, just a technical step)


After this step our DataFrame has been transformed into a sparse csr_matrix


Implemented at crossguard.train.trainer.NgavTrainer._classify


Our classifier is a ThresholdCompositeClassifier that wraps a LightGBMClassifier


The inner LightGBMClassifier trains to provide the probability for malicious classification according to the


training set samples


In inference time it predicts malicious probability

it



The outer ThresholdCompositeClassifier saves 12 ~~.~~ 5% of the training set aside for calibrating the


conviction probability threshold according to the given precision goal


In inference time it's taking the malicious probability and makes a final "malicious / benign" decision


Training is usually done by running the script "train_model ~~.~~ py" ~~.~~


Basic usage flags:


The " ~~--~~ labels" flag lets you specify the file where your labels are


The " ~~--~~ target ~~-~~ precision" flag lets you specify the precision according to which


Advanced flags:


The " ~~--~~ training ~~-~~ lambda" flag lets you change the malicious:benign ratio in the training set


The " ~~--~~ world ~~-~~ lambda" flag lets you specify the real ~~-~~ world malicious:benign ratio, so that the effective training


precision target is correctly set (important!)


In return you will get a few files:


ngav_model.<timestamp>.training_set.pkl ~~-~~ a dump of the actual training set data used (if sampled or


had lambda adjustments, this is post this sampling)


ngav_model.<timestamp>.labels.pkl ~~-~~ the labels that were used, aligned to the training set above


ngav_model.<timestamp>.trainer.pkl ~~-~~ the NgavTrainer object that was used to construct the classifier


(note: this is not the classifier itself)


Extracting the model information for PROTECT


This part is still a bit under construction, but as long as you train a model and export it using the same version of the


ngav package, all will be well ~~.~~


python \-m ngav.protect.exportmodel \-\-help



it


This script will output three files ~~-~~ one for the model itself, one for the list of features, one for the conviction


threshold value ~~.~~


Prediction and reporting


There isn't much to be said about prediction ~~.~~ Basically, you generate features, and then you load the classifier from


its pickle (always the " *.classifier.pkl " file) and call predict() to get a verdict ~~.~~


Here is a nice script that does that:





Provide it with the model (" xxx.classifier.pkl " from train_model ) and vectors (" yyy.pkl " output from

it



generate_features ) and you'll be rewarded with a prediction pickle file and a bunch of printed statistics ~~.~~


Some more details:


give " ~~--~~ out ~~-~~ prediction" to receive a pickled dataframe of the results (otherwise you only see statistics)


if you give " ~~--~~ labels" and provide it with a zzz.vtindex.pkl file (e ~~.~~ g ~~.~~ one created with the build_dataset

it



script), then information about the confusion matrix of the results will be presented and you'll know something


about the quality of your results


if you give " ~~--~~ postbd" and provide it with a zzz.vtindex.pkl file, then Bitdefender's scan result from VT's

it



reports will be used to augment the ML prediction with the "signature based" layer of conviction (creating


another column in the output dataframe)



Main article:




take a random sample of VT submissions over some timeframe (see "Dataset Building" above),


and generate features for them (see "Feature Generation" above),


and predict them using your pre ~~-~~ trained classifier (see "Prediction and reporting" above),


then you can create pretty graphs to tell you how really objectively unbiased ~~-~~ ly good your classifier performs ~~.~~


A simple script takes the above ingredients and creates a PDF full of reports:


Reports generated are:


DNC report ("consensus ~~-~~ based" reporting)


Daily precision/recall report (assuming the labels, how did our results change over the timeframe of the dataset)


Proba predictive power report (for advanced usage)


Not all reports make sense for every dataset ~~.~~ For example, if your dataset is not spread over a timeframe, "daily


precision/recall report" is meaningless ~~.~~ Experiment and discover for best results ~~.~~


Production Jenkins pipeline


We all know that production code should be built in production Jenkins pipelines ~~.~~ Well, what about production ML


models? There's no reason they should be any different ~~.~~


The production pipeline covers the feature generation, model training and model evaluation (prediction +


performance reporting) stages of the data path ~~.~~


We use Jenkins for two distinct purposes: CI and production model generation ~~.~~ For the sake of simplicity, we'll just


describe here the production usage; CI is basically about doing the same in a very small scale to make sure the


code isn't broken, and could serve for production usage at any point ~~.~~


This is the production Jenkins pipeline:


Source:



~~http://irelease:8080/view/Projects/view/ngav/job/ngav-ci-pipeline/~~



The Jenkins aspects are owned and maintained by Release Engineering studio (led by @Shaked Shauli


(Unlicensed) ) ~~.~~ However, we own and maintain 99% of what happens inside the jobs ~~.~~


Usage instructions


It's actually pretty simple ~~.~~ Go to ngav ~~-~~ ci ~~-~~ pipeline, start a new build, and enter three parameters:


Keep SCM_BRANCH on master (told you, simple!)


Choose the "task set(s)" from the list below by entering a regexp


copy the recommended regexp from below, so you don't accidentally run too many task sets


Enter the ngav_version (e ~~.~~ g ~~.~~ 0.0.1060 )


it should be already built from your latest commit; look at ngav ~~-~~ train ~~-~~ [build](http://irelease:8080/view/Projects/view/ngav/job/ngav-train-build-python/) ~~-~~ python's latest console output to

it



see the latest number


don't leave it empty; if you do, it will just use the latest build, but then you won't know for sure which version

it



to use in production

it



For example, here is a typical execution:


Task sets are a way to configure the data set(s), the features generation and the model parameters to be used ~~.~~ It is


a potentially overly flexible, but if configured well, then using one of the recommended sets will give you exactly the


results you need ~~.~~ The actual specification of the task sets is saved in the research repo under "ngav/ci/ngavci ~~.~~ yml" ~~.~~


Reminder: copy paste the exact "task set regexp" string into the job you launch, to make sure you don't mess up


the things you're launching ~~.~~


generate features on ~1000 random vectors and train a small model ~~.~~ good for testing ~~.~~ runs for a few minutes ~~.~~


an aggressive model (more TP, more FP) trained on a very large post ~~-~~ bd dataset (400K samples collected over


180 days 10/Feb ~~-~~ 8/Aug), with 50:50 stark distribution ("don't care" about unwanted) and using broccoli labels


precision target of the ML layer on post ~~-~~ bd: 50%


WIP


a permissive model (less TP, less FP) trained on a very large post ~~-~~ bd dataset (400K samples collected over 180


days 10/Feb ~~-~~ 8/Aug), with 50:50 stark distribution ("don't care" about unwanted) and using broccoli labels


precision target of the ML layer on post ~~-~~ bd: 90%


Here are some technical tips for keeping the pipeline in good shape:


The pipeline runs by launching the same production scripts well ~~-~~ documented in previous sections ~~.~~


The pipeline jobs run on a dedicated slave ( lin ~~-~~ slave ~~-~~ agent ) ~~.~~


The pipeline orchestration code lives in the research repo under "ngav/ci" ~~.~~


The task sets are defined in the YAML file "ngav/ci/ngavci ~~.~~ yml" ~~.~~


Machine Learning highlights


Generally speaking, we employ two rounds of attempted ~~-~~ conviction ~~.~~ We use BitDefender as a first line of


conviction ("signature based") ~~.~~ BitDefender convictions are final and auto ~~-~~ accepted, no further processing needed ~~.~~


For all other samples, a second round of conviction is attempted using a machine learning model ~~.~~ This means that


this ML model only sees the part of the world that BD does not convict, in both training and production settings ~~-~~


what we refer to as "post BD" ~~.~~


Here are some fine points of the ML aspects of the project ~~.~~


We use a machine learning pipeline to train on known samples and build a model of "what is malicious" (out of


those that BD does not convict) ~~.~~


We apply this model in production to unknown samples and identify those that appear malicious ~~.~~


We set a predefined precision goal and select the model that gives the highest recall under this limitation (using


We generate raw deterministic features for each sample, based on only its binary content (context ~~-~~


When training a model, we technically transform sample features in whole training set context, e ~~.~~ g ~~.~~ drop rare


categorical values; but the context impact is thought to be negligible ~~.~~


Our core ML algirithm is a forest of decision trees that infer malicious probability for every sample, without


casting a final verdict ~~.~~


We only decide malicious/benign, and make no multiclass decisions (i ~~.~~ e ~~.~~ no ransomware/malware/unwanted


We train our model parameters using the [LightGBM](https://github.com/Microsoft/LightGBM) algorithm ~~.~~


We usually train on a set consisting of 50:50 malicious:benign samples ~~.~~


We usually train on a set containing only stark samples (badware vs indifferent, no unwanted) because any


answer on unwanted is okay ~~.~~


We label training samples based on their VT report using what broccoli would say ~~.~~


We keep aside a small part of the training set for setting the minimal threshold for malicious labeling, chosen to


satisfy the precision goal ~~.~~


~~We~~ ~~search~~ ~~for~~ ~~meta-parameters~~ ~~by~~ ~~random~~ ~~sampling~~ ~~from~~ ~~a~~ ~~given~~ ~~space~~ ~~and~~ ~~ranking~~ ~~using~~ ~~the~~ ~~perfect-~~


~~balance-score~~ ~~(penalizes~~ ~~linearly~~ ~~for~~ ~~low~~ ~~recall~~ ~~and~~ ~~exponentially~~ ~~for~~ ~~too-low~~ ~~precision).~~


We stopped doing this when we switched from ExtraTrees to LightGBM; we might resume in the future ~~.~~


We keep an entirely separate test ~~-~~ set for measuring our immediate results, mainly the precision/recall on the


malicious label ~~.~~


We measure our predictive parameters on a separate test set of a later timeframe to check continued relevance


as time passes ~~.~~


We generate DNC [reports](https://cybereason.atlassian.net/wiki/spaces/IN/pages/207454462) for the later timeframe dataset to evaluate our performance in the most unbiased way


We can report expected precision numbers for target environments whose benign vs ~~.~~ malicious ratios are


different than those we trained on ~~.~~ This is report ~~-~~ only and does not affect recall ~~.~~


If requested, we can set training precision goals that, when met, should result in the real precision goal on some


target environment ~~.~~ This allows us to train on arbitrary malicious:benign ratios ~~.~~


