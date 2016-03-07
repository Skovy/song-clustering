
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter

from sklearn.decomposition import TruncatedSVD

fig = plt.figure(figsize=(15, 8))

JankData = [
['We Found Love - R3hab\'s XS Remix Edit'                                    ,  -2.34400000 , 0.52289402 , 0.85964239 , 0.05253588 , 0.62323999 , 0.00075855 , 0.00000470],
['Chandelier - Cutmore Club Remix'                                          ,  -6.18900000 , 0.66231423 , 0.68070183 , 0.03318303 , 0.08295735 , 0.00886432 , 0.00222396],
['GDFR (feat. Sage The Gemini & Lookas) - DJ Kay Rich x Up 2 No Good Remix' ,  -9.73500000 , 0.81373358 , 0.61748181 , 0.31661403 , 0.07314939 , 0.06984857 , 0.00001560],
['Ophelia'                                                                  ,  -6.51900000 , 0.66443445 , 0.57255708 , 0.02770619 , 0.08571186 , 0.61282370 , 0.00036333],
['Old Guitar'                                                               ,  -4.85900000 , 0.48559420 , 0.85359331 , 0.05687508 , 0.35790372 , 0.07387639 , 0.00001072],
['I Believe - Feat. Jacob Hemphill'                                         ,  -8.37700000 , 0.78881205 , 0.52622172 , 0.03982867 , 0.04396955 , 0.23075202 , 0.00000516],
['Nothing\'s Over'                                                           ,  -5.91300000 , 0.71794512 , 0.64598582 , 0.04107067 , 0.11055113 , 0.17783351 , 0.00000199],
['Maybe I\'m Sorry'                                                          ,  -9.31900000 , 0.69429592 , 0.55472453 , 0.04271141 , 0.07825231 , 0.01624545 , 0.00006609],
['Old No. 7'                                                                ,  -9.22100000 , 0.56127189 , 0.59671445 , 0.04641746 , 0.10734099 , 0.00008291 , 0.00003469],
['Wake N Bake'                                                              ,  -5.96800000 , 0.61211471 , 0.70383511 , 0.05348533 , 0.11339224 , 0.05117640 , 0.00062832],
['Bright - Lost Kings Remix'                                                ,  -5.30500000 , 0.70080191 , 0.71819461 , 0.03626629 , 0.10156459 , 0.23511439 , 0.00007146],
['Something Better'                                                         ,  -2.56300000 , 0.56143744 , 0.83724834 , 0.06614892 , 0.25350143 , 0.06160062 , 0.00000000],
['Pharaohs'                                                                 ,  -3.20000000 , 0.58497941 , 0.85851692 , 0.19635139 , 0.09495735 , 0.09765619 , 0.00000004],
['Doses and Mimosas'                                                        , -11.01600000 , 0.76917744 , 0.41309236 , 0.06253378 , 0.04919885 , 0.02381421 , 0.00963504],
['How Hard I Try'                                                           ,  -8.76100000 , 0.74254874 , 0.56357213 , 0.04498707 , 0.10918423 , 0.29932801 , 0.00069304],
['Hold My Hand - Feenixpawl Remix'                                          ,  -2.73400000 , 0.54611053 , 0.92662505 , 0.05350162 , 0.34786754 , 0.00596934 , 0.00000028],
['High You Are - Branchez Remix'                                            ,  -5.61300000 , 0.68992772 , 0.85653613 , 0.04052687 , 0.03406145 , 0.05568508 , 0.11038063],
['Till the Next One Comes'                                                  ,  -7.45700000 , 0.76488373 , 0.54182473 , 0.03584791 , 0.11324668 , 0.02540628 , 0.00000014],
['Roses - Loosid Remix'                                                     ,  -8.26600000 , 0.58672567 , 0.62662020 , 0.03463724 , 0.11775090 , 0.02883036 , 0.01251627],
['The Funeral - Excision Remix'                                             ,  -5.36100000 , 0.40328191 , 0.50541222 , 0.02890959 , 0.08481236 , 0.02993107 , 0.00054740]
]

c = []
for num in range(1, 21):
    c.append(num / 20)

color = np.array(c)

ActualJankData = []
for song in JankData:
    ActualJankData.append(song[1:])

# X = [[-1.0, -1.0, -1.0], [2.0, 2.0, 2.0], [2.0, 2.0, -1.0]]
X = ActualJankData
print X

svd = TruncatedSVD(n_components=2, random_state=42)

Y = svd.fit_transform(X)

print Y

TruncatedSVD(algorithm='randomized', n_components=2, n_iter=5,
        random_state=42, tol=0.0)

print(svd.explained_variance_ratio_)

print(svd.explained_variance_ratio_.sum())


plt.scatter(Y[:, 0], Y[:, 1], c=color, cmap=plt.cm.Spectral)
ax = fig.add_subplot(258)
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')
plt.show()
