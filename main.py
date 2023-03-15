import os
import cv2
from sklearn.cluster import KMeans
from collections import Counter
import shutil

def get_color(image):
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    clt = KMeans(n_clusters = 1)
    labels = clt.fit_predict(image)
    label_counts = Counter(labels)
    dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]
    return list(dominant_color)

redImg = []

for imageName in os.listdir('images'):
    orig_image = cv2.imread('images/'+imageName)
    edited_image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)
    dom_color = get_color(edited_image)
    red = int(dom_color[0])
    green = int(dom_color[1])
    blue = int(dom_color[2])
    if red > blue and red > green:
        redImg.append(imageName)
if not os.path.exists('redImages'):
    os.makedirs('redImages')
print("Red images:")
for i in redImg:
    print(i)
    shutil.copy('images/'+i, 'redImages')
