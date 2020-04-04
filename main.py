import matplotlib.pyplot as plt
import numpy as np


def bifurcation(r0: float = -2, step: float = 0.01, rmax: float = 4, backtrack: int = 10):
    rs = []
    ys = []
    for r in np.arange(r0, rmax, step):
        rs += [r] * backtrack
        yl = logistic_map(r=r)
        ys += [yl[-i] for i in range(1, backtrack + 1)]
    plot(x=rs, y=ys,
         title='bifurcation diagram\n\nx_t+1(x_t) = r*x_t*(1 - x_t)',  xlab='r', ylab='lim_n->inf(x_t)')


def logistic_map(y0: float = 0.1, r: float = 2, lim: int = 1000):
    y = [y0]
    for i in range(lim):
        y.append(r*y[-1]*(1 - y[-1]))
    return y[:-1]


def plot(y, x=None, title: str = None, xlab: str = None, ylab: str = None):
    if x is None:
        x = []
    fig, ax = plt.subplots()
    if not x:
        x = [i for i in range(len(y))]
    ax.plot(x, y, '.')

    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.show()


def main():
    bifurcation(step=0.001)


if __name__ == '__main__':

    main()
