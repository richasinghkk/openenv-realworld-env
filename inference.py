from openenv_env.env import OpenEnv
from openenv_env.models import Action

print("Starting inference...")

env = OpenEnv()

obs = env.reset()

print("Environment loaded.")
print("Using dummy responses.")

total_score = 0
task_count = 0

while True:

    # Always use dummy response
    dummy_response = "spam"

    action = Action(
        response=dummy_response
    )

    obs, reward, done, info = env.step(action)

    print("Reward received:", reward)

    if "feedback" in info:
        print("Feedback:", info["feedback"])

    total_score += reward
    task_count += 1

    if done:
        break

average_score = total_score / task_count

print("\nFinal Score:", total_score)
print("Average Score:", average_score)