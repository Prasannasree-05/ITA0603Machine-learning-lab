# Candidate Elimination Algorithm

# Training data
data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
]

# Initialize S and G
S = data[0][:-1]
G = [["?" for _ in range(len(S))]]
print("Initial Specific Hypothesis (S):", S)
print("Initial General Hypothesis (G):", G)
for example in data:
    attributes = example[:-1]
    label = example[-1]

    if label == "Yes":
        # Update S
        for i in range(len(S)):
            if S[i] != attributes[i]:
                S[i] = "?"

        # Remove hypotheses from G that do not match positive example
        G = [g for g in G if all(g[i] == "?" or g[i] == attributes[i] for i in range(len(S)))]

    else:
        # Specialize G for negative example
        new_G = []
        for g in G:
            for i in range(len(S)):
                if g[i] == "?":
                    if S[i] != "?":
                        new_h = g.copy()
                        new_h[i] = S[i]
                        new_G.append(new_h)
        G = new_G

    print("\nTraining Example:", example)
    print("S =", S)
    print("G =", G)

print("\nFinal Specific Hypothesis:")
print(S)

print("\nFinal General Hypothesis:")
for g in G:
    print(g)
