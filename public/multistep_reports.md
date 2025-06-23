# Step Indices

## General Formula of the Step/Skewedstep/Multistep Indices

For our discrete-time random walk, the position at time $t$ is given by the following equation:

$$
x_t = x_0 + \sum_{i=1}^{t} s_i
$$

where:
- $x_t$ is the position at time $t$,
- $x_0$ is the initial position,
- $s_i$ represents the step taken at time $i$, which is randomly selected from a set of possible step sizes, each associated with a specific probability.

The steps $s_i$ are independently distributed, drawn from a predefined set of step sizes with associated probabilities. This setup results in a model where the movement direction and magnitude at each step are stochastic.

## Parameters

The parameters for the random walk are defined in terms of the step sizes and their associated probabilities:

### Single-Step Indices – step100 to step500


| **Index** | **Step sizes** | **Probabilities** | **CumSum** |
|-----------|----------------|-------------------|------------|
| **step100** | 0.1  ;  -0.1 | 0.5  ;  0.5 | 0.5  ;  1.0 |
| **step200** | 0.2  ;  -0.2 | 0.5  ;  0.5 | 0.5  ;  1.0 |
| **step300** | 0.3  ;  -0.3 | 0.5  ;  0.5 | 0.5  ;  1.0 |
| **step400** | 0.4  ;  -0.4 | 0.5  ;  0.5 | 0.5  ;  1.0 |
| **step500** | 0.5  ;  -0.5 | 0.5  ;  0.5 | 0.5  ;  1.0 |

### MT5 | SkewStepRNG +

| **Step size** | -1   | 0.1  | 0.2  | 0.3  | 0.4  |
|---------------|------|------|------|------|------|
| **Probabilities** | 10.00% | 83.00% | 5.00% | 1.00% | 1.00% |
| **Cumulative Sum** | 10.00% | 93.00% | 98.00% | 99.00% | 100.00% |



### MT5 | SkewStepRNG -



| **Step size** | -0.4 | -0.3 | -0.2 | -0.1 | 1    |
|---------------|------|------|------|------|------|
| **Probabilities** | 1.00% | 1.00% | 5.00% | 83.00% | 10.00% |
| **Cumulative Sum** | 1.00% | 2.00% | 7.00% | 90.00% | 100.00% |

### cTrader | SkewStepRNG +

| **Step size** | -0.5 | 0.1  | 0.2  | 0.3  |
|---------------|------|------|------|------|
| **Probabilities** | 20.00% | 65.00% | 10.00% | 5.00% |
| **Cumulative Sum** | 20.00% | 85.00% | 95.00% | 100.00% |

### cTrader | SkewStepRNG -

| **Step size** | -0.3 | -0.2 | -0.1 | 0.5  |
|---------------|------|------|------|------|
| **Probabilities** | 5.00% | 10.00% | 65.00% | 20.00% |
| **Cumulative Sum** | 5.00% | 15.00% | 80.00% | 100.00% |

### Multi Step Index 2 - multistpRNG2

| **Step size**     | 0.5  | 0.1   | -0.1  | -0.5  |
|--------------|------|-------|-------|-------|
| **Probabilities** | 0.025| 0.475 | 0.475 | 0.025 |
| **CumSum**        | 0.025| 0.5   | 0.975 | 1.0   |

### Multi Step Index 3 - multistpRNG3

| **Step size**     | 0.5  | 0.25  | 0.1   | -0.1  | -0.25 | -0.5  |
|--------------|------|-------|-------|-------|-------|-------|
| **Probabilities** | 0.015| 0.01  | 0.475 | 0.475 | 0.01  | 0.015 |
| **CumSum**        | 0.015| 0.025 | 0.5   | 0.975 | 0.985 | 1.0   |

### Multi Step Index 4 - multistpRNG4

| **Step size**     | 0.5  | 0.3   | 0.2   | 0.1   | -0.1  | -0.2  | -0.3  | -0.5  |
|--------------|------|-------|-------|-------|-------|-------|-------|-------|
| **Probabilities** | 0.005| 0.01  | 0.01  | 0.475 | 0.475 | 0.01  | 0.01  | 0.005 |
| **CumSum**        | 0.005| 0.015 | 0.025 | 0.5   | 0.975 | 0.985 | 0.995 | 1.0   |


### Sample Paths

![Sample paths for selected Step/SkewStep/MultiStep indices](public/indices/step_sample_path.png)


## Monte-Carlo Simulation

The Monte-Carlo simulation generates random walks for each index configuration. For each index:
1. Random steps are generated according to the defined probabilities
2. The path is calculated as the cumulative sum of steps, starting from the initial value
3. Simple and logarithmic returns are calculated
4. Annualized volatility is computed for both simple and logarithmic returns


## Statistical Analysis

