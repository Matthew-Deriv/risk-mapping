---
layout: home
title: Risk Mapping
---

# Risk Mapping for Deriv Products

Welcome to the Risk Mapping analysis dashboard. This site provides detailed risk metrics and statistical analyses for Deriv's trading products. Use the navigation menu to explore each product's risk profile.

## Products Overview

<div class="product-cards">
  <div class="product-card">
    <h3>Accumulators</h3>
    <p>A product that lets clients profit from small price movements as long as the price stays within specified ranges.</p>
    <ul>
      <li>Mean PnL: 0.0129 per $1 staked</li>
      <li>99% VaR: -1.1070 per $1</li>
      <li>Max Drawdown: $1,373.68</li>
    </ul>
    <a href="{{ site.baseurl }}/accumulators/" class="button">View Details</a>
  </div>

  <div class="product-card">
    <h3>Digits</h3>
    <p>A product where clients predict the last digit of the last tick of a contract.</p>
    <ul>
      <li>Mean PnL: 0.0178 per $1 staked</li>
      <li>99% VaR: -1.4272 per $1</li>
      <li>Max Drawdown: $15,341.85</li>
    </ul>
    <a href="{{ site.baseurl }}/digits/" class="button">View Details</a>
  </div>

  <div class="product-card">
    <h3>Touch Bets</h3>
    <p>A product where clients predict whether the market will touch or not touch a target price during the contract period.</p>
    <ul>
      <li>Mean PnL: 0.0385 per $1 staked</li>
      <li>99% VaR: -2.2315 per $1</li>
      <li>Max Drawdown: $1,846.54</li>
    </ul>
    <a href="{{ site.baseurl }}/touch-bets/" class="button">View Details</a>
  </div>
</div>

## Comparative Analysis

| Product | Mean PnL per $1 | Std Dev | 99% VaR | 99% ES | Max Drawdown |
|---------|-----------------|---------|---------|--------|--------------|
| Accumulators | 0.0129 | 0.4518 | -1.1070 | -1.8617 | $1,373.68 |
| Digits | 0.0178 | 0.6957 | -1.4272 | -1.9715 | $15,341.85 |
| Touch Bets | 0.0385 | 0.8149 | -2.2315 | -3.3456 | $1,846.54 |

This comparative table highlights that Touch Bets offer the highest mean profit per dollar staked (0.0385) but also come with the highest risk metrics, including standard deviation and Value at Risk. Accumulators show the lowest volatility among the three products, while Digits experienced the largest maximum drawdown.
