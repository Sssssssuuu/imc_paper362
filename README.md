# GPT Store Mining and Analysis
This repository contains materials from the paper *GPT Store Mining and Analysis*.
## Directory structure
```
.
├── RQ1_gptstore_data
│   ├── categories_gpts_3.27.xlsx                # The GPT classification in the third-party GPT Store on March 27th
│   ├── gptstore_ai_data.xlsx                    # The GPT classification and detailed data in gptstore.ai on March 27th
│   └── spider.py                                # Example of a web spider
├── RQ2_top1000                                  # Detailed data of Top 1000 GPTs in various categories on March 17th
│   ├── 317_top_1000_dalle.xlsx
│   ├── 317_top_1000_education.xlsx
│   ├── 317_top_1000_lifestyle.xlsx
│   ├── 317_top_1000_other.xlsx
│   ├── 317_top_1000_productivity.xlsx
│   ├── 317_top_1000_programming.xlsx
│   ├── 317_top_1000_research.xlsx
│   └── 317_top_1000_writting.xlsx
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
## RQ1: GPTStore’s topic categories.
RQ1 delves into the categorization of GPTs across the official GPT store launched by OpenAI and three third-party GPT stores: GPTs Hunter, GPTStore.AI, and GPTs App. The objective is to analyze and evaluate how GPT apps (i.e., GPTs) are classified by topic, assessing the effectiveness of these classification schemes in facilitating user discovery and app selection. 

Within the `RQ1_gptstore_data` folder:
- `gptstore_ai_data.xlsx` captures data from the third-party GPTs website [gptstore.ai](https://gptstore.ai) as of March 27th. The data includes counts and percentages of GPTs across different categories. Additionally, the spreadsheet provides detailed information on 170,697 GPTs listed, including their name, description, logo, URL, and conversion count.
- `categories_gpts_3.27` records the categorization of GPTs on three third-party websites: [gptsapp.io](https://gptsapp.io), [gptstore.ai](https://gptstore.ai), and [gptshunter.com](https://gptshunter.com).
