# 📊 AI Needs & Opportunities in the Startup Ecosystem

## 📌 Project Description

This project explores the needs, behaviors, and priorities of various stakeholders in the AI startup ecosystem—founders, startups, investors, freelancers, and companies. Using a rich dataset from a virtual AI showcase, we uncover valuable insights into what tools are used, which services are in demand, and where opportunities for collaboration exist.

By analyzing AI adoption trends, regional investment interests, and service gaps, this project provides a strategic understanding for decision-makers, accelerators, investors, and solution providers aiming to operate more effectively in the AI landscape.

---

## 🎯 Objective

The primary goal of this project is to answer:

**What do different players in the AI ecosystem need right now?**

We focus on identifying:

- ounders’ interest in AI services, education, and automation

- Investors' focus by startup stage and region

- Startups' funding stages and global presence

- Freelancers' tool usage and service alignment

---

## 📂 Data Source & Structure

The dataset was sourced from a google forms of attendees from a virtual AI showcase conference.

**Key Sheets Analyzed:**
- **Full list of attendees** (founders and executives)
- **AI freelancers & agencies**
- **AI investors**
- **AI startups**
- **Companies seeking AI automation**


**Structure:**

Each sheet includes participant information like name, email, company name, stage of funding, regional interest, tools used, and AI-related needs. 

Some columns are binary flags (1 for selected), while others are free-text inputs.

**Assumptions Made:**

- Null or generic text (e.g., “none”, “not sure”) was treated as non-responses.

- Stage and region indicators are mutually exclusive unless explicitly multi-selected.

---

## 🧹 Cleaning and Preparation
**Steps taken:**

- Stripped whitespace and line breaks from column names

- Mapped long column headers to concise labels

- Converted binary responses to integers (1 for selected, 0 for not selected)

- Cleaned free-text responses using regex (e.g., tool lists like “Zapier + GPT” → [“Zapier”, “GPT”])

- Removed irrelevant or ambiguous values (“n/a”, “none at the moment”)

- Melted wide-form datasets into long format for region/stage analysis

---

##  ❓ Key Questions Answered
1. What are the primary AI-related needs of startup founders?

2. Which investors are interested in which funding stages?

3. What tools do AI freelancers use most frequently?

4. Where are investors most interested in placing capital geographically?

5. How do startup fundraising stages align with regional presence?

6. Which founders want services, training, or AI education for their teams?

---

## 🔍 Analysis Process

We used the following methods:

- Frequency counts with Counter for categorical needs and tools

- Data reshaping (melt) to map stages and regions

- Bar plots and horizontal bar charts using Seaborn and Matplotlib

- Grouping and filtering to match startups with investors

- Merging datasets (e.g., matching freelancers with founders needing services)

---

## 📈 Insights & Findings

1. **Top Needs of Founders:**

   - 249 founders expressed at least one need

   - Most common: AI Services, Personal AI Training, and Team AI Education

   ![Top Needs of Founders](images\founders_needs.png) Top Needs of Founders

   ![Primary Needs of Founders](images\founders_primary_needs.png) Primary Needs of Founders

2. Startup Stage Distribution:

    - Majority are at Seed and Pre-seed stages

    - Few in Series B or later

    ![Starting Funding Distributiom](images\startup_stages.png) Starting Funding Distributiom

    ![Investor Focus by Stage](images\investor_focus_stage.png) Investor Focus by Stage

3. Investor Interests:

    - Seed and Pre-seed are the most popular focus stages
    ![Investor Focus by Stage](images\ai_needs_investor_selected.png) Selected AI Needs by Investors

    - Majority of investors have 1 or 2 specific AI needs
    ![Investor AI Need](images\investor_ai_needs_distribution.png) Investor's AI Needs

4. Freelancers:

    - Most-used tools include **n8n**, **OpenAI**, **ChatGPT**, and **Make**

    - Tools were highly varied, but concentrated among top 10 automation platforms

    ![Top Freelancers Tools](images\top_freelancer_tools.png) Top Freelancers Tools

5. Regional Trends:

    - Investors are heavily interested in the **US**, **Europe**, and **Globally**

    - Startups also show global distribution, with strong presence in **Asia Pacific** and **Africa**
     ![Regional Trends](images\geographic_investment_interests.png) Regional Trends

---

## 📊 Visualizations

The following charts were created to support findings:

| Visualization | Description |
|---------------|-------------|
| `founders_needs.png` | Breakdown of AI needs among founders |
| `founders_primary_needs.png` | Primary needs selected by each founder |
| `investor_focus_stage.png` | Stage focus of AI investors |
| `startup_stages.png` | Fundraising stage distribution of startups |
| `top_freelancer_tools.png` | Top 10 AI tools used by freelancers |
| `startup_stage_region.png` | Startup stage vs. region distribution |
| `investor_ai_needs_distribution.png` | Count of AI-related needs per investor |
| `ai_needs_investor_selected.png` | Type of AI needs investors selected |
| `geographic_investment_interests.png` | Investor interest by global region |

---

## 📌 Recommendations

- **For AI Service Providers:** Prioritize founders interested in Process Automation and AI Services.

- **For Freelancers:** Tailor toolkits around top tools (Zapier, ChatGPT, etc.) and actively reach out to founders expressing need.

- **For Investors:** Consider expanding support into Africa and Asia Pacific regions where early-stage startup presence is growing.

- **For Ecosystem Builders:** Facilitate founder-mentor or founder-investor matchmaking based on shared stage/regional interest.

- **For Training Programs:** Offer tailored AI training for founders and their teams, particularly focused on practical applications.

---

## 🔁 How to Reproduce

1. Clone this repository and install requirements:

   ```bash
   pip install pandas seaborn matplotlib wordcloud

2. Place the Excel file here:

    ```bash

    /your_project_directory/
    └── AI_Showcase_Virtual_Conf_Full_attendee_list.xlsx

3. Run the analysis script:

    python your_analysis_script.py

4. Outputs will be saved in:

    /Cleaned_Data/

    /images/

---

## 🙌 Credits & Tools Used

- **Project by:** [Your Name]
- **Data provided by:** The DAO Network / AI Showcase Virtual Conference
- Libraries used:

  -  pandas for data manipulation

  -  matplotlib and seaborn for plotting

  -  Counter and re for text analysis

  -  wordcloud for future visualization extension

