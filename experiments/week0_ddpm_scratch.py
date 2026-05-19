from math import sqrt
import torch
import matplotlib.pyplot as plt

T = 1000
beta = torch.linspace(0.0001, 0.02, T)
alpha  = 1 - beta
sqrt_alpha = torch.sqrt(alpha)
alpha_bar = torch.cumprod(alpha, dim=0)

sqrt_alpha_bar = torch.sqrt(alpha_bar)
sqrt_one_minus_alpha_bar = torch.sqrt(1 - alpha_bar)

plt.plot(alpha_bar.numpy(), label='alpha_bar')
plt.xlabel('timestamp t')
plt.ylabel('alpha_bar')
plt.title('Cumulative noise schedule')
plt.legend()
plt.show()

plt.plot(sqrt_alpha_bar.numpy(), label='sqrt_alpha_bar')
plt.xlabel('timestamp t')
plt.ylabel('sqrt_alpha_bar')
plt.title('sqrt_alpha_bar')
plt.legend()
plt.show()

def forward_process(x0, t, sqrt_alpha_bar, sqrt_one_minus_alpha_bar,eps):
    x_t = sqrt_alpha_bar[t] * x0 + sqrt_one_minus_alpha_bar[t] * eps
    return x_t

x0 = torch.randn(3)   # fake "image" — 3 pixels
# t = 500

# xt = forward_process(x0, t, sqrt_alpha_bar, sqrt_one_minus_alpha_bar)

# print(f"x0:  {x0}")
# print(f"xt:  {xt}")
# print(f"ᾱ_t: {alpha_bar[t]:.4f}")

# for t in [50,500,999]:
#     xt = forward_process(x0, t, sqrt_alpha_bar, sqrt_one_minus_alpha_bar)
#     print(f"t={t:4d}, ᾱ_t={alpha_bar[t]:.4f}")

def training_loss(x0, t, sqrt_alpha_bar, sqrt_one_minus_alpha_bar, model):
    eps = torch.randn_like(x0)
    x_t = forward_process(x0, t, sqrt_alpha_bar, sqrt_one_minus_alpha_bar,eps)
    predicted_eps = model(x_t, t) if model is not None else torch.randn_like(x_t)
    loss = torch.mean((eps - predicted_eps) ** 2)
    print (f"MSE: {loss}")  

training_loss(x0, 500, sqrt_alpha_bar, sqrt_one_minus_alpha_bar,model=None)

def reverse_sample(sqrt_alpha,sqrt_one_minus_alpha_bar, beta, alpha, T, shape):
    x_t = torch.randn(shape)
    for t in range(T-1, -1, -1):
        beta_t = 1 - alpha[t]
        sqrt_beta = torch.sqrt(beta[t])
        predicted_eps = torch.randn_like(x_t)
        mu = (1/sqrt_alpha[t]) * (x_t - beta_t/sqrt_one_minus_alpha_bar[t] * predicted_eps)
        if t > 997:   # print first two steps
            print(f"t={t}  mu={mu}  x_t={x_t}")
        if t > 0:
            x_t = mu + sqrt_beta * torch.randn_like(x_t)
        else:
            x_t = mu
    return x_t

x_T = reverse_sample(sqrt_alpha,sqrt_one_minus_alpha_bar, beta, alpha, T, shape=(3,))
print(f"x_T: {x_T}")

def ddim_sample(sqrt_alpha_bar,sqrt_one_minus_alpha_bar, shape,steps = 50):
    x_t = torch.randn(shape)
    timesteps = list(range(T-1, -1, -steps))  # [999, 949, 899, ..., 49, 0] (ish)
    # now pair each t with the next one: (999,949), (949,899), ...
    for t, t_prev in zip(timesteps[:-1], timesteps[1:]):
        predicted_eps = torch.randn_like(x_t)
        x_hat_0 = (x_t - sqrt_one_minus_alpha_bar[t] * predicted_eps) / sqrt_alpha_bar[t]
        x_t_prev = sqrt_alpha_bar[t_prev] * x_hat_0 + sqrt_one_minus_alpha_bar[t_prev] * predicted_eps
        x_t = x_t_prev
    return x_t_prev

x_0 = ddim_sample(sqrt_alpha_bar,sqrt_one_minus_alpha_bar, shape=(3,))
print(f"x_0: {x_0}")

