from functions import PortfolioAnalyzer

import logging
import pandas as pd


def main():
    try:
        
        analyzer=PortfolioAnalyzer(r'C:\Users\abhas\Downloads\alphanalysis assignment\AlphaAnalysis\Stocks.csv')
        
        start_date,end_date,invested_amount= analyzer.get_input_from_user()


        print("Calculating Portfolio...")
        
        portfolio_df=analyzer.stock_calculation(start_date,end_date,invested_amount)
        
        print("Saving Portfolio...")
        
        analyzer.save_result(portfolio_df)
        
        print("Portfolio Saved Successfully")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()

