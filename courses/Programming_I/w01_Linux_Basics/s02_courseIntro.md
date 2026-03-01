### Course Content

* w01 Linux Basics

* w02 Python Basics

* w03 Recitation I (Review+Test+QA)

* w04 Control Flow

* w05 Function Module

* w06 Recitation II (Review+Test+QA)

* w07 Data Structure

* w08 File Operations

* w09 Recitation III (Review+Test+QA)

* w10 Exception Handling

* w11 LLM API in Python + Final Project Team Work

* w12 Recitation IV (Review+Test+QA)

* w13 Intro to Libraries + Final Project Team Work

* w14 Intro to Concurrent Programming + Final Project Team Work

* w15 Final Presentation


<br>

---------------------------

###  Team Arrangement

1. In total, we have 5 teams (5-7 members per team).

2. We have multiple rounds of member selection.

3. In each round, each Team Lead will provide one offer to one member (you can reject the offer, and then the lead should turn to another one). 

4. For the final project, the maximum grade is 30 (final presentation). Team Lead can get 3 bonus points (10%).

5. If more than 5 people want to be the team lead, let’s vote for it. If less than 5 people want to be the lead, I will randomly assign the remaining team lead.

<br>

---------------------------

### Final Grade

* We use a quantile-based evaluation method to calculate the final grade (ranging from 0 to 100), which consists of three components:

1. General Performance,
2. Final Project
3. Total Test Score (recitation sessions).

* For each component, a student’s quantile within the entire cohort is calculated. Quantiles are calculated as percentiles (0 = lowest, 1.0 = highest) within the entire cohort. The Average Quantile (AQ) is then computed across all three components. If a student’s AQ is below 0.2, they will receive a “FAIL” grade. In addition, if the AQ is lower than 0.2 but the Actual Score (AS) on the Total Test Score exceeds passing line, the final grade will be marked as 60 (passed with a low final grade).

```
if AQ ≥ 0.2:
    Passed, Final Grade = (AQ – 0.2) / (AQmax – 0.2) × 40 + 60
else if AQ < 0.2 and Total Test Score ≥ Passing Line:
    Passed, Final Grade = 60
else if AQ < 0.2 and Total Test Score < Passing Line:
    Failed, Final Grade = AQ / 0.2 × 60

# Note: "AQmax" refers to the actual highest AQ value among all students in the cohort.
```








