# stock-sim

This project contains a simulator(using previous data) for the performance of a stock market portfolio.
It works by web scraping past data on them from the internet according to their symbol, using the websites posted below, and showing you the potential gains from using monthly dollar-cost-averaging(DCA) and/or for a certain initial investment.

## Configuration
Set up your portfolio in the json file, according to the example shown.
Install dependencies by running(python3 needed): pip3 install -r requirements.txt

## Running
python3 stock_sim.py


## TODO
This is a small hobby project that I may work on from time to time, but the following may be added in the future:
* A UI to set up the config, instead of using a JSON file.
* Support for ETF's in the portfolio(would require finding proper websites with the data).
* Use scrappy instead of beautiful soup(better performance on the scrapping process).
* Cache data locally instead of web scrapping it each time(perhaps using a local sqlite file)

## Website credit

So far, the following websites are scrapped:
* https://www.buyupside.com
