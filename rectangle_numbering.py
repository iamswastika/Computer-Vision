
import cv2


img = cv2.imread("img.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(gray.shape)



ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("Number of contours detected:", len(contours))


def distanceCalculate(p1, p2):
    """p1 and p2 in format (x1,y1) and (x2,y2) tuples"""
    dis = ((p2[0] - p1[0]) * 2 + (p2[1] - p1[1]) * 2) ** 0.5
    return dis

points = []
# length = []
for i ,cnt in enumerate( contours):

    x1,y1 = cnt[0][0]
    print(hierarchy[0][i])
    if all(x == -1 for x in hierarchy[0][i][:3]):
        x, y, w, h = cv2.boundingRect(cnt)
        line_length =  distanceCalculate((x,y), (x+w, y+h))
        print(line_length)
        points.append([line_length,[x, y, w, h]])


        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

print(points)
sorted_points = sorted(points)

for i, pp in enumerate(sorted_points):
    cv2.putText(img, str(i+1), (pp[1][0],pp[1][1]),cv2.FONT_HERSHEY_SIMPLEX,
                2,(225,55,5),1, cv2.LINE_AA)

print(sorted(points))



cv2.imshow("image", img)

cv2.waitKey(0)