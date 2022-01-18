#Case Study2

"""
Groups (clusters) similar lines together from a text file with changin string form to TfidfVector
using k-means clustering algorithm and for best parameters silhouette_score used.
Also does some simple cleaning (such as removing white space and replacing numbers with (N)).
"""
import re
import numpy
import random
import pandas
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from matplotlib import pyplot as plt
import csv

with open("hospital.txt", "w") as my_output_file:
    with open("hospital.csv", "r") as my_input_file:
        [my_output_file.write(" ".join(row) + '\n') for row in csv.reader(my_input_file)]
    my_output_file.close()


def k_means_cluster():
    lines = numpy.array(list(get_lines("hospital.txt")))
    doc_feat = TfidfVectorizer().fit_transform(lines)
    range_n_clusters = range(2,60)
    silhouette_avg = []
    for num_clusters in range_n_clusters:
      kmeans = KMeans(n_clusters=num_clusters)
      kmeans.fit(doc_feat)
      cluster_labels = kmeans.labels_
      silhouette_avg.append(silhouette_score(doc_feat, cluster_labels))
    plt.plot(range_n_clusters,silhouette_avg,'bx-')
    cluster=range_n_clusters[silhouette_avg.index(max(silhouette_avg))]

    km = KMeans(cluster).fit(doc_feat)
    k = 0
    clusters = defaultdict(list)
    for i in km.labels_:
        clusters[i].append(lines[k])
        k += 1

    s_clusters = sorted(clusters.values(), key=lambda l: -len(l))

    for cluster in s_clusters:
        print('Cluster [%s]:' % len(cluster))
        if len(cluster) > 10:
            cluster = random.sample(cluster, 10)
        for line in cluster:
            print(line)
        print('--------')


def clean_line(line):
    line = line.strip().lower()
    line = re.sub('\d+', '(N)', line)
    return line


def get_lines(filename):
    for line in open(filename).readlines():
        yield clean_line(line)


if __name__ == '__main__':
    k_means_cluster()
