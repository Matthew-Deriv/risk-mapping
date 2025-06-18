---
layout: page
title: Digits
permalink: /digits/
---

# Digits

When a client buys a Digits contract, the client has a prediction on the last digits of the last tick of a contract. There are three types of Digits Contracts.

* Matches/Differs - Predict what number will be the last digit of the last tick of a contract.
* Even/Odd - Predict whether the last digit of the last tick of a contract will be an even number or an odd number.
* Over/Under - Predict whether the last digit of the last tick of a contract will be higher or lower than a specific number.

## Analysis Overview

Analysis based on 1.4 million trades on Digits between 2025-06-08 18:20:22+00:00 to 2025-06-11 05:35:46+00:00.

## Risk Metrics

### PnL Distribution
![Weighted Histogram of Company PnL for Digits Products](/risk-mapping/source/products/digits_pnl_hist.png)

The histogram above displays the weighted distribution of company PnL for Digits products. While the distribution appears skewed toward negative values, the company actually maintains profitability. This is because we experience a high frequency of small losses (per $1 stake) but consistently win larger amounts on fewer trades, resulting in a positive expected value overall.

### Maximum Drawdown

![Cumulative PnL and Maximum Drawdown for Digits Products](/risk-mapping/source/products/digits_cum_pnl.png)

The maximum drawdown of $15,341.85 occurred during a 2-hour 20-minute period:
- Peak at 2025-06-10 15:03:33+00:00 with cumulative PnL of $109,818.43
- Trough at 2025-06-10 17:23:46+00:00 with cumulative PnL of $94,476.58

### Statistical Performance Measures

| Metric | Value |
|--------|-------|
| Weighted Mean PnL per $1 staked | 0.0178 |
| Weighted Std Dev of PnL per $1 | 0.6957 |
| 99% Value at Risk (VaR) per $1 | -1.4272 |
| 99% Expected Shortfall per $1 | -1.9715 |
| Maximum Drawdown ($) | 15,341.85 |

### Interpretation

The positive weighted mean PnL indicates that on average, the company profits approximately 1.78 cents per dollar staked on Digits products. 

However, the standard deviation is relatively high (0.6957), reflecting the wide range of probabilities and payout structures across different contract types, such as Digit Match versus Digit Higher.

The 99% VaR of -\$1.4272 per dollar staked indicates that, with 99% confidence, the maximum loss per dollar will not exceed \$1.4272 in normal market conditions. The Expected Shortfall of -\$1.9715 represents the average loss in the worst 1% of scenarios.
