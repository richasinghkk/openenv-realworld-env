print("Starting inference...")

from openenv_env.env import OpenEnv
from openenv_env.models import Action

print("Environment loaded.")

env = OpenEnv()

obs = env.reset()

print("First Observation:", obs)

total_score = 0

while True:

    # Temporary fixed answer
    dummy_response = "spam"

    action = Action(
        response=dummy_response
    )

    obs, reward, done, _ = env.step(action)

    print("Reward received:", reward)

    total_score += reward

    if done:
        break

print("Final Score:", total_score)