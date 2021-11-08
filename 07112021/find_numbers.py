import numpy as np

def sum_factors(num):

	factor_list = []

	for possible_factor in range(1, int(np.sqrt(num)) + 1):

		if num%possible_factor == 0 and possible_factor == int(np.sqrt(num)):

			factor_list.append(possible_factor)

		elif num%possible_factor == 0 and possible_factor != int(np.sqrt(num)):

			factor_list.append(possible_factor)
			factor_list.append(num/possible_factor)

	return int(np.sum(factor_list))

def convert_in_to_cm(num):

	return int(round(num * 2.54))

def main():

	MAX_NUM = int(1e7)

	for candidate_num in range(1, MAX_NUM+1):

		if sum_factors(candidate_num) == convert_in_to_cm(candidate_num):
			print(candidate_num)


if __name__=="__main__":
	main()


