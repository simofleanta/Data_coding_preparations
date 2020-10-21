    """df['hr'] = df['hr'].astype('category')
    df['weathersit'].value_counts(normalize=True)

    p=pd.crosstab(df.weathersit, df.season)
    print(p)



df.loc[:,'temp':'windspeed'].plot(subplots=True)
plt.xlabel("")
plt.tight_layout()
plt.show()

df.cnt.plot(title = "Count of total rental bikes per day")
plt.xlabel("")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

dfs=df[['casual','registered','cnt']].describe()


c=df[df.cnt == df.cnt.min()]
print(c)
d=df[df.cnt == df.cnt.max()]
print(d)

e=df.groupby('weathersit')['cnt'].mean()
print(e)

ef=df.groupby(['workingday','weathersit'])['cnt'].mean()
print(ef)"""