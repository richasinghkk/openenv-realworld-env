from openenv_env.models import Observation

from openenv_env.tasks.task1_email import task_data as t1
from openenv_env.tasks.task2_cleaning import task_data as t2
from openenv_env.tasks.task3_code_review import task_data as t3

from openenv_env.tasks.graders import (
    grade_email,
    grade_cleaning,
    grade_code
)


class OpenEnv:

    def __init__(self):

        self.tasks = [t1, t2, t3]
        self.index = 0

    def reset(self):

        self.index = 0

        return Observation(
            task_id=0,
            input_data=self.tasks[0]["input"]
        )

    def step(self, action):

        task = self.tasks[self.index]

        if self.index == 0:

            score = grade_email(
                action.response,
                task["truth"]
            )

        elif self.index == 1:

            score = grade_cleaning(
                action.response,
                task["truth"]
            )

        else:

            score = grade_code(
                action.response,
                task["truth"]
            )

        self.index += 1

        done = self.index >= len(self.tasks)

        if not done:

            next_obs = Observation(
                task_id=self.index,
                input_data=self.tasks[self.index]["input"]
            )

        else:

            next_obs = None

        return next_obs, score, done, {}

    def state(self):

        return {
            "current_task": self.index
        }