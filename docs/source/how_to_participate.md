# How to Participate

## Step 1: Download the data and the questionnaire

You can download all the data from this [repository](https://ibl-brain-wide-map-public.s3.amazonaws.com/index.html#resources/con2phys/)*. 
Data is available as `.npy` or `.mat`. The total size of the dataset is roughly 29 GB.
If you download the `.npy` version of the dataset, you can use these [code snippets](/_static/code-snippets.zip) 
to check that you downloaded the entire dataset and start playing around with the data. 
A full description of the dataset is available in [Data Structure](data_structure.md).

Download the questionnaire from [here](/_static/questionnaire.pdf).

*The IBL has been so kind as to support us for data hosting. **This does not mean that the dataset is an IBL dataset.**

## Step 2: Run the analysis 
 
Answer the questions provided in `questionnaire.pdf` using **your usual pipeline**, your preferred tools, your usual hyperparameters, and your usual assumptions.
If your routine uses LLMs, you may use them to answer the questions. However, we reserve the right to reject low-effort contributions 
in which participants have mindlessly used LLMs with little to no intellectual contribution.

## Step 3: Fill out the questionnaire

The questionnaire consists of 15 high-level conceptual questions related to SUA and LFP data recorded with Neuropixels probes 
from three anonymized brain areas (Area 1, 2, and 3) of 18 mice carrying out an unspecified behavioral task. 
All data and information needed to answer the questions is described in [Data Structure](data_structure.md).

You will answer by selecting one of four multiple-choice options and briefly giving the quantitative estimates that you used. 
Each question also includes a couple of multiple-choice meta-questions about your confidence in the answer you provided. 
Lastly, while optional, we strongly encourage you to submit a brief explanation (~2-5 sentences) of how you arrived at your answer 
(preferably, **a snippet of the code you used**). A more thorough explanation of the questions is available in [Questions](questions.md).

You only need to answer questions about concepts with which you have direct, prior experience. We do not expect you to 
learn new analytical concepts to participate in the study.

We put an emphasis on minimizing the complexity of metadata and data manipulation. 
We estimate that, depending on your coding skills, the project should take you between 30 and 50 hours of work. Not much for a publication (see below)!  

## Step 4: Submit your results  
Once your analysis is complete, submit `questionnaire.pdf` and reply to the brief form as described in [Submit your answers](submissions.md).

For what happens next, please see [Contributions and Manuscript](contribution_and_manuscript.md).

## Important details  
- All participants start from **the same dataset**; differentiation comes from **your tools and choices**.  
- The questions are intentionally underspecified to expose interpretive variability.  
- **The goal is not to see who is right and who is wrong**. The overwhelming majority of questions have no ground-truth "correct" answer.
The goal is to analyze whether our (potentially different) implementations of the same concepts lead to different results. And if they do,
understand which details really make a difference.

---