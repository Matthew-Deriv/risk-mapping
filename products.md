# Products of Deriv 

## Accumulators
This product lets clients profit from small price movements of an asset, as long as the price stays within specified ranges that adjust with each tick. If the price touches or breaches these ranges, the product becomes worthless. The payout grows exponentially with every tick as long as the range is not breached.

#### Accumulator Barrier

Upper and lower barrier is given by:

$$\text{upper barrier} = \text{spot price} (1 + \text{barrier size})$$

$$\text{lower barrier} = \text{spot price} (1 - \text{barrier size})$$

To obtain an expression for barrier size,

$$ P(\text{Loss}) = P\left(\frac{S_t - S_{t-1}}{S_{t-1}} > b\right) + P\left(\frac{S_t - S_{t-1}}{S_{t-1}} < -b\right) $$

where $b = barrrier \space size$ 


#### Probability of Zero Payoff
Each tick of an open accumulator contract can be thought of as a new single tick accumulator contract with a different stake. Therefore, the probability of zero payoff (client side) is simply the loss probability (at time of writing):

| Growth Rate | Loss Probability |
|-------------|------------------|
| 0.01        | 0.015            |
| 0.02        | 0.023            |
| 0.03        | 0.033            |
| 0.04        | 0.0425           |
| 0.05        | 0.0535           |


#### Risk Metrics

##### PnL Distribution
![Weighted Histogram of Company PnL for Accumulator Products](/images/accu_pnl_hist.png)

The histogram above displays the weighted distribution of company PnL for Accumulator products. The distribution shows the risk-reward profile of Accumulators, where the company experiences a specific pattern of gains and losses based on barrier breaches and successful contracts.

##### Maximum Drawdown
![Cumulative PnL and Maximum Drawdown for Accumulator Products](/images/accu_cum_pnl.png)

The maximum drawdown of $1,373.68 occurred during a 52-minute period:
- Peak at 2025-06-15 16:50:30+00:00 with cumulative PnL of $4,205.20
- Trough at 2025-06-15 17:42:10+00:00 with cumulative PnL of $2,831.52

##### Statistical Performance Measures

| Metric | Value |
|--------|-------|
| Weighted Mean PnL per $1 staked | 0.0129 |
| Weighted Std Dev of PnL per $1 | 0.4518 |
| 99% Value at Risk (VaR) per $1 | -1.1070 |
| 99% Expected Shortfall per $1 | -1.8617 |
| Maximum Drawdown ($) | 1,373.68 |

##### Interpretation

The positive weighted mean PnL of 1.29 cents per dollar staked indicates that Accumulators are profitable for the company on average. The standard deviation (0.4518) is lower than that of Digits products, suggesting somewhat less volatility in returns.

The 99% VaR of -\$1.1070 per dollar staked shows that, with 99% confidence, the maximum loss per dollar will not exceed \$1.1070 in normal market conditions. The Expected Shortfall of -$1.8617 represents the average loss in the worst 1% of scenarios, providing insight into potential extreme losses.

 #### Max Drawdown (Worse Case)
Below is an analysis of worse case scenario based on currently BO limits.  

##### Parameters
- Maximum Tick Durations:
  - Growth Rate 0.01: 250 ticks
  - Growth Rate 0.02: 125 ticks
  - Growth Rate 0.03: 85 ticks
  - Growth Rate 0.04: 65 ticks
  - Growth Rate 0.05: 50 ticks
- Maximum Aggregate Open Stake: 5000 for each growth rate
- Target Amount: 6000

##### Results

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
**Total Loss for 10 Symbols**: 2,7759,80.46\$


##### Probability of above occurence
The probability of max drawdown is calculated as:
- For 1 symbol: 
  $100 \times (1 - 0.0535)^{50} \times (1 - 0.0425)^{(65-50)} \times (1 - 0.033)^{(85-65)} \times (1 - 0.023)^{(125-85)} \times (1 - 0.015)^{(250-125)} = 0.10161398822172756\%$
  <br>
- For 10 symbols: 
  $({Probability\space  for\space  1\space  symbol})^{10} = 1.173640187596948 \times 10^{-10}\%$


## Digits
When a client buys a Digits contract, the client has a prediction on the last digits of the last tick of a contract. There are three types of Digits Contracts.

* Matches/Differs - Predict what number will be the last digit of the last tick of a contract.
* Even/Odd - Predict whether the last digit of the last tick of a contract will be an even number or an odd number.
* Over/Under - Predict whether the last digit of the last tick of a contract will be higher or lower than a specific number.

#### Analysis Overview

Analysis based on 1.4 million trades on Digits between 2025-06-08 18:20:22+00:00 to 2025-06-11 05:35:46+00:00.

#### Risk Metrics

##### PnL Distribution
![Weighted Histogram of Company PnL for Digits Products](/images/digits_pnl_hist.png)

The histogram above displays the weighted distribution of company PnL for Digits products. While the distribution appears skewed toward negative values, the company actually maintains profitability. This is because we experience a high frequency of small losses (per $1 stake) but consistently win larger amounts on fewer trades, resulting in a positive expected value overall.
##### Maximum Drawdown

![Cumulative PnL and Maximum Drawdown for Digits Products](/images/digits_cum_pnl.png)
The maximum drawdown of $15,341.85 occurred during a 2-hour 20-minute period:
- Peak at 2025-06-10 15:03:33+00:00 with cumulative PnL of $109,818.43
- Trough at 2025-06-10 17:23:46+00:00 with cumulative PnL of $94,476.58

##### Statistical Performance Measures

