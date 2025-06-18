# Risk Mapping for Deriv Products

This repository contains a GitHub Pages site that provides detailed risk metrics and statistical analyses for Deriv's trading products.

## Products Included

- **Accumulators**: A product that lets clients profit from small price movements as long as the price stays within specified ranges.
- **Digits**: A product where clients predict the last digit of the last tick of a contract.
- **Touch Bets**: A product where clients predict whether the market will touch or not touch a target price during the contract period.

## GitHub Pages Site

The site is available at: https://matthewchan.github.io/risk-mapping/

## Local Development

To run this site locally:

1. Clone the repository
2. Install Jekyll and Bundler: `gem install jekyll bundler`
3. Install dependencies: `bundle install`
4. Run the server: `bundle exec jekyll serve`
5. Open your browser at `http://localhost:4000/risk-mapping/`

## Content Structure

- `index.md`: Homepage with product overview
- `accumulators.md`: Detailed analysis of Accumulators product
- `digits.md`: Detailed analysis of Digits product
- `touch-bets.md`: Detailed analysis of Touch Bets product
- `assets/css/main.css`: Custom styling for the site
- `_config.yml`: Jekyll configuration
