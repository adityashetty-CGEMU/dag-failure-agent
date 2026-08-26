import json
import os
import uuid
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(os.environ["GCP_PROJECT"], "dagfailures")

payload = {
    "dag_id": "dag1",
    "task_id": "test_task",
    "run_id": f"e2e-test-{uuid.uuid4().hex[:8]}",
    "try_number": 1,
    "github_repo": "adityashetty-CGEMU/dag-failure-agent",
}

future = publisher.publish(topic_path, json.dumps(payload).encode("utf-8"))
print(f"Published message ID: {future.result()}")
print(f"run_id used: {payload['run_id']}")