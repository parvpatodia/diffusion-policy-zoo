import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import matplotlib.pyplot as plt
import math
from pyexpat import model
import torch
import torch.nn as nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import torch.nn.functional as F


T = 1000
beta = torch.linspace(0.0001, 0.02, T)
alpha  = 1 - beta
sqrt_alpha = torch.sqrt(alpha)
alpha_bar = torch.cumprod(alpha, dim=0)

sqrt_alpha_bar = torch.sqrt(alpha_bar)
sqrt_one_minus_alpha_bar = torch.sqrt(1 - alpha_bar)

def sinusoidal_embedding(t, dim):
    half = dim // 2
    freqs = torch.exp(
        torch.arange(half) * -(math.log(10000.0) / (half - 1))
    )
    args = t.float()[:, None] * freqs[None, :]
    return torch.cat([torch.sin(args), torch.cos(args)], dim=-1)

class UNet(nn.Module):
    def __init__(self, time_emb_dim=128):
        super().__init__()
        # time embedding projection
        self.time_mlp = nn.Linear(time_emb_dim, time_emb_dim)
        self.time_emb_dim = time_emb_dim
        
        #encoder
        self.enc1 = nn.Conv2d(1,32,kernel_size=3,padding=1)
        self.enc2 = nn.Conv2d(32,64,kernel_size=3,padding=1)
        self.down = nn.MaxPool2d(2)

        #bottleneck
        self.bottleneck = nn.Conv2d(64,128,kernel_size=3,padding=1)

        #decoder
        self.dec1 = nn.Conv2d(128 + 64, 64, kernel_size=3, padding=1)  # 192 in
        self.dec2 = nn.Conv2d(64  + 32, 32, kernel_size=3, padding=1)  # 96 in
        self.up = nn.Upsample(scale_factor=2,mode='nearest')

        #output
        self.out = nn.Conv2d(32,1,kernel_size=1)

    def forward(self, x, t):
        t_emb = sinusoidal_embedding(t, self.time_emb_dim)
        h1 = F.relu(self.enc1(x))    # save
        x  = self.down(h1)
        h2 = F.relu(self.enc2(x))    # save
        x  = self.down(h2)
        x  = F.relu(self.bottleneck(x))
        # ... time embedding injection unchanged ...
        x  = self.up(x)
        x  = torch.cat([x, h2], dim=1)   # concat along channels
        x  = F.relu(self.dec1(x))
        x  = self.up(x)
        x  = torch.cat([x, h1], dim=1)   # concat along channels
        x  = F.relu(self.dec2(x))
        x  = self.out(x)     
        return x

    # --- FUNCTION: computes loss for one batch ---
def training_loss(x0, t, sqrt_alpha_bar, sqrt_one_minus_alpha_bar, model):
        eps = torch.randn_like(x0)
        a = sqrt_alpha_bar[t][:, None, None, None]   # (B,1,1,1)
        b = sqrt_one_minus_alpha_bar[t][:, None, None, None]
        x_t = a * x0 + b * eps
        predicted_eps = model(x_t, t)
        return torch.mean((eps - predicted_eps) ** 2)  # scalar loss


    # --- SETUP: run once before the loop ---
transform = transforms.Compose([
transforms.ToTensor(),
transforms.Normalize((0.5,), (0.5,))   # [0,1] → [-1,1]
])
dataset   = datasets.MNIST('.', train=True, download=True, transform=transform)
dataloader = DataLoader(dataset, batch_size=64, shuffle=True)
model     = UNet(time_emb_dim=128)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)   # fill in


    # --- TRAINING LOOP: separate from the function above ---
for epoch in range(30):
    epoch_loss = 0.0
    for x0, _ in dataloader:
        t = torch.randint(0, T, (x0.shape[0],))
        optimizer.zero_grad()
        loss = training_loss(x0, t, sqrt_alpha_bar, sqrt_one_minus_alpha_bar, model)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        epoch_loss += loss.item()
    print(f"Epoch {epoch}: {epoch_loss / len(dataloader):.4f}")


model.eval()
with torch.no_grad():
    # start from pure noise, shape = (1, 1, 28, 28) — one MNIST image
    x = torch.randn(1, 1, 28, 28)
    timesteps = list(range(T-1, -1, -5))   # 200 steps
    if timesteps[-1] != 0:
        timesteps.append(0)
    
    for t, t_prev in zip(timesteps[:-1], timesteps[1:]):
        t_tensor = torch.tensor([t])
        predicted_eps = model(x, t_tensor)
        x_hat_0 = (x - sqrt_one_minus_alpha_bar[t] * predicted_eps) / sqrt_alpha_bar[t]
        x = sqrt_alpha_bar[t_prev] * x_hat_0 + sqrt_one_minus_alpha_bar[t_prev] * predicted_eps

    # rescale [-1,1] → [0,1] for display
    x = (x.clamp(-1, 1) + 1) / 2
    plt.imshow(x.squeeze().numpy(), cmap='gray')
    plt.title('Generated after 30 epochs')
    plt.axis('off')
    plt.show()

    
