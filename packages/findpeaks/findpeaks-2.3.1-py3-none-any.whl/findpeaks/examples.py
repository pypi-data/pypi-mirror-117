# %%
# import os
# os.chdir(os.path.dirname(os.path.abspath('examples.py')))
# import findpeaks
# print(dir(findpeaks))
# print(findpeaks.__version__)

# %%
from findpeaks import findpeaks
import cv2
x = cv2.imread('C://temp/LbK2I.png')
x = cv2.imread('C://temp/uISO2.png')


fp = findpeaks(method="topology", whitelist=['peak', 'valley'], denoise=None, limit=0, verbose=3)
results = fp.fit(x)

results['persistence']
fp.plot(cmap='coolwarm')
fp.plot_persistence()
fp.plot_mesh(view=(90,0))


# %% find peak and valleys in 2d images.
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from findpeaks import findpeaks
rng = np.random.default_rng(42)
x = rng.normal(size=(50, 50))
x = gaussian_filter(x, sigma=10.)

fp = findpeaks(method="topology", whitelist=['peak', 'valley'], denoise=None, verbose=3)
results = fp.fit(x)

results['persistence']
fp.plot(cmap='coolwarm')
fp.plot_persistence()
fp.plot_mesh()

# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from findpeaks import findpeaks
rng = np.random.default_rng(42)

x = rng.normal(size=(50, 50))
x = gaussian_filter(x, sigma=10.)


fp = findpeaks(method="topology", denoise=None, limit=0, verbose=3)
results = fp.fit(x)

results['persistence']
fp.plot(cmap='coolwarm')

# Plot
plt.imshow(x, cmap="coolwarm", interpolation="none", vmin=0, vmax=255)

fp.plot(cmap='coolwarm')
fp.plot_persistence()
fp.plot_mesh()


plt.imshow(x, cmap="coolwarm", interpolation="none", vmin=0, vmax=255)
plt.imshow(fp.results['Xdetect'], cmap='gray_r')
results["persistence"]


results.keys()
results['persistence']
results['Xdetect']

# %%
from findpeaks import findpeaks
fp = findpeaks()
# Import example
X = fp.import_example("btc")

# Make fit
fp = findpeaks(method="topology")
results = fp.fit(X)
fp.plot()
fp.plot_persistence()

fp = findpeaks(method="peakdetect", lookahead=15)
# Make fit
results = fp.fit(X)
fp.plot()

fp = findpeaks(method="caerus", params={'minperc':100}, interpolate = None)
# Make fit
results = fp.fit(X)
ax = fp.plot()


# %%
from findpeaks import findpeaks
import numpy as np

# np.random.seed(100)
np.random.seed(200)
X = np.random.randint(200, size=400)

fp = findpeaks(method = 'topology', interpolate = 10, lookahead = 1)
results = fp.fit(X)

fig=fp.plot()
fp.plot_mesh()

# %%
from findpeaks import findpeaks
fp = findpeaks(method="topology", verbose=0)
X = fp.import_example("2dpeaks")
results = fp.fit(X)
fp.plot()

# %%
# Load library
from findpeaks import findpeaks
# Data
X = [10,11,9,23,21,11,45,20,11,12]
# Initialize
fp = findpeaks(method='peakdetect', lookahead=1)
results = fp.fit(X)
# Plot
fig=fp.plot()

# %%
# Import library
from findpeaks import findpeaks
# Import image example
img = fp.import_example('2dpeaks_image')
# Initializatie
fp = findpeaks(scale=True, denoise='fastnl', window=31, togray=True, imsize=(300,300), whitelist=['peak', 'valley'])
# Fit
fp.fit(img)
fp.plot()
fp.results["persistence"]

# Take the minimum score for the top peaks off the diagonal.
limit = fp.results['persistence'][0:5]['score'].min()
fp = findpeaks(scale=True, denoise='fastnl', window=31, togray=True, imsize=(300,300), limit=254, whitelist=['peak', 'valley'])
fp.fit(img)

fp.results["persistence"]
fp.plot(text=True)

# Plot
fp.plot_mesh()
# Rotate to make a top view
fp.plot_mesh(view=(90,0))

# %%
from findpeaks import findpeaks
fp = findpeaks(method="topology", denoise=None, window=3, limit=None)
X = fp.import_example("2dpeaks_image")
# X = fp.import_example("2dpeaks")
results = fp.fit(X)

fp.plot_persistence()

results["persistence"]

fp.plot()
fp.plot_persistence()
fp.plot_mesh()


