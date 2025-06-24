# Products of Deriv 

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
