# How to Participate

## Step 1: Download the data and the questionnaire
You can download all the data from this [repo](https://ibl-brain-wide-map-public.s3.amazonaws.com/index.html#resources/con2phys/)*. 
Data is available as `.npy` or `.mat`. The total size is roughly 29 Gb.
If you download the `.npy` version of the dataset, in the same repo you'll also find a few scripts to make sure that you 
downloaded the entire dataset. A full description of the dataset is availabe in [Data Structure](data_structure.md).

Download the questionnaire from [here](_static/questionnaire.pdf).

*the IBL has been so kind as to support us for data hosting. **This does not mean that the dataset is an IBL dataset**

## Step 2: Run the analysis  
Answer the questions provided in `questionnaire.pdf` using **your usual pipeline**, your preferred tools, you usual hyper-parameters, and your usual assumtions.
If your routine uses LLMs, you are allowed to use them to answer the questions. However, we reserve the right to reject low-effort contributions 
in which participants have mindlessly used LLMs with little to no intellectual contribution.

You do not have to answer all the 15 questions, it is enough if you answer the questions with which you have solid prior experience.

## Step 3: Filling out the questionnaire
The questionnaire consists of 15 high-level conceptual questions related to neural data recorded with Neuropixels probes 
from three anonymized brain areas (Area 1, 2, and 3) of 18 mice carrying out an unspecified behavioral task. 
All the data and the information needed to answer the questions is available in [Data Structure](data_structure.md).

You will answer by selecting one of four multiple-choice options and briefly giving the quantitative estimates that you used 
(mean and 95% C.I. - you can transform the data if you think that the mean is not an appropriate measure of central tendency). 
Each question also includes a couple of multiple-choice meta-questions about your confidence in the answer you provided. 
Lastly, while optional, we strongly encourage to submit also a brief explanation (~2-5 sentences) of how you arrived at your answer 
(preferably, **a snippet of the code you used**).

You only need to answer questions about concepts with which you have direct, prior experience. 
You are not required to answer every question, and we do not expect that you will have to learn new analytical concepts to participate in the study.

We put an emphasys on reducing to a minimum the complexity of meta-data and data manipulation. 
We estimate that, depending on your coding skills, the project should take you between 20 and 50 hours of work. Not much for a publication (see below)!  

## Step 4: Submit your results  
Once your analysis is complete, simply submit `questionnaire.pdf` to xxx (put an email address here or github repo?). That's it, you're done. 

For what happens next, please see [Contributions and Manuscript](contribution_and_manuscript.md)

## Important details  
- All participants start from **the same dataset**; differentiation comes from **your tools and choices**.  
- The questions are intentionally underspecified to expose interpretive variability.  
- **The goal is not to see who is right and who is wrong**. The overwhelming majority of questions have no ground-truth "correct" answer.
The goal is to analyze whether our (potentially different) implementations of the same concepts lead to different results. And if they do,
understand which details really make a difference.

---