fp = findpeaks(method="mask")
X = fp.import_example()
results = fp.fit(X)

fp.plot()
fp.plot_preprocessing()
fp.plot_persistence()
fp.plot_mesh()

# %%
from findpeaks import findpeaks
# X = fp.import_example('1dpeaks')
X = [10,11,9,23,21,11,45,20,11,12]
methods = ['topology', 'peakdetect', None]
interpolates = [None, 1, 10, 1000]
lookaheads =[None, 0, 1, 10, 100]

for method in methods:
    for interpolate in interpolates:
        for lookahead in lookaheads:
            fp = findpeaks(lookahead=lookahead, interpolate=interpolate, method=method)
            results = fp.fit(X)
            # fp.plot()
            # fp.plot_persistence()

# fp.results['df_interp']
fp.results['df']

# %%
from findpeaks import findpeaks
X = [10,11,9,23,21,11,45,20,11,12]
fp = findpeaks(lookahead=1, method="topology")
results = fp.fit(X)
fp.plot()
fp.plot_persistence()


# %% Run over all methods and many parameters
from findpeaks import findpeaks
savepath='./comparison_methods/'
methods = ['mask','topology', None]
filters = ['fastnl','bilateral','frost','median','mean', None]
windows = [3, 9, 15, 31, 63]
cus = [0.25, 0.5, 0.75]

for getfilter in filters:
    for window in windows:
            fp = findpeaks(method='topology', scale=True, denoise=getfilter, window=window, togray=True, imsize=(300,300), verbose=3)
            img = fp.import_example('2dpeaks_image')
            results = fp.fit(img)
            title = 'Method=' + str(getfilter) + ', window='+str(window)
            _, ax1 = fp.plot_mesh(wireframe=False, title=title, savepath=savepath+title+'.png')

filters = ['lee','lee_enhanced','kuan']
for getfilter in filters:
    for window in windows:
        for cu in cus:
            fp = findpeaks(method='topology', scale=True, denoise=getfilter, window=window, cu=cu, togray=True, imsize=(300,300), verbose=3)
            img = fp.import_example('2dpeaks_image')
            results = fp.fit(img)
            title = 'Method=' + str(getfilter) + ', window='+str(window) + ', cu='+str(cu)
            _, ax1 = fp.plot_mesh(wireframe=False, title=title, savepath=savepath+title+'.png')


#%% Plot each seperately
fp.plot_preprocessing()
fp.plot()
fp.plot_persistence()
fp.plot_mesh()

# Make mesh plot
fp.plot_mesh(view=(0,90))
fp.plot_mesh(view=(90,0))


# %%
from findpeaks import findpeaks

fp = findpeaks(method='peakdetect', lookahead=1, interpolate=10, verbose=3)
X = fp.import_example('1dpeaks')
fp.fit(X)
fp.plot()
fp.plot_persistence()


from findpeaks import findpeaks
fp = findpeaks(method='topology')
X = fp.import_example('1dpeaks')
fp.fit(X)
fp.plot()
fp.plot_persistence()

from findpeaks import findpeaks
fp = findpeaks(method='topology',  interpolate=10)
X = fp.import_example('1dpeaks')
fp.fit(X)
fp.plot()
fp.plot_persistence()


from tabulate import tabulate
print(tabulate(fp.results['df'], tablefmt="grid", headers="keys"))
print(tabulate(fp.results['persistence'], tablefmt="grid", headers="keys"))
print(tabulate(fp.results['df_interp'].head(), tablefmt="grid", headers="keys"))

print(tabulate(fp.results['persistence'][0:10], tablefmt="grid", headers="keys"))


# %%
from findpeaks import findpeaks

# 2dpeaks example
fp = findpeaks(method='topology')
img = fp.import_example('2dpeaks')
fp.fit(img)
fp.plot(cmap='hot')
fp.plot()
fp.plot_persistence()

fp = findpeaks(method='mask')
img = fp.import_example()
fp.fit(img)
fp.plot()


# 2dpeaks example with other settings
fp = findpeaks(method='topology', scale=True, denoise='fastnl', window=31, togray=True, imsize=(300,300), verbose=3)
img = fp.import_example('2dpeaks')
fp.fit(img)
fp.plot()

# %%
from findpeaks import findpeaks
fp = findpeaks(method='topology')
X = fp.import_example('1dpeaks')
fp.fit(X)
fp.plot()

fp.plot_preprocessing()
fp.plot_mesh()
fp.plot_persistence()

