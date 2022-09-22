import random
folder_name = [
		"00Uncorrelated",
		"01WeaklyCorrelated",
		"02StronglyCorrelated",
		"03InverseStronglyCorrelated",
		"04AlmostStronglyCorrelated",
		"05SubsetSum",
		"06UncorrelatedWithSimilarWeights",
		"07SpannerUncorrelated",
		"08SpannerWeaklyCorrelated",
		"09SpannerStronglyCorrelated",
		"10MultipleStronglyCorrelated",
		"11ProfitCeiling",
		"12Circle"
	]

folder_name_2 = [
		"n00050",
		"n00100",
		"n00200",
		"n00500",
		"n01000",
		"n02000",
		"n05000",
		"n10000"
	]

for name in folder_name:
    for name_2 in folder_name_2:
        rand = random.randint(0, 1)
        if rand >= 0.5:
            print("data/" + name + "/" + name_2 + "/R01000/s0" + str(random.randint(10, 100)), end = '')
        else:
            print("data/" + name + "/" + name_2 + "/R10000/s0" + str(random.randint(10, 100)), end = '')
        print('",')