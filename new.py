#extract column
cnt=df['cnt']
print(cnt.head(3))


#heatmap
plt.figure(figsize=(10,5))
sns.heatmap(df.corr(),cmap='Blues')
plt.show()

#pairplot
vissual3 = sns.pairplot(df, vars=['registered','cnt'])
plt.show()

#violin
sns.violinplot(x=df["season"], y=df["cnt"], palette="Blues")
plt.show()

sns.violinplot(x=df["mnth"], y=df["casual"], palette="Blues")
plt.show()

#boxplots
vis4= sns.boxplot(data=df, x="season", y="registered", palette='Blues')
plt.show()

vis4= sns.boxplot(data=df, x="mnth", y="registered", palette='Blues')
plt.show()

vis4= sns.boxplot(data=df, x="mnth", y="casual", palette='Blues')
plt.show()

#distplot
vis1 = sns.distplot(df["cnt"])
plt.show()

#implot-scatterdot
vissual2 = sns.lmplot(data=df, x='mnth', y='casual',
                 fit_reg=False)
plt.show()

vissual2 = sns.lmplot(data=df, x='mnth', y='cnt',
                 fit_reg=False)
plt.show()

season = sns.lmplot(data=df, x='season', y='cnt',
                 fit_reg=False)
plt.show()







