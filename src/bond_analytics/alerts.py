import numpy as np
import requests

class SmartAlert:
    def __init__(self, spread_history, bond_id, n8n_webhook_url):
        self.spread_history = np.array(spread_history)
        self.bond_id = bond_id
        self.n8n_webhook_url = n8n_webhook_url

    def is_abnormal_move(self, latest_spread, threshold=2.5):
        mean = np.mean(self.spread_history)
        std = np.std(self.spread_history)
        if std == 0:
            return False, 0
        z_score = abs((latest_spread - mean) / std)
        return z_score > threshold, z_score

    def send_alert(self, message, channel="n8n"):
        payload = {
            "bond_id": self.bond_id,
            "message": message,
            "channel": channel
        }
        try:
            response = requests.post(self.n8n_webhook_url, json=payload, timeout=5)
            return response.status_code == 200
        except Exception as e:
            # Optionally log error here
            return False

# Example usage:
# alert = SmartAlert([100, 102, 98, 101, 99], "ACME2025", "https://n8n.example.com/webhook/alert")
# abnormal, z = alert.is_abnormal_move(120)
# if abnormal:
#     alert.send_alert(f"Abnormal spread move detected! Z-score: {z:.2f}")