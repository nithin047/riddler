import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange

fig_dir = './fig/'

max_num = 1e5
angle_array = np.linspace(0, 2*np.pi, 1000)
f_val_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

num_array = np.linspace(0, max_num, int(max_num)+1)

for f_val in f_val_list:

	plt.clf()

	for ii in trange(len(angle_array)):

		angle = angle_array[ii]
		X = np.sum(f_val**num_array * np.cos(num_array*angle))
		Y = np.sum(f_val**num_array * np.sin(num_array*angle))

		# imag_theory = 1/(1 - f_val*(np.cos(angle) + 1j * np.sin(angle)))

		# abs_theory = np.absolute(imag_theory)
		# angle_theory = np.angle(imag_theory)

		# X_theory = abs_theory * np.cos(angle_theory)
		# Y_theory = abs_theory * np.sin(angle_theory)

		plt.plot(X, Y, 'bo')
		# plt.plot(X_theory, Y_theory, 'r+')

		fig = plt.gcf()
		ax = fig.gca()

		# circle1 = plt.Circle((1/(1-f_val**2), 0), (f_val)/(1-f_val**2), color='r')
		# ax.add_patch(circle1)


	plt.title("Riddler Classic Shape, f="+str(f_val))
	plt.savefig("shape_f_"+str(f_val)+".png")