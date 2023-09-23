
from matplotlib import pyplot as plt

movies = ["Titanic","Vingadores","Avatar 2"]
num_oscar =[3,7,4]

xs = 9
plt.bar(movies,num_oscar)
plt.ylabel("#premiacao")
plt.title("teste basico")

plt.savefig("./img/Example.png")