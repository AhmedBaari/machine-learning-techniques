# A: forward procedure
# Credit: Raghavender
emission_probs = {'A': {'K': 0.4, 
                        'T': 0.5}, 
                  'B': {'K': 0.3, 
                        'T': 0.3}
                        }
alpha_a = 1
alpha_b = 0
alpha_A = [alpha_a]
alpha_B = [alpha_b]

visible_states = ['K', 'T','K']  # Update with the actual visible states

for state in visible_states:
    old_alpha = alpha_a
    alpha_a = (alpha_a * 0.2 * emission_probs["A"][state]) + (alpha_b * 0.6 * emission_probs["B"][state])
    alpha_b = (old_alpha * 0.8 * emission_probs["A"][state]) + (alpha_b * 0.4 * emission_probs["B"][state])
    alpha_A.append(alpha_a)
    alpha_B.append(alpha_b)

print(alpha_A)
print(alpha_B)

# B. BACKWARD PROCEDURE
# Credit: Ahmed Baari
# Backward
emission_probs = {
    'A': {'K': 0.4, 'T': 0.5}, 
    'B': {'K': 0.3, 'T': 0.3}
    }

b_A = 1
b_B = 1
beta_A = [b_A]
beta_B = [b_B]

for state in reversed(visible_states):
    old_bA = b_A

    b_A = (
        b_A * 0.2 * emission_probs["A"][state]
    ) + (  
        b_B * 0.8 * emission_probs["A"][state]
    )

    b_B = (
        old_bA * 0.6 * emission_probs["B"][state]
    ) + (
        b_B * 0.4 * emission_probs["B"][state]
    )         

    beta_A.append(b_A)
    beta_B.append(b_B)

# Reverse the Beta list for correct order
beta_A.reverse()
beta_B.reverse()


# C. BEST STATE SEQUENCE 
# Credit: Ahmed Baari 
gamma_A = []
gamma_B = []

# alpha * beta of A / that of A + that of B

for i in range(3):
    g_A = (
        alpha_A[i] * beta_A[i]
    ) / (
        alpha_A[i]*beta_A[i] + alpha_B[i]*beta_B[i]
    )
    g_B = (
        alpha_B[i] * beta_B[i] 
    ) / (
        alpha_B[i] * beta_B[i] + alpha_A[i] * beta_A[i]
    )

    gamma_A.append(g_A)
    gamma_B.append(g_B)

for i in range(3):
    print( 
        "A" if gamma_A[i] > gamma_B[i] else "B", 
        end=" "
    )