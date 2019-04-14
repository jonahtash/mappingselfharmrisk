import twint

c = twint.Config()

c = twint.Config()

for i in range (1,5):
    c.Near = "USA"
    c.Lang = "en"
    c.Location = True
    c.Store_csv = True
    c.Since = "2019-04-13"
    c.Output = "twitter2.csv"
twint.run.Search(c)

