# IBM HR Analytics — Business EDA & Attrition Analysis

## 1. Objective

The purpose of this analysis is to identify employee attrition patterns across key workforce dimensions and determine which factors should receive attention in the executive HR dashboard.

The analysis focuses on:

* Department
* Job Role
* Overtime
* Job Satisfaction
* Job Level
* Business Travel
* Work-Life Balance
* Age Group

---

## 2. Overall Attrition

| Attrition Status | Employees | Percentage |
| ---------------- | --------: | ---------: |
| No               |     1,233 |     83.88% |
| Yes              |       237 |     16.12% |
| **Total**        | **1,470** |   **100%** |

The overall employee attrition rate is **16.12%**.

This will be one of the primary executive KPIs in the Power BI dashboard.

---

## 3. Workforce Composition

### Business Travel

| Business Travel   | Employees |
| ----------------- | --------: |
| Travel_Rarely     |     1,043 |
| Travel_Frequently |       277 |
| Non-Travel        |       150 |

Travel_Rarely is the dominant travel category, representing the majority of employees.

### Department

| Department             | Employees |
| ---------------------- | --------: |
| Research & Development |       961 |
| Sales                  |       446 |
| Human Resources        |        63 |

Research & Development has the largest workforce, followed by Sales and Human Resources.

### Gender

| Gender | Employees |
| ------ | --------: |
| Male   |       882 |
| Female |       588 |

### Marital Status

| Marital Status | Employees |
| -------------- | --------: |
| Married        |       673 |
| Single         |       470 |
| Divorced       |       327 |

### Overtime

| Overtime | Employees |
| -------- | --------: |
| No       |     1,054 |
| Yes      |       416 |

Approximately 28% of employees work overtime.

---

# 4. Attrition Analysis

## 4.1 Attrition by Department

| Department             | No Attrition | Attrition |
| ---------------------- | -----------: | --------: |
| Human Resources        |        81.0% |     19.0% |
| Research & Development |        86.2% |     13.8% |
| Sales                  |        79.4% | **20.6%** |

### Finding

Sales has the highest departmental attrition rate at **20.6%**, followed by Human Resources at **19.0%**.

Research & Development has the lowest rate among the three departments at **13.8%**.

### Business implication

The Sales department should receive additional investigation, particularly around workload, overtime, job roles, compensation, and travel requirements.

---

## 4.2 Attrition by Job Role

| Job Role                  | No Attrition | Attrition |
| ------------------------- | -----------: | --------: |
| Healthcare Representative |        93.1% |      6.9% |
| Human Resources           |        76.9% |     23.1% |
| Laboratory Technician     |        76.1% |     23.9% |
| Manager                   |        95.1% |      4.9% |
| Manufacturing Director    |        93.1% |      6.9% |
| Research Director         |        97.5% |      2.5% |
| Research Scientist        |        83.9% |     16.1% |
| Sales Executive           |        82.5% |     17.5% |
| Sales Representative      |        60.2% | **39.8%** |

### Finding

Sales Representative has the highest attrition rate at **39.8%**.

Laboratory Technician and Human Resources also show relatively high attrition rates of **23.9%** and **23.1%** respectively.

Research Director and Manager have substantially lower attrition rates.

### Business implication

Job-role-level analysis is important because departmental averages can hide high-risk roles.

For example, the Sales department's overall attrition rate of 20.6% is strongly influenced by the much higher attrition observed among Sales Representatives.

---

## 4.3 Attrition by Overtime

| Overtime | No Attrition | Attrition |
| -------- | -----------: | --------: |
| No       |        89.6% |     10.4% |
| Yes      |        69.5% | **30.5%** |

### Finding

Employees working overtime have a **30.5% attrition rate**, compared with **10.4%** among employees who do not work overtime.

This represents a substantial difference in observed attrition rates.

### Business implication

Overtime should be treated as an important workforce-risk dimension in the dashboard.

HR management could investigate workload distribution, staffing levels, overtime frequency, and employee well-being.

> **Important:** This analysis shows an association, not proof that overtime directly causes attrition.

---

## 4.4 Attrition by Job Satisfaction

| Job Satisfaction | No Attrition | Attrition |
| ---------------: | -----------: | --------: |
|                1 |        77.2% | **22.8%** |
|                2 |        83.6% |     16.4% |
|                3 |        83.5% |     16.5% |
|                4 |        88.7% | **11.3%** |

### Finding

Employees with the lowest job satisfaction score have a higher observed attrition rate of **22.8%**.

Employees with the highest satisfaction score have an attrition rate of **11.3%**.

### Business implication

Job satisfaction should be included as an interactive dashboard dimension and considered when identifying potential retention risks.

---

## 4.5 Attrition by Job Level

| Job Level | No Attrition | Attrition |
| --------: | -----------: | --------: |
|         1 |    **73.7%** | **26.3%** |
|         2 |        90.3% |      9.7% |
|         3 |        85.3% |     14.7% |
|         4 |        95.3% |      4.7% |
|         5 |        92.8% |      7.2% |

### Finding

Job Level 1 has the highest attrition rate at **26.3%**.

Higher job levels generally show lower observed attrition rates.

### Business implication

Entry-level employees may require additional attention through onboarding, career progression, mentoring, compensation review, or engagement initiatives.

