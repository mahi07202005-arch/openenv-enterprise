from env.core_env import OpenEnv
from env.models import simple_model
from env.tasks import get_task
from env.graders import grade
from env.reward import compute_reward

def main():
    env = OpenEnv()
    state = env.reset()

    task = get_task()
    print("\n🧠 Task:", task)

    done = False
    step_count = 0

    while not done:
        print(f"\n--- Step {step_count + 1} ---")

        # Step 1: Model generates response
        action = simple_model(task)
        print("🤖 Model Output:", action)

        # Step 2: Evaluate response
        score = grade(action)
        reward = compute_reward(score)

        print("📊 Score:", score)
        print("🏆 Reward:", reward)

        # Step 3: Improve task if bad output
        if score == 0:
            task = f"Improve this answer: {action}"
            print("🔁 Improving task...")

        # Step 4: Environment step
        state, _, done, _ = env.step(action)
        print("📦 State:", state)

        step_count += 1

    print("\n✅ Finished Execution")

if __name__ == "__main__":
    main()