🎬 Her Story, Their Success: A Data-Driven Look at Female-Led Movies 📊

  A deep-dive analysis into the trends, critical reception, and genre distribution of female-led films from 2018-2022.

🚀 Project Overview

- Do films with female protagonists perform differently at the box office or with critics? Are there specific genres where female-led stories are becoming more prevalent? This project tackles these questions by analyzing a massive dataset of over 700,000 movies to explore the cinematic landscape for female-led films released between 2018 and 2022.
- The core of this project involved classifying films as "female-led" using Natural Language Processing (NLP) on plot summaries, scraping external websites for up-to-date review scores, and building an interactive Power BI dashboard to visualize the findings.

✨ Key Features

✅ Automated Classification: Leveraged NLP (TF-IDF) to intelligently classify over 700k movies as female-led or not based on cast and plot data.

✅ Live Data Scraping: Built a robust web scraper with BeautifulSoup to augment the dataset with the latest IMDB and Rotten Tomatoes scores.

✅ Interactive Dashboard: Designed and deployed a comprehensive Power BI dashboard to explore genre trends, score distributions, and correlations.

✅ In-Depth Analysis: Investigated the relationship between genre, critical scores, and release year to uncover actionable insights.

🛠️ Tech Stack & Tools

- Python	Core language for data processing and analysis.
- Pandas & NumPy	Data manipulation, cleaning, and transformation.
- NLTK & Scikit-learn	NLP for classifying films using TF-IDF on plot keywords.
- BeautifulSoup & Requests	Web scraping IMDB and Rotten Tomatoes for critic scores.
- Jupyter Notebook	Prototyping, exploratory data analysis (EDA), and model development.
- Power BI	Creating interactive visualizations and the final dashboard.
- Kaggle API	Programmatic retrieval of the dataset.

Export to Sheets
⚙️ Methodology
This project followed a structured data analysis workflow:
- Data Ingestion: The Movies Daily Update Dataset from Kaggle, containing over 700,000 film records, was imported for analysis.
- NLP-Powered Classification: A key challenge was identifying "female-led" films at scale. I engineered a solution using the NLTK library to process plot keywords. By leveraging a Term Frequency-Inverse Document Frequency (TfidfVectorizer) model, I classified films based on the prominence of female-centric terms and roles in their descriptions.
- Data Augmentation via Web Scraping: To ensure the analysis was current, I developed a Python script using BeautifulSoup and requests to scrape IMDB and Rotten Tomatoes, collecting the latest audience and critic scores for the filtered subset of films.
- Insight Generation & Visualization: The final, cleaned dataset was imported into Power BI. Here, I developed an interactive, multi-page dashboard to visualize trends, compare scores, and explore correlations between genres and release years.

📈 Key Findings & Visuals
The analysis revealed several interesting trends. The dashboard allows for a dynamic exploration of these key questions:

- How do IMDB and Rotten Tomatoes scores compare for female-led films?
    - Finding: Female-led dramas consistently scored higher on Rotten Tomatoes compared to their IMDB counterparts, suggesting a potential difference in perception between critics and the general audience.

<img width="648" height="455" alt="image" src="https://github.com/user-attachments/assets/9c6badd7-4d85-4cae-affa-5d2e846fefed" />
