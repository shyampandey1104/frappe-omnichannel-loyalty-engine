# Frappe Omnichannel Retail Loyalty & Tier Progression Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Retail](https://img.shields.io/badge/D2C%20Retail-Omnichannel%20Loyalty-pink.svg)](https://frappe.io)

Omnichannel customer engagement engine offering dynamic tier progression (Silver, Gold, Platinum), spending multipliers, and anti-fraud redemption velocity checks.

## Features
- **Dynamic Tier Upgrades:** Real-time customer milestone promotion based on trailing annual purchase values.
- **Velocity Anti-Fraud Caps:** Prevents cashier or user fraud by limiting point redemption to 50% of basket totals.
- **FIFO Expiration Protection:** Limits unredeemed point liabilities on corporate balance sheets.

## Tests
```bash
python3 -m unittest discover tests
```
