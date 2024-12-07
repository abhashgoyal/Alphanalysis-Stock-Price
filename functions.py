import pandas as pd
import yfinance as yf
from datetime import datetime
import logging
import sys
from typing import Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PortfolioAnalyzer:
    def __init__(self, csv_path: str):
        """Initialize with stock data from CSV"""
        try:
            self.stock_df = pd.read_csv(csv_path)
            
            if 'Ticker' not in self.stock_df.columns:
                logger.info("Ticker Column Not Found")
                self.stock_df['Ticker'] = self.stock_df['Company']
                
            # Validate weightages sum to 1
            total_weight = self.stock_df['Weightage'].sum()
            if not 0.99 <= total_weight <= 1.01:
                logger.warning(f"Total weightage is {total_weight}, should be close to 1")
                
            logger.info("Stock data loaded successfully")
            
        except Exception as e:
            logger.error(f"Error Loading CSV File: {e}")
            sys.exit(1)
    
    def get_input_from_user(self) -> Tuple[str, str, float]:
        """Get date range and investment amount from user"""
        while True:
            try:
                print("\nEnter Details:")
                start_date = input("Enter Start Date (YYYY-MM-DD): ")
                end_date = input("Enter End Date (YYYY-MM-DD): ")
                invested_amount = float(input("Enter Invested Amount: "))
                
                # Validate dates
                datetime.strptime(start_date, '%Y-%m-%d')
                datetime.strptime(end_date, '%Y-%m-%d')
                
                if invested_amount <= 0:
                    raise ValueError("Invested Amount Must be Positive")
                
                return start_date, end_date, invested_amount
            
            except Exception as e:
                logger.error(f"Invalid Input: {e}")
                print("Please Try Again")
    
    def stock_data(self, ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
        """Fetch stock data from Yahoo Finance"""
        try:
            ticker_symbol = f"{ticker}.NS"  # Add .NS suffix for NSE stocks
            
            stock_data = yf.download(
                ticker_symbol,
                start=start_date,
                end=end_date,
                progress=False
            )
            
            return stock_data['Close'] if not stock_data.empty else None
            
        except Exception as e:
            logger.error(f"Error Fetching Stock Data for {ticker}: {e}")
            return None
    
    def stock_calculation(self, start_date: str, end_date: str, invested_amount: float) -> pd.DataFrame:
        """Calculate shares for each stock based on weightage and price"""
        try:
            self.stock_df['Amount'] = self.stock_df['Weightage'] * invested_amount
            portfolio_df = pd.DataFrame()
            
            for _, row in self.stock_df.iterrows():
                logger.info(f"Processing {row['Ticker']}")
                
                prices = self.stock_data(row['Ticker'], start_date, end_date)
                
                if prices is not None:
                    # Calculate shares for each day
                    shares = row['Amount'] / prices
                    portfolio_df[row['Ticker']] = shares.round(2)
                else:
                    logger.warning(f"No price data found for {row['Ticker']}, skipping...")
            
            portfolio_df.index.name = 'Date'
            return portfolio_df
            
        except Exception as e:
            logger.error(f"Error in stock calculation: {e}")
            return pd.DataFrame()
    
    def save_result(self, portfolio_df: pd.DataFrame, output_file: str = 'portfolio.xlsx'):
        """Save portfolio data to Excel"""
        try:
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                portfolio_df.to_excel(writer, sheet_name='Portfolio')
                
                # Format the worksheet
                worksheet = writer.sheets['Portfolio']
                
                # Format date column
                for idx, cell in enumerate(worksheet['A'], 1):
                    if idx == 1:  # Skip header
                        continue
                    cell.number_format = 'YYYY-MM-DD'
                
            logger.info(f"Portfolio Data Saved to {output_file}")
            
        except Exception as e:
            logger.error(f"Error Saving Portfolio Data: {e}")
        finally:
            logger.info("Execution Completed")