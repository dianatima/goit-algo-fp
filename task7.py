import random
import matplotlib.pyplot as plt


def roll_dice(num_simulations):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_simulations):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        roll_sum = dice_1 + dice_2
        sum_counts[roll_sum] += 1

    prob = {
        key: value / num_simulations * 100 for key, value in sum_counts.items()
    }

    return sum_counts, prob


num_simulations = 1_000_000
sum_counts, prob = roll_dice(num_simulations)

analytic_prob = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}


print("Monte Carlo results:")
for roll_sum in range(2, 13):
    print(f"{roll_sum}: {prob[roll_sum]:.2f}%")

print("\nAnalytical results:")
for roll_sum in range(2, 13):
    print(f"{roll_sum}: {analytic_prob[roll_sum]:.2f}%")


sums = list(range(2, 13))
mk = [prob[roll_sum] for roll_sum in sums]
analytical_prob = [analytic_prob[roll_sum] for roll_sum in sums]

plt.figure(figsize=(10, 6))
plt.bar(
    sums,
    mk,
    alpha=0.6,
    label="Monte Carlo",
    color="skyblue",
)
plt.plot(sums, analytical_prob, "r-", label="Analytical", marker="o")
plt.xlabel("Sum")
plt.ylabel("Probability (%)")
plt.title("Probability of each sum")
plt.legend()
plt.grid(True)
plt.show()
