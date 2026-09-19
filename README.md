# CodeAlpha Books Analytics

End-to-end Data Analytics project covering **Task 1: Web Scraping**, **Task 2: Exploratory Data Analysis (EDA)**, and **Task 3: Data Visualization**.

## Project Overview

This project demonstrates a complete analytics workflow:

**Web page → Web scraping → CSV dataset → Data cleaning → EDA → Visualizations → Dashboard**

The project uses Python, Requests, BeautifulSoup, Pandas, NumPy, Matplotlib, and Streamlit. A Power BI dashboard can also be built from the cleaned CSV.

## Tasks Completed

### Task 1 — Web Scraping
- Scrape book information from Books to Scrape using Python.
- Extract title, price, availability, rating, and product URL.
- Handle multiple pages with pagination.
- Save results as CSV.

### Task 2 — Exploratory Data Analysis
- Inspect dataset structure and data types.
- Check missing values and duplicates.
- Convert price and rating fields into analysis-ready numeric columns.
- Calculate descriptive statistics, correlation, and IQR-based price outliers.
- Document analytical questions and findings.

### Task 3 — Data Visualization
- Price distribution histogram.
- Rating distribution chart.
- Price vs Rating scatter plot.
- Top 10 highest-priced books chart.
- Streamlit dashboard and Power BI dashboard guide.

## Project Structure

```text
CodeAlpha_Books_Analytics/
├── data/
│   ├── books_sample.csv
│   └── books_clean.csv
├── src/
│   ├── scraper.py
│   ├── clean_data.py
│   └── eda.py
├── dashboard/
│   └── app.py
├── reports/
│   ├── charts/
│   └── eda_summary.txt
├── Books_Analytics.ipynb
├── books_analytics.xlsx
├── POWER_BI_GUIDE.md
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python src/scraper.py
python src/clean_data.py
python src/eda.py
streamlit run dashboard/app.py
```

## Power BI

Open Power BI Desktop and load `data/books_clean.csv`. Recommended visuals are KPI cards, rating distribution, price distribution, a rating-vs-price scatter plot, a top-10 price chart, and a detailed data table. See `POWER_BI_GUIDE.md` for the dashboard layout.

## Dataset Note

Books to Scrape is a sandbox website for scraping practice. Its displayed prices and ratings are randomly assigned for demonstration, so analytical findings from this dataset should be treated as a technical/educational example rather than real book-market intelligence.

## Portfolio Outcome

This project demonstrates practical skills in:
- Python web scraping
- Data cleaning and preprocessing
- Exploratory data analysis
- Statistical analysis
- Data visualization
- Dashboard development
- Documentation and GitHub workflow

## Author

**Ayu2427**

GitHub: https://github.com/Ayu2427
