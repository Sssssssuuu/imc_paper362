# GPT Store Mining and Analysis
This repository contains materials from the paper *GPT Store Mining and Analysis*.
## Directory structure
```
.
├── RQ1_gptstore_data
│   ├── categories_gpts_3.27.xlsx                # The GPT classification in the third-party GPT Store on March 27th
│   ├── gptstore_ai_data.xlsx                    # The GPT classification and detailed data in gptstore.ai on March 27th
│   ├── spider.py                                # Example of a web spider
│   └── response.json                            # An example of a web sipder result
├── RQ2_top1000                                  # Detailed data of Top 1000 GPTs in various categories on March 17th
│   ├── 317_top_1000_dalle.xlsx
│   ├── 317_top_1000_education.xlsx
│   ├── 317_top_1000_lifestyle.xlsx
│   ├── 317_top_1000_other.xlsx
│   ├── 317_top_1000_productivity.xlsx
│   ├── 317_top_1000_programming.xlsx
│   ├── 317_top_1000_research.xlsx
│   ├── 317_top_1000_writting.xlsx
│   ├── correlation_analysis.py                  # Box plots
│   └── spearman_correlation.py                  # Calculate the Spearman coefficients between features.
├── RQ2_top500                                   # Detailed data of Top 500 GPTs from March 9th to March 15th
│   ├── 309_top500_raw.json
│   ├── 310_top500_raw.json
│   ├── 311_top500_raw.json
│   ├── 312_top500_raw.json
│   ├── 313_top500_raw.json
│   ├── 314_top500_raw.json
│   └── 315_top500_raw.json
├── RQ3_security_vulnerabilities
│   └── Security_Vulnerabilities_in_GPTs.xlsx    # List of security vulnerabilities in GPTs
```
## RQ1: GPT Store’s topic categories.
RQ1 delves into the categorization of GPTs across the official GPT store launched by OpenAI and three third-party GPT stores: GPTs Hunter, GPTStore.AI, and GPTs App. The objective is to analyze and evaluate how GPT apps (i.e., GPTs) are classified by topic, assessing the effectiveness of these classification schemes in facilitating user discovery and app selection. 

Within the [RQ1_gptstore_data](RQ1_gptstore_data) folder:
- [gptstore_ai_data.xlsx](RQ1_gptstore_data/gptstore_ai_data.xlsx) captures data from the third-party GPTs website [gptstore.ai](https://gptstore.ai) as of March 27th. The data includes counts and percentages of GPTs across different categories. Additionally, the spreadsheet provides detailed information on 170,697 GPTs listed, including their name, description, logo, URL, and conversion count.
- [categories_gpts_3.27](RQ1_gptstore_data/categories_gpts_3.27.xlsx) records the categorization of GPTs on three third-party websites: [gptsapp.io](https://gptsapp.io), [gptstore.ai](https://gptstore.ai), and [gptshunter.com](https://gptshunter.com).

Additionally, we provide a straightforward Python script named [spider.py](RQ1_gptstore_data/spider.py) that is capable of performing automated web scraping operations. The script utilizes the Python `requests` library to send HTTP requests and handles responses with a concurrent execution strategy using `ThreadPoolExecutor` from the `concurrent.futures` module. This tool has built-in retry logic for failed requests and implements random delays to minimize the risk of being blocked by the target server. The [response.json](RQ1_gptstore_data/response.json) provides an example of the data extracted.

## RQ2: Factors influencing featured GPTs in the GPT Store.
RQ2 seeks to identify the criteria driving the selection of featured GPTs in the GPT Store.  It explores various factors that could influence a GPT's popularity and ranking, such as categories, user engagement metrics, and update frequency.  Through this analysis, we aim to provide insights into how these elements collectively shape the visibility and success of GPTs within the store, ensuring a comprehensive understanding of the factors that drive user preference and engagement.

In the [RQ2_top1000](RQ2_top1000) folder, we present the data of the top 1000 GPTs from each category as of March 17th, ranked by dialogue volume. This dataset includes the name, description, chat count, rating, and number of reviews for each GPT. 

In the [RQ2_top500](RQ2_top500) folder, we display the data for the top 500 GPTs from each category based on dialogue volume, covering the period from March 9th to March 15th. The dataset includes each GPT's ID, name, chat volume, categories, average review score, and total review count.

In the [correlation_analysis.py](RQ2_top1000/correlation_analysis.py) file, we compute and compare the Spearman correlation coefficients between rankings and review counts across various categories, visualizing the outcomes with box plots.

In the [spearman_correlation.py](RQ2_top1000/spearman_correlation.py), we load data from an Excel file, calculate and print the Spearman correlation coefficients between rankings, ratings, and review counts for each pair of these variables.

## RQ3：Security risks associated with the GPT Store.
The emergence of the GPT Store as a prominent AI marketplace also raises concerns about potential security risks. RQ3 explores the various security challenges that the platform faces, ranging from the misuse of GPTs for malicious purposes to vulnerabilities in user data protection. This exploration includes analyzing the store's current security measures, identifying potential loopholes, and assessing the overall risk landscape. We aim to provide a comprehensive understanding of these risks and to offer recommendations for enhancing the platform's security.

In the [RQ3_security_vulnerabilities](RQ3_security_vulnerabilities) folder, [Security_Vulnerabilities_in_GPTs.xlsx](RQ3_security_vulnerabilities/Security_Vulnerabilities_in_GPTs.xlsx)file presents the results of our testing on 1,000 GPTs regarding potential security risks. Each GPT is assessed for specific types of security vulnerabilities, with a '1' indicating the confirmed presence of such a risk warranting attention, and a '0' suggesting the likely absence of that risk.
