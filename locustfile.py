from locust import HttpUser, between, task


class MyLocust(HttpUser):
     wait_time = between(1000,2000)
     
     @task(1)
     def user_action(self):
         self.client.get("/api/users")

     @task(2)
     def user_aciton2(self):
         self.client.get("/api/users/2")
