# Install pytorch geometric dependencies according to 
# https://gist.github.com/ameya98/b193856171d11d37ada46458f60e73e7
import torch

def format_pytorch_version(version):
  return version.split('+')[0]


def format_cuda_version(version):
  return 'cu' + version.replace('.', '')

if __name__ == "__main__":

    TORCH_version = torch.__version__
    TORCH = format_pytorch_version(TORCH_version)

    CUDA_version = torch.version.cuda
    CUDA = format_cuda_version(CUDA_version)

    print(f'https://pytorch-geometric.com/whl/torch-{TORCH}+{CUDA}.html')
