import random
import time

from locust import HttpUser, between, task


class ChatUser(HttpUser):
    wait_time = between(5, 20)

    @task
    def ask_question(self):
        self.client.get("/")
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "messages": [
                    {
                        "content": random.choice(
                            [
                                "Good spot to grab a quick coffee in morning?",
                                "Inexpensive Chinese restaurants for 8 people?",
                                "Can you recommend a highly rated Japanese restaurant?",
                            ]
                        ),
                        "role": "user",
                    }
                ],
                "context": {
                    "overrides": {"use_advanced_flow": True, "top": 3, "retrieval_mode": "hybrid", "temperature": 0.3}
                },
            },
        )
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "messages": [
                    {"content": "Good spot to grab a quick coffee in morning?", "role": "user"},
                    {
                        "content": "For the best shoe for hiking, I recommend the Trailblaze Steel-Blue Hiking Shoes.",
                        "role": "assistant",
                    },
                    {"content": "any other options?", "role": "user"},
                ],
                "context": {
                    "overrides": {"use_advanced_flow": True, "top": 3, "retrieval_mode": "hybrid", "temperature": 0.3}
                },
            },
        )
