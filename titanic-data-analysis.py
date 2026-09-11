import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df =pd.read_csv("titanic/train.csv")
#读取数据
print(df.head())
#打印数据的前五行

df=df.drop('Cabin',axis=1)
#删除点Cabin这一列

df['Age'] = df['Age'].fillna(df['Age'].median())
#用中位数来填充缺失的年龄

df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
#用众数来替代登船港口

df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
#用0代替男性，1代替女性

sex_counts = df['Sex'].value_counts()
#男性和女性分别的人数
sex_rate = df.groupby('Sex')['Survived'].mean()
#生存率

print("整体存活率：" + str(df['Survived'].mean()))
print("平均年龄：" + str(df['Age'].mean()))
print("男性人数%d,女性人数%d" % (sex_counts.get(0, 0), sex_counts.get(1, 0)))
print("男性存活率：%.4f, 女性存活率：%.4f" % (sex_rate.get(0, np.nan), sex_rate.get(1, np.nan)))

# 性别生存率柱状图
labels_sex = ['Male', 'Female']
survival_rates = [sex_rate.get(0, np.nan), sex_rate.get(1, np.nan)]

plt.figure(figsize=(6, 4))
plt.bar(labels_sex, survival_rates, color=['#4C72B0', '#55A868'])
plt.title('Survival rate by gender')
plt.xlabel('Gender')
plt.ylabel('Survival rate')
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig('fig1_survival_by_sex.png', dpi=300, bbox_inches='tight')
plt.show()


# 船舱生存率柱状图
class_rate = df.groupby('Pclass')['Survived'].mean()
plt.figure(figsize=(6, 4))
plt.bar(class_rate.index.astype(str), class_rate.values, color=['#4C72B0', '#55A868', '#C44E52'])
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig('fig1_survival_by_Pclass.png', dpi=300, bbox_inches='tight')
plt.show()


# 年龄分布直方图
plt.figure(figsize=(8, 5))
plt.hist(df['Age'], bins=20, color='steelblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('fig3_age_distribution.png', dpi=300, bbox_inches='tight')
plt.show()


