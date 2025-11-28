# Questions

The questionnaire:

- Consists of 15 questions, arranged in order of increasing complexity and abstraction, from basic "sanity checks" to abstract 
concepts such as dimensionality and complexity; 
- Covers a broad spectrum of ephys topics (e.g., spike-spike interactions, functional connectivity, phase locking, 
excitation–inhibition balance, intrinsic neuronal timescales, decoding, dimensionality, modularity, and signal complexity);
- Uses a common answer template for all questions, combining a forced-choice answer, quantitative estimates, and a short description of the analytical steps; 
- Collects meta-information about how each answer was obtained, including confidence, prior experience, and expected consensus among participants. 

The following information is collected for each question:

- 🧩 [Multiple-choice answers](#multiple-choice-answers)
- 📊 [Belief metrics](#belief-metrics)
- 🧮 [Quantitative estimates](#quantitative-estimates)
- 🧾 [Methods and code](#methods-and-code)

---
(multiple-choice-answers)=
## Multiple-choice answers

For each of the 15 questions, participants give a single multiple-choice answer. In most cases, the options are:

- **Brain area 1**
- **Brain area 2**
- **Brain area 3**
- **Not enough data / no differences**

Some questions compare **pairs** of brain areas or **trial segments**, so the options reflect that (e.g. “Brain area 1 ⇔ Brain area 2”, 
“Stim start ⇒ Outcome”, etc.). 

The questions are ordered from:

1. Basic sanity checks (e.g. mean firing rates, broadband LFP power);
2. Intermediate questions about specific events and interactions (e.g. ripple density, pairwise interactions, functional connectivity etc.);
3. More abstract questions about information, decoding, dimensionality, modularity, and neural complexity. 

---
(belief-metrics)=
## Belief metrics

For every question, participants rate three belief-related metrics on a 1–10 scale: 

- **Confidence in your answer** (1 = very low, 10 = very high)
- **Prior experience with the methods used** (1 = no experience, 10 = expert)
- **Expected consensus among participants** (1 = expect strong disagreement, 10 = expect strong agreement)

These ratings are provided **separately for each question**.

---
(quantitative-estimates)=

## Quantitative estimates

For each question, participants report the quantitative estimates that support their multiple-choice answer. The template is: 

- A small table with one row per relevant brain area or condition, including:

  - Mean value
  - 95% confidence interval
  - Units (e.g. Hz, events/min, bits, etc.)

For example, a typical table might look like:

- Brain Area | Mean | 95% C.I. | Units
- Area 1     |  …   |    …     |  …
- Area 2     |  …   |    …     |  …
- Area 3     |  …   |    …     |  …

Participants are free to choose how they compute these estimates (e.g. parametric vs. non-parametric, frequentist vs. Bayesian), 
as long as they describe it clearly in the methods section for that question.
Using a single central-tendency estimate (the mean) is limiting, but necessary to make estimates comparable. You are free to transform
the data as you best see fit.

---
(methods-and-code)=

## Methods and code

For each question, participants briefly explain **how** they reached their answer. 

They are asked to:

* Describe **inclusion/exclusion criteria** (e.g. which units, channels, time windows, trial types);
* Outline the **step-by-step analytical and statistical approach** (e.g. preprocessing, feature extraction, statistics, model fitting);
* Summarize the **key quantitative results** (e.g. effect sizes, confidence intervals, p-values or posterior intervals).

Participants are strongly encouraged to:

* Provide **code snippets** (Python, MATLAB, Julia, R, etc.) that implement their analysis; or
* If code cannot be shared, give a **clear, reproducible description** of the analysis pipeline.

The goal is that another participant, given the same data and the description/code, could in principle reproduce the answer.

---
(example-questions)=

## Example questions

The full questionnaire includes 15 questions. Here are some practical examples to illustrate the range and progression. 

1. **Basic sanity checks**

   - Q1. Which brain area has the lowest firing rate over the entire recording?

2. **Intermediate questions on specific/concrete phenomena**

   - Q3. Which brain area (if any) has the highest density of ripples?

3. **Abstract questions about information and complexity**

   - Q11. Which brain area contains most information about variable A?
   
These examples are illustrative; participants will see the full list of 15 questions in the questionnaire document. 

---
(time-commitment-and-expectations)=

## Time commitment and expectations

Participants are **only expected to answer questions on topics for which they have prior knowledge** 
and feel comfortable implementing or interpreting the relevant analyses. 
It is acceptable—and expected—that some questions will be skipped if they fall outside the participant’s expertise.

The total time commitment depends strongly on prior experience with similar datasets and on coding abilities, but is typically expected to be
**between ~20 and ~50 hours** in total.

---