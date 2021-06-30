from locust import HttpUser, between, task


class MyLocust(HttpUser):
     wait_time = between(1000,2000)
     
     @task
     def user_action(self):
         self.client.get("/")

