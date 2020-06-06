import matplotlib.pyplot as plt


def Show_Riffle_Order(placemenetOrder):
	'''
	Plots the order in which the Riffle Shuffle is performed.
	'''
	nleft = sum(placemenetOrder==0)
	nright = sum(placemenetOrder==1)

	print('# Cards in left: ', nleft)
	print('# Cards in right: ', nright)
	print(placemenetOrder)
	return
	fig, ax = plt.subplots()
	plt.axis([-0.2, 1.2, 0.5, 52.5])
	ax.set_xticks([0, 1])
	ax.set_xticklabels(['Left Half\n' + str(nleft), 'Right Half\n' + str(nright)])
	ax.set_ylabel('Number of Cards Put Down')
	ax.set_title('Riffle Shuffle Distribution')
	ax.plot(placemenetOrder[0], 1, 'b.')

	for i in range(1, len(placemenetOrder)):
		ax.plot(placemenetOrder[i], i + 1, 'b.')
		ax.plot(placemenetOrder[i - 1:i + 1], [i, i + 1], 'g')
		plt.pause(0.0001)
	plt.show()
	return
