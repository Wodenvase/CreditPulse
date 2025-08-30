def calculate_duration(bond_data, discount_rate):
    """
    Calculate Macaulay duration as a placeholder.
    Expects bond_data to have a 'cash_flows' key with a list of numbers.
    """
    cash_flows = bond_data.get("cash_flows", [5, 5, 105])  # Example: 2 coupons + principal
    # Ensure all cash flows are floats
    cash_flows = [float(cf) for cf in cash_flows]
    discount_rate = float(discount_rate) / 100  # Convert percent to decimal if needed

    duration = sum([(t+1) * cf / ((1 + discount_rate) ** (t+1)) for t, cf in enumerate(cash_flows)]) / \
               sum([cf / ((1 + discount_rate) ** (t+1)) for t, cf in enumerate(cash_flows)])
    return round(duration, 2)

def calculate_convexity(bond_data):
    """
    Calculate convexity as a placeholder.
    Expects bond_data to have a 'cash_flows' key with a list of numbers.
    """
    cash_flows = bond_data.get("cash_flows", [5, 5, 105])
    cash_flows = [float(cf) for cf in cash_flows]
    discount_rate = 0.05  # Example fixed rate

    convexity = sum([(t+1)*(t+2)*cf / ((1 + discount_rate) ** (t+3)) for t, cf in enumerate(cash_flows)]) / \
                sum([cf / ((1 + discount_rate) ** (t+1)) for t, cf in enumerate(cash_flows)])
    return round(convexity, 2)

def yield_curve_shift(yield_curve, shift_amount):
    return [rate + shift_amount for rate in yield_curve]

def credit_risk_signal(bond_rating, market_conditions):
    if bond_rating in ['AAA', 'AA']:
        return 'Low Risk'
    elif bond_rating in ['A', 'BBB']:
        return 'Moderate Risk'
    else:
        return 'High Risk'