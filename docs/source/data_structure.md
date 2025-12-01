# Data Structure

The [dataset](https://ibl-brain-wide-map-public.s3.amazonaws.com/index.html#resources/con2phys/):

- Consists of 18 compressed files, each corresponding to one of the 18 mice included in the dataset;
- Comprises single-unit activity (SUA) and local field potentials (LFP) recorded using a Neuropixels probe during a behavioral task;
- Task details and electrode placements are intentionally kept minimal to reduce biases and minimize workload;
- The data has been collected from 3 simultaneously recorded brain areas;
- Every recording includes LFP (≥20 channels) and SUA (≥5 units, total of 1449 units) signals from each brain area;
- The length of the recordings varies between 55 and 101 minutes.

For each mouse, the following data is provided:  

- 📋 [Trial Data](#trial-data)
- 🧠 [Brain Area](#brain-area)
- ⚡ [Spikes](#spikes)
- 🔍 [Clusters](#clusters)
- 🌊 [Waveforms](#waveforms)
- 🌀 [LFP](#lfp)

---

(trial-data)=
## Trial Data

**Trial Data** (`.csv`) - a spreadsheet containing trial-specific information, all aligned with the ephys data:
- **`trial_start`** (s): Trial onset.
- **`stim_start`** (s): Stimulus presentation.
- **`outcome`** (s): Reward or punishment time.
- **`trial_end`** (s): Trial conclusion (the trial length is variable).
- **`Variable A`**: Binary qualitative behavioral variable.
- **`Variable B`**: Binary qualitative behavioral variable.
- **`Variable C`**: Qualitative behavioral variable (1–3).

---

(brain-area)=
## Brain Area

**Brain Area** (`.npy`, `.mat`):
- **`[1 × num_units]`** array with integer values (1–3), indicating the brain area in which a unit has been recorded.  
- **`[1 × num_units]`** array with integer values for cluster IDs.  

---

(spikes)=
## Spikes

**Spikes** (`.npy`, `.mat`):
- **`[1 × num_spikes]`** array with spike times (s).  

---

(clusters)=
## Clusters

**Clusters** (`.npy`, `.mat`):
- **`[1 × num_spikes]`** array linking each spike to a cluster ID.  

---

(waveforms)=
## Waveforms

**Waveforms** (`.npy`, `.mat`):
- **`[num_units × 128]`** array of average waveforms for each unit, recorded at 30 kHz on the best detection channel.  
- The order of waveforms matches that of cluster IDs and brain areas in `brain_area`.  

---

(lfp)=
## LFP

**LFP** (`.npy`, `.mat`):
- `lfp1`, `lfp2`, `lfp3` each contain `[num_channels × timestamps]` arrays of LFP signals.  
- The number of channels varies from brain area to brain and from mouse to mouse. The minimum number of channels per brain area is 20.  
- Channels within a brain area are contiguous in space, but channels from different brain areas are not.  
- Channels within a brain area are ordered from the deepest to the most superficial with respect to the brain surface.  
- The dataset comprises one channel every two that have been recorded on the Neuropixel probe. The vertical spacing between recording sites is 20µM  
- The signal has been recorded with an external reference and has already undergone a preprocessing pipeline.  
- Sampling rate: 500 Hz.  

---