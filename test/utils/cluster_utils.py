import requests
import json
import subprocess
from resources.config import Config


class Cluster:
    def __init__(self, workspace_url, api_token, cluster_id):
        self.workspace_url = workspace_url
        self.api_token = api_token
        self.cluster_id = cluster_id
        self.job_id = Config.SILVER_JOB_ID

    def start_cluster(self):
        cluster_status = None
        workspace_url = self.workspace_url
        api_token = self.api_token
        cluster_id = self.cluster_id
        # Define your Azure Databricks workspace URL and API token

        # Define the API endpoints for getting cluster information and starting a cluster
        get_cluster_info_endpoint = f'{workspace_url}/api/2.0/clusters/get'
        start_cluster_endpoint = f'{workspace_url}/api/2.0/clusters/start'

        # Define the request headers with the API token
        headers = {
            'Authorization': f'Bearer {api_token}',
            'Content-Type': 'application/json'
        }

        # Define the request payload with the cluster ID
        data = {
            'cluster_id': cluster_id
        }

        # Send a POST request to get cluster information
        response = requests.post(get_cluster_info_endpoint, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            cluster_info = response.json()
            cluster_status = cluster_info['state']

            if cluster_status == 'RUNNING':
                print(f"Cluster '{cluster_id}' is already running.")
                # print(f"Cluster Info: {json.dumps(cluster_info, indent=2)}")
            elif cluster_status == 'TERMINATED':
                # If the cluster is terminated, start it
                response = requests.post(start_cluster_endpoint, headers=headers, data=json.dumps(data))
                if response.status_code == 200:
                    print(f"Cluster '{cluster_id}' was terminated and has been started.")
                else:
                    print(f"Failed to start cluster '{cluster_id}'.")
                    print(f"Response: {response.status_code}, {response.text}")
            else:
                print(f"Cluster '{cluster_id}' is in state: {cluster_status}")
        else:
            print(f"Failed to get cluster information for '{cluster_id}'.")
            print(f"Response: {response.status_code}, {response.text}")
        return cluster_status

    def run_silver_job(self):
        job_id = self.job_id
        cluster_id = self.cluster_id
        # Define the job run configuration as a Python dictionary
        job_run_config = {
            "job_id": job_id,
            "existing_cluster_id": self.cluster_id
        }
        # Serialize the job run configuration to a JSON string
        json_config = json.dumps(job_run_config)

        # Command to run the Databricks job with the JSON argument
        databricks_executable = (r'C:\Users\h548020\AppData\Local\Packages\PythonSoftwareFoundation.Python.3'
                                 r'.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\databricks.exe')
        command = [
            databricks_executable,
            'jobs',
            'run-now',
            '--json',
            json_config
        ]

        try:
            # Run the Databricks job and capture the response
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    text=True)

            if result.returncode == 0:
                # Job ran successfully
                response_json = json.loads(result.stdout)
                print("Job Run Response:")
                print(json.dumps(response_json, indent=2))
            else:
                # Job execution failed
                print("Error running the Databricks job:")
                print(result.stderr)
        except subprocess.CalledProcessError as e:
            # Handle any subprocess error
            print("Error running the Databricks job:")
            print(e.stderr)

# inst = Cluster(Config.WORKSPACE_URL, Config.DATABRICKS_TOKEN, Config.CLUSTER_ID)
# inst.start_cluster()
# inst.run_silver_job()
