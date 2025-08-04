# stock_auth

## Project Requirements

- **User Authentication**
  - JWT-based registration/login
  - Password hashing (bcrypt/scrypt/Argon2)
  - Protected endpoints (auth required)

- **Stock Data**
  - Fetch real-time prices from external API
  - Symbol validation (e.g., AAPL, TSLA)
  - Basic company info (name, price, change %)

- **Watchlist**
  - Save/retrieve user's favorite stocks
  - Prevent duplicates per user

### Forecasting (Optional)
- `GET /stocks/{symbol}/sma?window=7`  
  Returns simple moving average over N days.  
- Uses cached historical data (no model training).
