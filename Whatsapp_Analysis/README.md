# TDN Whatsapp Group Analysis

## Introduction (Overview)
This project analyzes communication patterns, sentiment, and participation levels in multiple WhatsApp groups within The DAO Network community from October 15th 2024 through 22nd March 2025. 

The goal is to extract valuable insights from exported chat logs, visualize member engagement, and understand the tone and volume of group interactions over time.

## Background (The Questions)
We set out to answer key questions such as:

- What is the volume of messages over time?

- Who are the most and least active contributors?

- What is the general sentiment of the conversations?

- How does engagement vary across different WhatsApp groups?

- Which group or member demonstrates the most consistent participation?

- What day/month/year had peak interaction?

- How many unique senders are participating in conversations?

## Tools Used

- Python – For data processing, sentiment analysis, and visualization.

- Libraries: pandas, matplotlib, seaborn, textblob, re, collections

- Power BI (Free Version) – For interactive dashboard creation and stakeholder presentation.

## Analysis
1. Data Cleaning & Preparation

- WhatsApp chat exports were cleaned by replacing characters (-, ,, :) with a semicolon ; as a uniform delimiter.
```python
if len(parts) >= 5:
            date = parts[0]
            hour = parts[1]
            minute = parts[2]
            sender = parts[3]
            message = ";".join(parts[4:])
            data.append([date, hour, minute, sender, message, group_name])
```
- Data was structured into: Date, Time, Sender, and Message.
```python
return pd.DataFrame(data, columns=["Date", "Hour", "Minute", "Sender", "Message", "Group"])
```

- Missing values and system messages (e.g., join/left notifications) were removed.


- Sentiment polarity was calculated using TextBlob.

2. Data Merging

- Multiple WhatsApp groups were loaded and merged into a single dataset.
```python
df_combined = pd.concat(all_dfs, ignore_index=True)
```

- A new column was added to categorize each message by its originating group.

3. Metrics Calculated

- Total number of messages, unique senders, and date ranges.

- Sentiment breakdown (positive, neutral, negative).
```python
df_combined["Polarity"] = df_combined["Message"].apply(lambda msg: TextBlob(str(msg)).sentiment.polarity)
df_combined["Sentiment"] = df_combined["Polarity"].apply(
    lambda p: "Positive" if p > 0.2 else "Negative" if p < -0.2 else "Neutral"
)
```
- Participation percentage and mentions per member.
```python
unique_senders = df_combined['Sender'].unique()
mention_counts = {sender: 0 for sender in unique_senders}
```
- Daily message volume and sender frequency.

4. Visualizations

- Sentiment distribution pie chart.
```python
sentiment_counts = df_dao["Sentiment"].value_counts()
plt.figure(figsize=(5,5))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['#F44336', '#4CAF50', '#9E9E9E'])
plt.title("Sentiment Analysis")
plt.tight_layout()
plt.savefig("Images/sentiment_analysis_donut.png")
plt.show()
```
- Message volume trend line chart.
```python
df_dao["Year"] = df_dao["Date"].dt.year
yearly_counts = df_dao.groupby("Year").size()
yearly_counts.plot(kind="pie", autopct='%1.1f%%', startangle=90, figsize=(5,5), colors=['#4CAF50', '#9E9E9E'])
plt.ylabel("")
plt.title("Total Messages by Year")
plt.tight_layout()
plt.savefig("Images/total_messages_by_year.png")
plt.show()
```
- Top 10 most active senders.
```python
top_senders = df_dao["Sender"].value_counts().head(10)
plt.figure(figsize=(8,4))
top_senders.plot(kind="bar", color="#796200")
plt.title("Top Senders")
plt.xlabel("Sender")
plt.ylabel("Total Messages")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Images/top_senders_python.png")
plt.show()
```
- Group-level comparison of message volume.
```python
group_count = df_dao["Group"].value_counts()
plt.figure(figsize=(10,4))
group_count.plot(kind="bar", color="#796200")
plt.title("Total Messages by Group")
plt.xlabel("Group")
plt.ylabel("Message Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Images/messages_by_group.png")
plt.show()
```
## What You Learned
- Group activity tends to spike in short bursts, followed by long quiet periods.

- Neutral sentiment dominates, but key contributors set the tone with positivity.

- Few members drive the majority of engagement, showing a core team effect.

- Some members are frequently mentioned but rarely post — indicating passive stakeholders or authority figures.

## Insights
From the visual analysis:

- Sentiment Analysis: Majority of messages are neutral (~82%), with ~16% positive and ~2% negative.
![Sentiment Analysis](images/sentiment_analysis_donut.png)Sentiment Analysis

- Top Contributors: A few users like Violet Benson and Jesus Is Lord are responsible for hundreds of messages.
![Top Contributors](images/top_senders_python.png)Top Contributors

- Engagement by Group: Groups like TDN GENERAL and DAO Core Team had the highest activity levels.
![Group engagement](images/messages_by_group.png) Group engagement


- Daily Trends: November 2024 saw significant spikes in daily engagement.
![Daily Trends](images/daily_volume.png)Daily Trends

![Dashboard Screenshot](images/Dashboard_Screenshot.png)Dashboard Screenshot

## Business Impact
- Leadership Clarity: Helps identify natural leaders and active contributors.

- Operational Focus: Reveals which groups are most engaged and worth investing in further.

- Community Health: Early detection of inactivity or negativity helps intervene in group dynamics.

- Planning Events: Peak message days and engagement trends can inform when best to announce or organize key initiatives.

## Conclusion
This project provides a scalable method to monitor, analyze, and report on group communication across multiple WhatsApp teams. With both sentiment and engagement insights, leadership can make data-driven decisions to foster collaboration, address communication gaps, and reward high-performing contributors.