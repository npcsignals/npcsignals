"""Retain the superseded aggregate calculation separately from authoritative raw fills."""
from pathlib import Path
import json
p=Path(__file__).resolve().parent/'evidence/financial_reconciliation.json'
f=json.loads(p.read_text())
legacy=['xmr1_buy_quantity','xmr1_sold_all_returned','gross_proceeds_all_returned_usdc','usdc_trade_fees_all_returned','net_xmr1_sale_proceeds_usdc','last_sale_utc','first_sale_utc','through_13utc_quantity','through_13utc_gross_usdc','expected_xmr1_before_unexplained_adjustment','xmr1_residual_unresolved']
f.setdefault('superseded_aggregate_calculation',{}).update({k:f.pop(k)for k in legacy if k in f})
f['superseded_aggregate_calculation']['warning']='retained for audit; superseded by raw_fill_reconciliation; initial balance calculation omitted pre-funding buy and token-denominated fee'
p.write_text(json.dumps(f,indent=2))