# %%
from findpeaks import findpeaks
X = [1,1,1.1,1,0.9,1,1,1.1,1,0.9,1,1.1,1,1,0.9,1,1,1.1,1,1,1,1,1.1,0.9,1,1.1,1,1,0.9,1,1.1,1,1,1.1,1,0.8,0.9,1,1.2,0.9,1,1,1.1,1.2,1,1.5,1,3,2,5,3,2,1,1,1,0.9,1,1,3,2.6,4,3,3.2,2,1,1,0.8,4,4,2,2.5,1,1,1]

fp = findpeaks(method='peakdetect', lookahead=1, verbose=3)
results = fp.fit(X)
fp.plot()
fp.plot_persistence()

fp = findpeaks(method='topology')
results=fp.fit(X)
fp.plot()
fp.plot_persistence()

# %%
X = [10,11,9,23,21,11,45,20,11,12]
fp = findpeaks(method='peakdetect', lookahead=1, interpolate=10)
fp.fit(X)
fp.plot()

fp = findpeaks(method='topology', lookahead=1, interpolate=10)
fp.fit(X)
fp.plot()
fp.plot_persistence()

# %%
from math import pi
import numpy as np
from findpeaks import findpeaks

i = 10000
xs = np.linspace(0,3.7*pi,i)
X = (0.3*np.sin(xs) + np.sin(1.3 * xs) + 0.9 * np.sin(4.2 * xs) + 0.06 * np.random.randn(i))

# Findpeaks
fp = findpeaks(method='peakdetect')
results=fp.fit(X)
fp.plot()

fp = findpeaks(method='topology')
results=fp.fit(X)

fp.plot_persistence()
# fp.results['Xdetect']>1

# %% Denoising example
from findpeaks import findpeaks
fp = findpeaks()


img = fp.import_example('2dpeaks_image')
import findpeaks

# filters parameters
# window size
winsize = 15
# damping factor for frost
k_value1 = 2.0
# damping factor for lee enhanced
k_value2 = 1.0
# coefficient of variation of noise
cu_value = 0.25
# coefficient of variation for lee enhanced of noise
cu_lee_enhanced = 0.523
# max coefficient of variation for lee enhanced
cmax_value = 1.73

# Some pre-processing
# Resize
img = findpeaks.stats.resize(img, size=(300,300))
# Make grey image
img = findpeaks.stats.togray(img)
# Scale between [0-255]
img = findpeaks.stats.scale(img)

# Denoising
# fastnl
img_fastnl = findpeaks.stats.denoise(img.copy(), method='fastnl', window=winsize)
# bilateral
img_bilateral = findpeaks.stats.denoise(img.copy(), method='bilateral', window=winsize)
# frost filter
image_frost = findpeaks.frost_filter(img.copy(), damping_factor=k_value1, win_size=winsize)
# kuan filter
image_kuan = findpeaks.kuan_filter(img.copy(), win_size=winsize, cu=cu_value)
# lee filter
image_lee = findpeaks.lee_filter(img.copy(), win_size=winsize, cu=cu_value)
# lee enhanced filter
image_lee_enhanced = findpeaks.lee_enhanced_filter(img.copy(), win_size=winsize, k=k_value2, cu=cu_lee_enhanced, cmax=cmax_value)
# mean filter
image_mean = findpeaks.mean_filter(img.copy(), win_size=winsize)
# median filter
image_median = findpeaks.median_filter(img.copy(), win_size=winsize)

# Plotting
import matplotlib.pyplot as plt
plt.figure(); plt.imshow(img_fastnl, cmap='gray'); plt.title('Fastnl'); plt.grid(False)
plt.figure(); plt.imshow(img_bilateral, cmap='gray'); plt.title('Bilateral')
plt.figure(); plt.imshow(image_frost, cmap='gray'); plt.title('Frost')
plt.figure(); plt.imshow(image_kuan, cmap='gray'); plt.title('Kuan')
plt.figure(); plt.imshow(image_lee, cmap='gray'); plt.title('Lee')
plt.figure(); plt.imshow(image_lee_enhanced, cmap='gray'); plt.title('Lee Enhanced')
plt.figure(); plt.imshow(image_mean, cmap='gray'); plt.title('Mean')
plt.figure(); plt.imshow(image_median, cmap='gray'); plt.title('Median')


from findpeaks import findpeaks
fp = findpeaks(method='topology', scale=False, denoise='fastnl', togray=True, imsize=False, verbose=3)
fp.fit(img)
fp.plot_persistence()
fp.plot_mesh(wireframe=False, title='image_lee_enhanced', view=(30,30))

# %%