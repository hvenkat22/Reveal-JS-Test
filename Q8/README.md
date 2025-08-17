# Healthcare Performance Analysis — Patient Satisfaction (2024 Q1–Q4)

**Contact / Verification:** 22f2001398@ds.study.iitm.ac.in
**Contact / Verification:** 22f2001398@ds.study.iitm.ac.in

## Overview
The executive team is concerned about patient satisfaction. We analyzed the 2024 quarterly patient satisfaction scores to understand trend, compare against industry benchmarks, and recommend concrete actions to reach the target score.

### Data (2024 quarterly patient satisfaction scores)
- Q1: -0.23  
- Q2: 6.26  
- Q3: 7.30  
- Q4: 5.11  

**Computed average (2024): 4.61**
**Computed average (2024): 4.61**

The solution: "improve service quality and wait times"

**Industry target:** 4.5

---

## Key Findings
1. **Average above target but inconsistent across quarters.**  
   - The computed average is **4.61**, which is slightly above the industry target (4.5). However, the quarterly values show large swings (Q1 far below zero, Q2–Q4 high).
2. **High volatility indicates instability in experience delivery.**  
   - Q1’s negative value suggests either measurement issues or a severe operational problem in that quarter.
3. **Most recent quarter (Q4) is 5.11 — positive but not consistently sustained.**

---

## Business Implications
- The average being >4.5 provides some comfort, but the large quarter-to-quarter variance signals **operational inconsistency**. Executives should not be complacent — volatility can harm patient trust and long-term brand.
- Q1’s anomalous low value may point to:
  - data collection or reporting error, OR
  - a specific event (e.g., staff shortages, IT outage) that must be investigated.

---

## Recommendations (to reach & sustain target of 4.5)
**Short term (immediate, 0-3 months)**
- Investigate Q1 root causes: audit survey process, timestamps, and operational logs for that quarter.
- Targeted operational fixes (if Q1 was operational): allocate extra staff during peak hours and address system outages.

**Medium term (3–9 months)**
- Operationalize process improvements:
  - Reduce patient wait times (scheduling changes, triage improvements).
  - Implement real-time monitoring dashboards for patient satisfaction and wait times to detect declines quickly.
- Pilot a service-quality improvement program (training, standardized scripts, KPI-based incentives).

**Long term (9–18 months)**
- Institutionalize the continuous feedback loop:
  - Automate post-visit surveys with segmentation and sentiment analysis.
  - Tie part of performance reviews to sustained satisfaction metrics.

**Quick metric-driven action:** Prioritize interventions that reduce variability (variance) in scores, not just improving mean. A stable mean above 4.5 is more valuable than a volatile mean.

---

## Reproducible analysis
Files in this PR:
- `analysis.py` — Python script that computes average and produces `trend.png`.
- `trend.png` — The generated visualization (attached in PR).
- `quarterly_scores.csv` — The CSV of quarterly scores.

Run:
```bash
python analysis.py

This work was developed with support from Codex.  
Reference: https://chatgpt.com/codex/tasks
