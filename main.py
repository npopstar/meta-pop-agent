import matplotlib.pyplot as plt
import random

# =========================
# Meta POP Agent Visual Demo
# =========================

plt.ion()

price_pop_area = [-8, 2]
experience_pop_area = [8, 2]
start_area = [0, -8]

agents = []

for i in range(10):
    agent_type = random.choice([
        "価格重視",
        "品質重視",
        "家族向け",
        "健康意識",
        "発見好き",
        "料理好き"
    ])

    if agent_type == "価格重視":
        target = price_pop_area
        choice = "価格訴求 POP"
    else:
        target = experience_pop_area
        choice = "体験数字 POP"

    agents.append({
        "id": i + 1,
        "x": start_area[0] + random.uniform(-1, 1),
        "y": start_area[1] + random.uniform(-1, 1),
        "target": target,
        "type": agent_type,
        "choice": choice
    })

for step in range(40):
    plt.clf()
    plt.xlim(-12, 12)
    plt.ylim(-10, 8)
    plt.grid(True)
    plt.title(f"Meta POP Agent Simulation | Step {step}")

    plt.scatter(price_pop_area[0], price_pop_area[1], s=700, marker="s")
    plt.text(price_pop_area[0], price_pop_area[1] + 1.2, "PRICE POP\n198 yen", ha="center")

    plt.scatter(experience_pop_area[0], experience_pop_area[1], s=700, marker="s")
    plt.text(experience_pop_area[0], experience_pop_area[1] + 1.2, "EXPERIENCE POP\nSugar 12", ha="center")

    plt.scatter(start_area[0], start_area[1], s=300, marker="^")
    plt.text(start_area[0], start_area[1] - 1, "Entrance", ha="center")

    price_count = 0
    experience_count = 0

    for agent in agents:
        dx = agent["target"][0] - agent["x"]
        dy = agent["target"][1] - agent["y"]

        agent["x"] += dx * 0.08
        agent["y"] += dy * 0.08

        if agent["choice"] == "価格訴求 POP":
            price_count += 1
            marker = "o"
        else:
            experience_count += 1
            marker = "*"

        plt.scatter(agent["x"], agent["y"], s=120, marker=marker)

    plt.text(-11, 7, f"Price: {price_count}\nExperience: {experience_count}")

    plt.pause(0.2)

plt.ioff()

print("=== Result ===")
print(f"価格POP: {price_count}")
print(f"体験POP: {experience_count}")

plt.show()
