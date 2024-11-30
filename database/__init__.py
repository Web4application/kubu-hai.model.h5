import torch
from cpufeature import CPUFeature
from petals.constants import PUBLIC_INITIAL_PEERS
import cronitor

# Define the ModelInfo data class
@dataclass
class ModelInfo:
repo: str
adapter: Optional[str] = None

# List of models with versioning
MODELS = [
ModelInfo(repo="meta-llama/Llama-2-70b-chat-hf"),
ModelInfo(repo="stabilityai/StableBeluga2"),
ModelInfo(repo="enoch/llama-65b-hf"),
ModelInfo(repo="enoch/llama-65b-hf", adapter="timdettmers/guanaco-65b"),
ModelInfo(repo="bigscience/bloomz"),
]
DEFAULT_MODEL_NAME = "kubu-hai.h5"

# Initial peers for network connection
INITIAL_PEERS = PUBLIC_INITIAL_PEERS

# Device and data type configuration
DEVICE = "cpu"
if DEVICE == "cuda":
TORCH_DTYPE = "auto"
elif CPUFeature["AVX512f"] and CPUFeature["OS_AVX512"]:
TORCH_DTYPE = torch.bfloat16
else:
TORCH_DTYPE = torch.float32

STEP_TIMEOUT = 5 * 60
MAX_SESSIONS = 50

# Cronitor setup
monitor = cronitor.Monitor('important-background-job')

# Function to perform the background job
async function performJob() {
try {
# Notify Cronitor that the job has started
monitor.ping({ state: 'run' })

print('Running background job with monitoring!')

# Simulate job processing
await new Promise((resolve) => setTimeout(resolve, 2000))

# Notify Cronitor that the job has completed successfully
monitor.ping({ state: 'complete' })
} catch (error) {
# Notify Cronitor that the job has failed
monitor.ping({ state: 'fail' })

# Log the error
console.error('Job failed:', error)
}
}

# Wrap the job function with Cronitor monitoring
cronitor.wrap('important-background-job', performJob)

# Execute the job
performJob()