# Stock Market Data Visualization

This beginner-friendly Python project allows you to fetch and visualize historical stock price data for any company using its ticker symbol (e.g., AAPL for Apple, MSFT for Microsoft). The project leverages the `yfinance` library to access Yahoo Finance data and `matplotlib` for plotting.

## Features

- Fetch historical stock data for any ticker symbol
- Visualize closing price trends over a chosen time period
- Interactive command-line interface
- Simple and easy-to-understand codebase

## Demo

![Stock Visualization Demo](demo_screenshot.png)

## Getting Started

### Prerequisites

- Python 3.7 or newer
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/stock-market-visualization.git
   cd stock-market-visualization
   ```

2. **Install dependencies:**
   ```bash
   pip install yfinance matplotlib
   ```

### Usage

1. **Run the script:**
   ```bash
   python stock_visualization.py
   ```

2. **Enter the ticker symbol** for the stock you want to visualize (for example, `AAPL` for Apple).

3. **Choose the time period** (like `1mo`, `3mo`, `6mo`, `1y`, `5y`). If you press enter, the default is `6mo`.

4. **View the plotted stock data** in a pop-up window.

### Example

```
Stock Market Data Visualization
Enter the stock ticker symbol (e.g., AAPL, MSFT): AAPL
Enter the period (e.g., 1mo, 3mo, 6mo, 1y, 5y) [default=6mo]:
```
*A graph will appear showing Apple's closing price for the last 6 months.*

## Customization Ideas

- Plot moving averages (SMA/EMA) for trend analysis
- Compare multiple stocks in one plot
- Export the plot as an image file (`plt.savefig('output.png')`)
- Add volume or other technical indicators

## Troubleshooting

- **No data found for ticker**: Check if the ticker symbol is correct and exists on Yahoo Finance.
- **Plot not appearing**: Make sure your Python environment has GUI support (try running outside VS Code terminal if needed).

## Contributing

Pull requests are welcome! Feel free to open an issue or submit improvements and new features.

## License

This project is licensed under the MIT License.

---

*Happy Data Visualizing!*