Additional statistical analysis includes:
- Generation of multiple sample paths for each index
- Analysis of the distribution of final positions
- Calculation of empirical moments:
  - Drift (mean step)
  - Variance
  - Skewness
  - Kurtosis
  - Annualized volatility (simple %)

### Monte Carlo Simulation Results

![Monte Carlo simulation results](public/indices/step_mc.png)

### Empirical Moments

| Proposal               | Drift $\mu$ | Variance $\sigma^{2}$ |  Skewness | Kurtosis (excess) | Ann. Vol (simple %) |
| ---------------------- | ----------: | --------------------: | --------: | ----------------: | ------------------: |
| **step100**            |    0.000039 |             10.093902 | -0.002927 |         -0.069575 |            5.615678 |
| **step200**            |   -0.000154 |             39.554205 | -0.006466 |          0.032084 |           11.231421 |
| **step300**            |   -0.000174 |             89.063831 | -0.003794 |          0.026419 |           16.847150 |
| **step400**            |    0.000193 |            160.128560 | -0.000200 |          0.013399 |           22.462659 |
| **step500**            |    0.000174 |            249.985989 |  0.003734 |          0.017695 |           28.078197 |
| **MT5 SkewStep +**     |   -0.000077 |            115.515034 | -0.079264 |         -0.016465 |           18.865530 |
| **MT5 SkewStep −**     |    0.000089 |            109.559969 |  0.048164 |          0.000003 |           18.865873 |
| **cTrader SkewStep +** |    0.000057 |             64.262883 | -0.024874 |          0.052312 |           14.317838 |
| **cTrader SkewStep −** |    0.000138 |             66.662378 |  0.037495 |          0.006057 |           14.321810 |
| **multistpRNG2**       |   -0.000013 |             22.141016 |  0.007043 |         -0.003183 |            8.330607 |
| **multistpRNG3**       |    0.000053 |             18.458777 | -0.037137 |         -0.044343 |            7.589326 |
| **multistpRNG4**       |    0.000007 |             14.971622 | -0.006700 |         -0.051282 |            6.782722 |


## Probability of Index Dropping Below Zero

The probability that an index drops below zero is estimated for various time horizons (1, 3, 5, 10, and 20 years). This calculation relies on the Central Limit Theorem (CLT).

#### Model

$$
x_t = x_0 + \sum_{i=1}^{t} s_i, \qquad s_i \stackrel{\text{i.i.d.}}{\sim} \{(x_j,p_j)\}_{j=1}^{k}
$$

Where:
- $x_0 = 10,000$
- $\mu = \mathbb{E}[s_i] = \sum x_j p_j$
- $\sigma^{2} = \operatorname{Var}(s_i) = \sum x_j^{2}p_j - \mu^{2}$

#### Normal Approximation (via CLT)

Because the $s_i$ are i.i.d. with finite $\mu$ and $\sigma^{2}$:

$$
x_t \;\approx\; \mathcal{N}\!\bigl(x_0 + n\mu,\; n\sigma^{2}\bigr), \qquad n = \text{steps in the chosen horizon}.
$$



$$
P\!\bigl(x_t < 0\bigr) \;=\; \Phi\!\left(\dfrac{-x_0 - n\mu}{\sqrt{n}\,\sigma}\right)
$$

with $\Phi$ the standard-normal CDF.




### Results

Probability that the index drops below zero (P(x_t < 0) %) for different time horizons:

| Proposal                | 1 yr | 3 yr | 5 yr | 10 yr | 20 yr |
|-------------------------|-----:|-----:|-----:|------:|------:|
| **MT5 SkewStep −**      | 0.000006 | 0.110252 | 0.886666 | 4.680557 | 11.789611 |
| **MT5 SkewStep +**      | 0.000006 | 0.110252 | 0.886666 | 4.680557 | 11.789611 |
| **cTrader SkewStep −**  | 0.000000 | 0.002759 | 0.089327 | 1.359718 | 5.916772 |
| **cTrader SkewStep +**  | 0.000000 | 0.002759 | 0.089327 | 1.359718 | 5.916772 |
| **multistpRNG2**        | 0.000000 | 0.000000 | 0.000004 | 0.007337 | 0.363145 |
| **multistpRNG3**        | 0.000000 | 0.000000 | 0.000000 | 0.001534 | 0.160190 |
| **multistpRNG4**        | 0.000000 | 0.000000 | 0.000000 | 0.000158 | 0.049145 |
| **step100**             | 0.000000 | 0.000000 | 0.000000 | 0.000001 | 0.003419 |
| **step200**             | 0.000000 | 0.000014 | 0.003419 | 0.243452 | 2.324537 |
| **step300**             | 0.000000 | 0.030514 | 0.397075 | 3.025574 | 9.220910 |
| **step400**             | 0.000426 | 0.508120 | 2.324537 | 7.959719 | 15.975747 |
| **step500**             | 0.018441 | 1.988146 | 5.561058 | 13.003431 | 21.291021 |

