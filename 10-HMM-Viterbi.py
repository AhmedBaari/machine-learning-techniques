# Credit: Ahmed Baari
emission_probs = {
    "CP": {"cola": 0.6, "ice_tea": 0.1, "lem": 0.3}, 
    "IP": {"cola": 0.1, "ice_tea": 0.7, "lem": 0.2}
    }
alpha_a = 1
alpha_b = 0

for _ in range(3):
    state = input("Enter the state:")
    alpha_a = max(alpha_a * 0.7 * emission_probs["CP"][state], 
                           alpha_b * 0.5 * emission_probs["IP"][state])
                           
    alpha_b = max(alpha_a * 0.3 * emission_probs["CP"][state], 
                           alpha_b * 0.5 * emission_probs["IP"][state])
    print(alpha_a, alpha_b)
    print("CP" if alpha_a > alpha_b else "IP")