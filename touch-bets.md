---
layout: page
title: Touch Bets
permalink: /touch-bets/
---

# Touch Bets

When a client buys a Touch Option, the client predicts whether the market will touch or not touch the target price at any time during the contract period.

## Analysis Overview

Analysis based on recent trading data for Touch Bets products.

## Risk Metrics

### PnL Distribution
![Weighted Histogram of Company PnL for Touch Bets Products](/quants-model-validation/source/products/touch_pnl_hist.png)

The histogram above displays the weighted distribution of company PnL for Touch Bets products. 

### Maximum Drawdown

![Cumulative PnL and Maximum Drawdown for Touch Bets Products](/quants-model-validation/source/products/touch_cum_pnl.png)

The maximum drawdown of \$1,846.54 occurred during a 5-hour 46-minute period:
- Peak at 2025-06-10 18:22:55+00:00 with cumulative PnL of \$11,735.94
- Trough at 2025-06-11 00:08:54+00:00 with cumulative PnL of \$9,889.40

### Statistical Performance Measures

| Metric | Value |
|--------|-------|
| Weighted Mean PnL per \$1 staked | 0.0385 |
| Weighted Std Dev of PnL per \$1 | 0.8149 |
| 99% Value at Risk (VaR) per \$1 | -2.2315 |
| 99% Expected Shortfall per \$1 | -3.3456 |
| Maximum Drawdown (\$) | 1,846.54 |

### Interpretation

The positive weighted mean PnL of 3.85 cents per dollar staked indicates that Touch Bets are the most profitable product type for the company on average among the analyzed products. However, this comes with significantly higher volatility, as evidenced by the standard deviation of 0.8149, which is higher than both Accumulators and Digits products.

The 99% VaR of -\$2.2315 per dollar staked and Expected Shortfall of -\$3.3456 are also notably higher than other products, indicating greater potential for extreme losses. This risk-reward profile is characteristic of Touch options, where the binary nature of outcomes (touch or no-touch) creates more pronounced volatility in returns.
