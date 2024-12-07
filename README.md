<h1 align="center" id="title">Portfolio Share Calculator</h1>

<p id="description">A sophisticated Python application designed to calculate optimal share quantities for a given investment portfolio. The system leverages Yahoo Finance API for real-time stock data, pandas for efficient data manipulation, and openpyxl for detailed Excel reporting. It incorporates automatic weightage normalization, precise share calculation based on investment amount, and comprehensive error handling, providing a complete solution for portfolio management needs.</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="shields">
<img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="shields">
<img src="https://img.shields.io/badge/Yahoo_Finance-800080?style=for-the-badge&logo=yahoo&logoColor=white" alt="shields">
</p>

<h2>🧐 Features</h2>

Here're some of the project's best features:

* Real-time Stock Data: Fetches current stock prices using Yahoo Finance API
* Automated Calculations: Computes share quantities based on investment weightage
* Excel Reporting: Generates detailed, formatted Excel reports
* Error Handling: Comprehensive error checking and logging
* Data Validation: Ensures data integrity and proper weightage distribution

<h2>💻 Built with</h2>

Technologies used in the project:

* Python: Core programming language
* pandas: Data manipulation and analysis
* yfinance: Yahoo Finance market data downloader
* openpyxl: Excel file handling
* logging: Error and information tracking

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the repository:</p>

```
git clone https://github.com/abhashgoyal/Alphanalysis-Stock-Price.git
```

<p>2. Create and activate virtual environment:</p>

```
bash
python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # Linux/Mac
```

<p>3. Install required dependencies:</p>

```
pip install -r requirements.txt
```

<p>4. Run the application:</p>

```
python Code/main.py
```


<h2>📉 Output Format</h2>

The generated Excel file contains:

| Ticker     | Weightage | 2023-04-27          | 2023-04-28          |
|------------|-----------|---------------------|---------------------|
| ADANIPORTS | 0.0082    | 124.289503599848   | 120.358141008682   |
| APOLLOHOSP | 0.0061    | 13.808715336728    | 13.514411095213    |
| ASIANPAINT | 0.0195    | 67.242539796661    | 67.186932464649    |

<h2>🔒 Error Handling</h2>

* Input validation for dates and investment amount
* Weightage normalization and validation
* Stock data availability checking
* Comprehensive error logging

<h2>📝 Usage Example</h2>

* Enter Details:
* Enter Start Date (YYYY-MM-DD): 2024-01-01
* Enter End Date (YYYY-MM-DD): 2024-01-10
* Enter Invested Amount: 100000
* Calculating Portfolio...
* Saving Portfolio...
* Portfolio Saved Successfully

  
<h2>🚧 Future Roadmap</h2>

* Add support for international markets
* Implement portfolio performance analytics
* Add visualization capabilities
* Include real-time portfolio tracking

<h2>🙏 Acknowledgments</h2>

* Yahoo Finance for providing stock data API
* Python community for excellent libraries
* Alpha Analysis for the project opportunity

<h2>Thank You Alpha Analysis For Providing me this opportunity</h2>
<h2>Alpha Analysis's Python Developer </h2>

Developed with ❤️ by Abhash Goyal
<p>(https://www.linkedin.com/in/abhashgoyal-4692b91b8/)</p>
<p>abhashgoyal200@gmail.com</p>





