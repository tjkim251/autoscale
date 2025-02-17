from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 3)  # 요청 간 간격 (1~3초)

    @task
    def load_test(self):
        self.client.get("/cpu")