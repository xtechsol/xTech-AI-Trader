Added
Integration with Chainlink for real-time market data feeds.
AI model fine-tuning endpoint for custom trading strategies.

Changed
Updated Twitter API integration to use the new v2 endpoints.
Improved the efficiency of Solana transaction handling.

Fixed
Fixed a bug where transaction fees were not accurately calculated for large trades.

[2.5.2] - 2024-08-25
Added
Added support for NFT trading.
WebSocket support for real-time updates from exchanges.

Changed
Updated the AI model to a more recent version from the Hugging Face model hub.

Fixed
Fixed typos in documentation.

[2.5.1] - 2024-08-10
Added
Added multilingual support for tweets to reach a broader audience.

Changed
Enhanced security by implementing a two-factor authentication for trading actions.

Fixed
Fixed a memory leak in the long-running processes.

[2.5.0] - 2024-07-20
Added
New module for risk assessment and portfolio diversification.

Changed
Refactored the AI decision-making module for improved performance and readability.

Fixed
Fixed synchronization issues between different components of the trading system.

[2.4.3] - 2024-07-05
Added
Added dynamic rate limit handling for Twitter API calls.

Fixed
Fixed bug where the system would not recover from internet connectivity issues.

[2.4.2] - 2024-06-15
Added
Added support for real-time market sentiment analysis from Reddit.

Changed
Changed default trading strategy to include sentiment analysis from social media.

Fixed
Fixed improper handling of decimal points in token pricing.

[2.4.1] - 2024-06-01
Added
Added a new utility for historical data analysis.

Fixed
Fixed an issue where the bot was not tweeting during off-peak hours.

[2.4.0] - 2024-05-18
Added
Added support for multiple blockchain networks including Ethereum and Binance Smart Chain.
Added a user interface for manual trade execution.
Implemented token price prediction using machine learning algorithms.

Changed
Switched to asynchronous processing for all blockchain interactions to enhance performance.
Updated the project's documentation to match the new features.

Removed
Removed unused dependencies for reducing project size.

[2.3.4] - 2024-05-03
Added
Added custom error handling for Solana network errors.

Fixed
Fixed race condition in multi-threaded AI decision making.

[2.3.3] - 2024-04-15
Changed
Improved logging to include more detailed transaction logs.

Fixed
Resolved an issue causing intermittent failures in token creation.

[2.3.2] - 2024-04-01
Added
Added a graphical dashboard for monitoring trading activities.

Changed
Reorganized file structure for better project navigation.

Deprecated
Deprecated the use of certain less secure cryptographic methods.

[2.3.1] - 2024-03-20
Added
Added support for stop-loss and take-profit orders.

Fixed
Fixed an error where invalid transactions were being logged.

[2.3.0] - 2024-03-03
Added
Added a simulation mode for testing trading strategies.

Changed
Changed the AI model from GPT-2 to a custom-trained model for better predictions.

Deprecated
Deprecated the tweet_purchase method in favor of post_trade_update.

Removed
Removed external data fetching dependencies, now using internal data caching.
