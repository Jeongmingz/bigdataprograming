# week12_chap_numpy_01
import numpy as np

mid_scores = np.array([10, 20, 30])
final_scores = np.array([70, 80, 90])

total_scores = mid_scores + final_scores

# print(total_scores)
print(f'시험 성적 합계 : {total_scores}')
print(f'시험 성적 평균 : {total_scores / 2}')


# mid_scores = [10, 20, 30]
# final_scores = [70, 80, 90]
# total_scores = []
# avg_scores = []
# for i in range(len(mid_scores)):
# 	total_scores.append(mid_scores[i]+final_scores[i])
# 	avg_scores.append(total_scores[i]/2)
#
# # average = [total_scores[i] / 2 for i in range(len(mid_scores))]
#
# print(total_scores)
# print(f'시험 성적 합계 : {total_scores}')
# print(f'시험 성적 평균 : {avg_scores}')