| Metric | Value |
|--------|-------|
| Weighted Mean PnL per $1 staked | 0.0178 |
| Weighted Std Dev of PnL per $1 | 0.6957 |
| 99% Value at Risk (VaR) per $1 | -1.4272 |
| 99% Expected Shortfall per $1 | -1.9715 |
| Maximum Drawdown ($) | 15,341.85 |

##### Interpretation

The positive weighted mean PnL indicates that on average, the company profits approximately 1.78 cents per dollar staked on Digits products. 
However, the standard deviation is relatively high (0.6957), reflecting the wide range of probabilities and payout structures across different contract types, such as Digit Match versus Digit Higher
The 99% VaR of -\$1.4272 per dollar staked indicates that, with 99% confidence, the maximum loss per dollar will not exceed \$1.4272 in normal market conditions. The Expected Shortfall of -\$1.9715 represents the average loss in the worst 1% of scenarios.

### Digits Match
#### 99% Value at Risk (VaR) Calculation for a Single Bet

Given a betting scenario:

- **Stake per bet:** $1
- **Probability client wins (company loses):** $p = 0.1$
- **If client wins:** company **loses $9**
- **If client loses:** company **wins $1** (keeps the stake)
- **Probability client loses:** $1-p = 0.9$

##### 1. Define Profit/Loss Variable

Let $X$ be the company's profit per bet:

\[
X =
\begin{cases}
-9 & \text{with probability } 0.1 \\
1 & \text{with probability } 0.9
\end{cases}
\]

---

##### 2. Calculate Mean ($\mu$) and Standard Deviation ($\sigma$):

**Mean:**
\[
\mu = E[X] = 0.1 \times (-9) + 0.9 \times 1 = -0.9 + 0.9 = 0
\]

**Second moment:**
\[
E[X^2] = 0.1 \times (-9)^2 + 0.9 \times 1^2 = 0.1 \times 81 + 0.9 \times 1 = 8.1 + 0.9 = 9.0
\]

**Variance:**
\[
\sigma^2 = E[X^2] - (E[X])^2 = 9.0 - 0^2 = 9.0
\]
\[
\sigma = \sqrt{9.0} = 3.0
\]

---

##### 3. Normal Approximation VaR Calculation

For a 99% VaR (z-score $\approx 2.33$):

\[
\text{99\% VaR} = \mu - 2.33 \sigma = 0 - 2.33 \times 3.0 = -6.99
\]

---

##### 4. **Interpretation**

The 99% VaR is **\$6.99** (rounded to two decimal places).  
This means that in 99% of cases, the company's loss will not exceed \$6.99 **per $1 bet**, according to the normal approximation.

### Digits Differ 
#### 99% Value at Risk (VaR) Calculation for a Single Bet

Given a betting scenario:

- **Stake per bet:** $1
- **Probability client wins:** $p = 0.9$
- **If client wins:** company loses $1/0.9 \approx \$1.11$ (company net loss $-0.11\overline{1}$)
- **If client loses:** company wins $1$

##### 1. Define Profit/Loss Variable

\[
X = 
\begin{cases}
-0.111\overline{1} & \text{with probability } 0.9 \\
1 & \text{with probability } 0.1
\end{cases}
\]

##### 2. Calculate Mean ($\mu$) and Standard Deviation ($\sigma$):

\[
\mu = 0
\]
\[
\sigma \approx 0.3333
\]

##### 3. 99% VaR (z-score = 2.33):

\[
\text{99\% VaR} = 0 - 2.33 \times 0.3333 \approx -0.7767
\]

##### 4. **Interpretation**

The 99% VaR is **\$0.78** (rounded).
This means that in 99% of cases, the company's loss will not exceed **\$0.78 per \$1 bet** (under normal approximation).

## Touch Bets
When a client buys a Touch Option, the client predicts whether the market will touch or not touch the target price at any time during the contract period.

#### Analysis Overview

Analysis based on recent trading data for Touch Bets products.

#### Risk Metrics

##### PnL Distribution
![Weighted Histogram of Company PnL for Touch Bets Products](/images/touch_pnl_hist.png)

The histogram above displays the weighted distribution of company PnL for Touch Bets products. 

##### Maximum Drawdown

![Cumulative PnL and Maximum Drawdown for Touch Bets Products](/images/touch_cum_pnl.png)

The maximum drawdown of $1,846.54 occurred during a 5-hour 46-minute period:
- Peak at 2025-06-10 18:22:55+00:00 with cumulative PnL of $11,735.94
- Trough at 2025-06-11 00:08:54+00:00 with cumulative PnL of $9,889.40

##### Statistical Performance Measures

| Metric | Value |
|--------|-------|
| Weighted Mean PnL per $1 staked | 0.0385 |
| Weighted Std Dev of PnL per $1 | 0.8149 |
| 99% Value at Risk (VaR) per $1 | -2.2315 |
| 99% Expected Shortfall per $1 | -3.3456 |
| Maximum Drawdown ($) | 1,846.54 |

##### Interpretation

The positive weighted mean PnL of 3.85 cents per dollar staked indicates that Touch Bets are the most profitable product type for the company on average among the analyzed products. However, this comes with significantly higher volatility, as evidenced by the standard deviation of 0.8149, which is higher than both Accumulators and Digits products.

The 99% VaR of -\$2.2315 per dollar staked and Expected Shortfall of -$3.3456 are also notably higher than other products, indicating greater potential for extreme losses. This risk-reward profile is characteristic of Touch options, where the binary nature of outcomes (touch or no-touch) creates more pronounced volatility in returns.