---

## 4.6 Attrition by Business Travel

| Business Travel   | No Attrition | Attrition |
| ----------------- | -----------: | --------: |
| Non-Travel        |        92.0% |      8.0% |
| Travel_Frequently |        75.1% | **24.9%** |
| Travel_Rarely     |        85.0% |     15.0% |

### Finding

Employees who travel frequently have an observed attrition rate of **24.9%**, compared with **8.0%** among employees who do not travel.

### Business implication

Frequent business travel should be monitored as a potential workforce-risk indicator.

Further analysis should examine whether travel interacts with overtime, job role, department, or work-life balance.

---

## 4.7 Attrition by Work-Life Balance

| Work-Life Balance | No Attrition | Attrition |
| ----------------: | -----------: | --------: |
|                 1 |        68.8% | **31.2%** |
|                 2 |        83.1% |     16.9% |
|                 3 |        85.8% |     14.2% |
|                 4 |        82.4% |     17.6% |

### Finding

Employees with the lowest work-life balance score have the highest attrition rate at **31.2%**.

The strongest observed retention occurs at Work-Life Balance level 3, with attrition of **14.2%**.

### Business implication

Work-life balance should be included in the dashboard because it provides a potentially important employee-experience dimension for retention analysis.

---

## 4.8 Attrition by Age Group

| Age Group | No Attrition | Attrition |
| --------- | -----------: | --------: |
| 18–25     |        64.2% | **35.8%** |
| 26–35     |        80.9% | **19.1%** |
| 36–45     |        90.8% |  **9.2%** |
| 46–55     |        88.5% |     11.5% |
| 56–65     |        83.0% |     17.0% |

### Finding

The **18–25 age group has the highest attrition rate at 35.8%**.

Attrition decreases significantly through the 36–45 age range, where it reaches 9.2%.

### Business implication

Younger employees may require targeted retention strategies involving career development, progression opportunities, mentoring, compensation, and employee engagement.

---

# 5. Key Business Findings

Based on the current EDA, the strongest observed attrition patterns are:

### 1. Overtime

Employees working overtime have a **30.5% attrition rate**, compared with 10.4% for employees without overtime.

### 2. Age

Employees aged **18–25 show 35.8% attrition**, substantially higher than the overall rate of 16.12%.

### 3. Job Role

**Sales Representatives have 39.8% attrition**, making this the highest-risk job role in the current analysis.

### 4. Work-Life Balance

Employees with the lowest work-life balance score have **31.2% attrition**.

### 5. Job Level

Job Level 1 employees have **26.3% attrition**, considerably higher than Job Level 2 and above.

### 6. Business Travel

Employees who travel frequently show **24.9% attrition**, compared with 8.0% for non-travel employees.

### 7. Department

Sales has the highest departmental attrition at **20.6%**.

---

# 6. Potential Retention Areas

Based on the observed patterns, management could investigate:

* Overtime and workload distribution
* Retention of younger employees
* Sales Representative turnover
* Entry-level employee experience
* Work-life balance
* Frequent business travel
* Job satisfaction
* Career development and progression

These should be treated as **areas for investigation rather than confirmed causal drivers**.

---

# 7. Dashboard Requirements Derived from EDA

The EDA directly informs the Power BI dashboard design.

### Executive KPIs

* Total Employees
* Attrition Count
* Attrition Rate
* Average Age
* Average Monthly Income
* Average Years at Company

### Key Visuals

* Attrition by Department
* Attrition by Job Role
* Attrition by Age Group
* Attrition by Overtime
* Attrition by Job Satisfaction
* Attrition by Job Level
* Attrition by Business Travel
* Attrition by Work-Life Balance

### Recommended Interactive Filters

* Department
* Job Role
* Gender
* Age Group
* Business Travel
* OverTime
* Job Level
* Marital Status

### Drill-down

Recommended hierarchy:

```text
Department
    ↓
Job Role
```

This allows HR stakeholders to identify which specific roles contribute to higher departmental attrition.

---

# 8. Analytical Limitations

The current analysis identifies **associations and patterns**, not causal relationships.

For example:

* Higher overtime is associated with higher attrition.
* Frequent travel is associated with higher attrition.
* Lower work-life balance is associated with higher attrition.

However, these results do not prove that these factors independently cause employees to leave.

Additional segmentation and statistical analysis could be performed if deeper causal or predictive analysis is required.

---

# 9. Next Step

The next stage is to prepare the final analytical dataset.

Planned transformations:

1. Remove constant columns.
2. Exclude the employee identifier from dashboard analysis.
3. Create an `AgeGroup` analytical field.
4. Validate the transformed dataset.
5. Export the cleaned CSV.
6. Load the cleaned dataset into Power BI.
7. Create DAX measures and executive KPIs.
8. Build the interactive dashboard.

---

## Conclusion

The dataset demonstrates several clear attrition patterns that can support an executive HR dashboard.

The most significant observed high-attrition segments include:

* Sales Representatives — **39.8%**
* Age 18–25 — **35.8%**
* Low Work-Life Balance — **31.2%**
* Employees working overtime — **30.5%**
* Job Level 1 — **26.3%**
* Frequent business travel — **24.9%**

These findings provide the analytical foundation for the dashboard's visual hierarchy and decision-oriented recommendations.
