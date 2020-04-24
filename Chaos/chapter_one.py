import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1 - x)

def prime_logistic(r, x):
    return r ** (1 - 2**x)

def run_logist(start, N, r):
    res = np.zeros(N)
    res[0] = start
    for i in range(0, N-1):
        res[i+1] = logistic(r, res[i]) 
        if res[i] < 0:
            res[i] = 0;
    return res
## Logistic map and y=x
r = 2
x = np.linspace(0, 1, 100)
plt.plot(x, logistic(r, x), 'k', lw=2)
plt.plot([0, 1], [0, 1])

plt.show()

## Plot logistic map
N = 20
start = 0.5
r = 3.835

res = np.zeros(N)
res[0] = start
for i in range(0, N-1):
    res[i+1] = logistic(r, res[i]) 

plt.plot(res)
plt.show()

## Plot logistic map for a range of r
r_range = np.linspace(0, 5, 10)
print(r_range)
for i in r_range:
    plt.plot(run_logist(0.2, 30, i))
plt.xlabel('Itteration')
plt.ylabel('Population')
plt.show()

## A first look at the biforcation diagram
run = False

if run:
    N1 = 100
    N2 = 100000
    fin = np.zeros(N2)
    r_range = np.linspace(3, 4, N2) 

    j = 0;
    for i in r_range:
        tmp = run_logist(0.3, N1, i)
        fin[j] = tmp[N1-1] 
        j += 1
    plt.xlabel('r-value')
    plt.ylabel('Value of f(N), N >> 0')
    plt.plot(r_range, fin, ',', color='k', alpha=.5)

## Oscillating point with periodicity 2

r = 3.5
x = np.linspace(0, 1, 100)
plt.plot(x, logistic(r, logistic(r, x)), 'k', lw=2)
plt.plot([0, 1], [0, 1])

plt.show()

## Oscillating point with periodicity 2

r = 3.9
x = np.linspace(0, 1, 100)
plt.plot(x, logistic(r, logistic(r, logistic(r, x))), 'k', lw=2)
plt.plot([0, 1], [0, 1])

plt.show()

## Online example of iteration of f(x) and y=x

def plot_system(r, x0, n, ax=None):
    # Plot the function and the
    #     # y=x diagonal line.
    t = np.linspace(0, 1)
    ax.plot(t, logistic(r, t), 'k', lw=2)
    ax.plot([0, 1], [0, 1], 'k', lw=2)

    # Recursively apply y=f(x) and plot two lines:
    #     # (x, x) -> (x, y)
    #         # (x, y) -> (y, y)
    x = x0
    for i in range(n):
                y = logistic(r, x)
                # Plot the two lines.
                ax.plot([x, x], [x, y], 'k', lw=1)
                ax.plot([x, y], [y, y], 'k', lw=1)
                # Plot the positions with increasing opacity.
                ax.plot([x], [y], 'ok', ms=10, alpha=(i + 1) / n)
                x = y

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title(f"$r={r:.1f}, \, x_0={x0:.1f}$")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6),sharey=True)
plot_system(2.5, .1, 10, ax=ax1)
plot_system(3.5, .1, 10, ax=ax2)


## Introduction to Lyapunov exponent
N = 800
x = np.linspace(0, N, N)
start1 = 0.0001
start2 = 0.0001000000001
r = 3.1

res1 = run_logist(start1, N, r)
res2 = run_logist(start2, N, r)
diff = res1 - res2
prime = prime_logistic(r, res1)

plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(311)
plt.plot(x, np.abs(diff))
plt.xlabel('Itteration')
plt.ylabel('Differance')
plt.subplot(312)
plt.plot(res1)
plt.plot(res2)
plt.subplot(313)
plt.plot(abs(prime))
l1 = np.ones(N)
plt.plot(l1)
plt.show()

## Lyapunov single exponent

N = 800
x = np.linspace(0, N, N)
start1 = 0.0001
start2 = 0.00015
r = 3.1

res1 = run_logist(start1, N, r)
res2 = run_logist(start2, N, r)

lyap = 1/N * np.log(np.abs(res1[N-1] - res2[N-1]) / np.abs(start1 - start2))
lyap

## Lyapunov range of exponents

N = 800
x = np.linspace(0, N, N)
start1 = 0.0001
start2 = 0.00010000001
r = 3.8

res1 = run_logist(start1, N, r)
res2 = run_logist(start2, N, r)

lyap = np.zeros(N)
for i in range(N):
    lyap[i] = 1/N * np.log(np.abs(res1[i-1] - res2[i-1]) / np.abs(start1 - start2))

plt.plot(lyap)
plt.show()

## Lyapunov eponents for a range of r's

N = 300
n = 10000
x = np.linspace(0, N, N)
start1 = 0.0001
start2 = 0.00010000001
r = np.linspace(1, 4, n)
fin_lyap = np.zeros(n)

k = 0
for j in r:
    res1 = run_logist(start1, N, j)
    res2 = run_logist(start2, N, j)

    lyap = np.zeros(N)
    for i in range(10):
        lyap[i] = 1/N * np.log(np.abs(res1[N-11+i] - res2[N-11+i]) / np.abs(start1 - start2))
    fin_lyap[k] = np.mean(lyap) 
    k += 1
plt.plot(fin_lyap)
plt.show()

## Online example of bifurcation diagram

n = 10000
r = np.linspace(2.5, 4.0, n)

iterations = 1000
last = 100

x = 1e-5 * np.ones(n)
lyapunov = np.zeros(n)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 9),sharex=True)

for i in range(iterations):
        x = logistic(r, x)
        # We compute the partial sum of the
        #     # Lyapunov exponent.
        lyapunov += np.log(abs(r - 2 * r * x))
        # We display the bifurcation diagram.
        if i >= (iterations - last):
                    ax1.plot(r, x, ',k', alpha=.25)
ax1.set_xlim(2.5, 4)
ax1.set_title("Bifurcation diagram")

# We display the Lyapunov exponent.
# # Horizontal line.
ax2.axhline(0, color='k', lw=.5, alpha=.5)

# Negative Lyapunov exponent.
ax2.plot(r[lyapunov < 0],lyapunov[lyapunov < 0] / iterations,'.k', alpha=.5, ms=.5)

# Positive Lyapunov exponent.
ax2.plot(r[lyapunov >= 0],lyapunov[lyapunov >= 0] / iterations,'.r', alpha=.5, ms=.5)

ax2.set_xlim(2.5, 4)
ax2.set_ylim(-2, 1)
ax2.set_title("Lyapunov exponent")
plt.tight_layout()
    
##
