# BananaPyStocks

A web-based stock market simulator built with **Flask**. Eight fictional companies have prices that move on their own in the background; users sign up, submit buy and sell requests, and an admin approves them.

## Features

- **Live-moving market:** a simulation process keeps nudging each company's price at random and tracks the percentage change plus the highest and lowest price seen
- **Accounts:** sign up and log in, with a separate admin login
- **Trading requests:** users submit buy and sell requests for a company and quantity
- **Admin console:** review pending buy and sell requests and see all registered users
- **Company pages:** one page per company with its current price, change, high and low
- **Dashboard:** an overview of the market for the logged-in user

## How it works

| File | Role |
|---|---|
| `main.py` | Flask app: routes for login, sign-up, dashboard, trading requests and admin pages |
| `simulation.py` | Price simulation loop, run as its own process alongside the web server |
| `thread.py` | An alternative version of the simulation loop (not used by default) |
| `data.py` | Reads and writes the flat-file data store |
| `Companies.txt`, `Usernames.txt` | Company price data and demo accounts |
| `BuyRequests.txt`, `SellRequests.txt` | Pending requests awaiting admin action |
| `templates/`, `static/` | HTML pages and company logos |

Data is kept in plain text files rather than a database, which keeps the project easy to run and inspect.

## Running it

```bash
pip install -r requirements.txt
python simulation.py   # terminal 1: keeps the prices moving
python main.py         # terminal 2: starts the web app
```

Then open `http://127.0.0.1:5000`. Demo accounts are listed in `Usernames.txt`.

## Notes

This is a learning project. Accounts are stored in plain text and the market is simulated with random price changes, so it is not suitable for real use.
