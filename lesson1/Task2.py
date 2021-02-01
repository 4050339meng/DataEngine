
import numpy as np

# 创建numpy的dtype类型
grade_dtype = np.dtype({
    'names': ['name', 'Chinese', 'Math', 'English'],
    'formats': ['S32', 'i', 'i', 'i']
})

# 班里学生的成绩
grade = np.array([
    ('zhangfei', 68, 65, 30),
    ('guanyu', 95, 76, 98),
    ('liubei', 98, 86, 88),
    ('dianwei', 90, 88, 77),
    ('xuchu', 80, 90, 90)], dtype=grade_dtype)

chineses = grade['Chinese']  # 语文成绩一个列表
maths = grade['Math']  # 数学成绩一个列表
englishs = grade['English']  # 英语成绩一个列表

# 求各个科目最大最小成绩索引
index1 = np.argmin(chineses)
index2 = np.argmin(maths)
index3 = np.argmin(englishs)
index4 = np.argmax(chineses)
index5 = np.argmax(maths)
index6 = np.argmax(englishs)

print('平均成绩：')
print('语文：{:.2f}, 数学：{:.2f}, 英语：{:.2f}'.format(np.mean(chineses),
                                               np.mean(maths), np.mean(englishs)))

print('\n最小成绩：')
print('语文：{}, {}'.format(grade[index1]['Chinese'], grade[index1]['name'].decode('utf-8')))
print('数学：{}, {}'.format(grade[index2]['Math'], grade[index2]['name'].decode('utf-8')))
print('英语：{}, {}'.format(grade[index3]['English'], grade[index3]['name'].decode('utf-8')))

print('\n最大成绩：')
print('语文：{}, {}'.format(grade[index4]['Chinese'], grade[index4]['name'].decode('utf-8')))
print('数学：{}, {}'.format(grade[index5]['Math'], grade[index5]['name'].decode('utf-8')))
print('英语：{}, {}'.format(grade[index6]['English'], grade[index6]['name'].decode('utf-8')))

print('\n方差：')
print('语文：{:.2f}, 数学：{:.2f}, 英语：{:.2f}'.format(np.var(chineses),
                                               np.var(maths), np.var(englishs)))

print('\n标准差')
print('语文：{:.2f}, 数学：{:.2f}, 英语：{:.2f}'.format(np.std(chineses),
                                               np.std(maths), np.std(englishs)))

# 创建另外一个字典用于存放每个人的总成绩
total = {}
for i in range(len(grade)):
    total[grade[i][0]] = grade[i][1] + grade[i][2] + grade[i][3]

# 对总成绩排序，名字也随之排序
total = sorted(total.items(), key=lambda x: x[1], reverse=True)

print('\n总成绩排序：')
for i in range(len(total)):
    print("第{}名： {}\t总成绩： {}".format(i + 1, total[i][0].decode('utf-8'), total[i][1]))
