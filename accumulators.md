---
layout: page
title: Accumulators
permalink: /accumulators/
---

# Accumulators

This product lets clients profit from small price movements of an asset, as long as the price stays within specified ranges that adjust with each tick. If the price touches or breaches these ranges, the product becomes worthless. The payout grows exponentially with every tick as long as the range is not breached.

## Accumulator Barrier

Upper and lower barrier is given by:

$$\text{upper barrier} = \text{spot price} (1 + \text{barrier size})$$

$$\text{lower barrier} = \text{spot price} (1 - \text{barrier size})$$

To obtain an expression for barrier size,

$$ P(\text{Loss}) = P\left(\frac{S_t - S_{t-1}}{S_{t-1}} > b\right) + P\left(\frac{S_t - S_{t-1}}{S_{t-1}} < -b\right) $$

where $b = barrrier \space size$ 


## Probability of Zero Payoff
Each tick of an open accumulator contract can be thought of as a new single tick accumulator contract with a different stake. Therefore, the probability of zero payoff (client side) is simply the loss probability (at time of writing):

| Growth Rate | Loss Probability |
|-------------|------------------|
| 0.01        | 0.015            |
| 0.02        | 0.023            |
| 0.03        | 0.033            |
| 0.04        | 0.0425           |
| 0.05        | 0.0535           |


## Risk Metrics

### PnL Distribution
![Weighted Histogram of Company PnL for Accumulator Products](/quants-model-validation/source/products/accu_pnl_hist.png)

The histogram above displays the weighted distribution of company PnL for Accumulator products. The distribution shows the risk-reward profile of Accumulators, where the company experiences a specific pattern of gains and losses based on barrier breaches and successful contracts.

### Maximum Drawdown
![Cumulative PnL and Maximum Drawdown for Accumulator Products](/quants-model-validation/source/products/accu_cum_pnl.png)

The maximum drawdown of \$1,373.68 occurred during a 52-minute period:
- Peak at 2025-06-15 16:50:30+00:00 with cumulative PnL of \$4,205.20
- Trough at 2025-06-15 17:42:10+00:00 with cumulative PnL of \$2,831.52

### Statistical Performance Measures

| Metric | Value |
|--------|-------|
| Weighted Mean PnL per \$1 staked | 0.0129 |
| Weighted Std Dev of PnL per \$1 | 0.4518 |
| 99% Value at Risk (VaR) per \$1 | -1.1070 |
| 99% Expected Shortfall per \$1 | -1.8617 |
| Maximum Drawdown (\$) | 1,373.68 |

### Interpretation

The positive weighted mean PnL of 1.29 cents per dollar staked indicates that Accumulators are profitable for the company on average. The standard deviation (0.4518) is lower than that of Digits products, suggesting somewhat less volatility in returns.

The 99% VaR of -\$1.1070 per dollar staked shows that, with 99% confidence, the maximum loss per dollar will not exceed \$1.1070 in normal market conditions. The Expected Shortfall of -\$1.8617 represents the average loss in the worst 1% of scenarios, providing insight into potential extreme losses.

## Max Drawdown (Worse Case)
Below is an analysis of worse case scenario based on currently BO limits.  

### Parameters
- Maximum Tick Durations:
  - Growth Rate 0.01: 250 ticks
  - Growth Rate 0.02: 125 ticks
  - Growth Rate 0.03: 85 ticks
  - Growth Rate 0.04: 65 ticks
  - Growth Rate 0.05: 50 ticks
- Maximum Aggregate Open Stake: 5000 for each growth rate
- Target Amount: 6000

### Results

| Growth Rate | Initial Stake | Number of Positions | Remainder | Total Payout |
|-------------|---------------|---------------------|-----------|--------------|
| 0.01        | 498.66        | 10                  | 13.40     | 60,160.78    |
| 0.02        | 504.81        | 9                   | 456.71    | 59,428.05    |
| 0.03        | 486.39        | 10                  | 136.10    | 61,678.54    |
| 0.04        | 468.79        | 10                  | 312.10    | 63,993.68    |
| 0.05        | 523.22        | 9                   | 291.02    | 57,337.00    |

**Total Payout for 1 Symbol**: 302,598.05\$  <br>
**Total Loss for 1 Symbol**: 277,598.05\$ <br>
**Total Payout for 10 Symbols**: 3,025,980.46\$ <br>
**Total Loss for 10 Symbols**: 2,775,980.46\$


### Probability of above occurence
The probability of max drawdown is calculated as:
- For 1 symbol: 
  $100 \times (1 - 0.0535)^{50} \times (1 - 0.0425)^{(65-50)} \times (1 - 0.033)^{(85-65)} \times (1 - 0.023)^{(125-85)} \times (1 - 0.015)^{(250-125)} = 0.10161398822172756\%$
  <br>
- For 10 symbols: 
  $({Probability\space  for\space  1\space  symbol})^{10} = 1.173640187596948 \times 10^{-10}\%$
