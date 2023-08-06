# cdktf-gitlab-runner

### Example

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import cdktf_cdktf_provider_google as gcp
import cdktf as cdktf
from constructs import Construct
from ..index import GitlabRunnerAutoscaling

class IntegDefaultStack(cdktf.TerraformStack):
    def __init__(self, scope, id):
        super().__init__(scope, id)
        local = "asia-east1"
        project_id = f"{process.env.PROJECT_ID}"
        provider = gcp.GoogleProvider(self, "GoogleAuth",
            region=local,
            zone=local + "-c",
            project=project_id
        )
        GitlabRunnerAutoscaling(self, "GitlabRunnerAutoscaling",
            gitlab_token=f"{process.env.GITLAB_TOKEN}",
            provider=provider
        )

app = cdktf.App()
IntegDefaultStack(app, "gitlab-runner")
app.synth()
```
