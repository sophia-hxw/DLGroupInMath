#HSV H(色彩/色度)[0,179] S(饱和度)[0,255] V(亮度)[0,255]
#白色[255,255,255] 黑色[0,0,0]

#绘制直线：
cv.line(img,start,end,color,thickness) #color: BGR
#绘制圆形：
cv.circle(img,centerpoint, r, color, thickness) #thickness为-1时，生成闭合图案并填充颜色
#绘制矩形：
cv.rectangle(img,leftupper,rightdown,color,thickness)#leftupper,rightdown:矩形的左上角和右下角坐标
#向图像中添加文字：
cv.putText(img,text,station, font, fontsize,color,thickness,cv.LINE_AA)
#font字体 fontsize字体大小
#创建一个空白图像
img = np.zeros((512,512,3),np.uint8)  #512*512的像素 3个波段 数据类型np.uint8
plt.imshow(img[:,:,::-1])

#获取并修改图像中的像素点
#获取某个像素点的值
px = img[100,100]
#仅获取蓝色通道的强度值
blue = img[100,100,0]
#修改某个位置的像素值
img[100,100] = [255,255,255]

#获取图像的属性
#形状 img.shape 图像大小 img.size 数据类型 img.dtype

#图像通道的拆分与合并
#通道拆分 b,g,r = cv.split(img)  通道合并 img = cv.merge(b,g,r)

#色彩空间的改变
cv.cvtColor(input_img, flag)
#input_img:进行转换的图像 flag：转换类型 cv.COLOR_BGR2GRAY cv.COLOR_BGR2HSV

#图像的加法
img3 = cv.add(img1,img2)
#图像的混合
img3 = cv.addWeighted(img1,0.7,img2,0.3,0) #0.7,0.3权重，0 常数，可以为0，也可以为其他数值
#图像缩放
cv.resize(src,dsize,fx=0,fy=0,interpolation=cv2.INTER_LINEAR)
#src：输入图像，dsize:(2*cols,2*rows),行和列扩大两倍，绝对尺寸、调整后的图像大小，fx,fy：相对尺寸，将dsize设置为None,然后将fx,fy设置为比例因子即可
#在resize之前，rows,cols = img.shape[:2]
#interpolation:插值方法
#cv2.INTER_LINEAR 双线性插值法
#cv2.INTER_NEAREST 最近邻插值
#cv2.INTER_AREA 像素区域重采样(默认)
#cv2.INTER_CUBIC 双三次插值

#图像平移
cv.warpAffine(img,M,dsize)
#M:2*3移动矩阵 设置为np.float32类型的Numpy数组 dsize：输出图像的大小，(宽，高)
M = np.float32([[1,0,100],[0,1,50]])#平移矩阵 向x轴平移100，向y轴平移50

#图像旋转
M = cv2.getRotationMatrix2D(center,angle,scale)# M旋转矩阵：旋转中心，旋转角度，缩放比例
#旋转变换
img2 = cv2.warpAffine(img,M,(cols,rows))

#图像的仿射变换
 #创建变换矩阵
pts1 = np.float32([50,50],[200,50],[50,200]) #原始图像三个点
pts2 = np.float32([100,100],[200,50],[100,250]) #仿射之后这三个点的位置
M = cv.getAffineTransform(pts1,pts2)
#完成仿射变换
dst = cv.warpAffine(img,M,(cols,rows))

#图像的透射变换
 #创建变换矩阵
pts1 = np.float32([56,65],[368,52],[28,387],[389,390]) #原始图像四个点 任意三个不共线
pts2 = np.float32([100,145],[300,100],[80,290],[310,300]) #透射之后这四个点的位置
T = cv.getPerspectiveTransform(pts1,pts2)
#进行变换
dst = cv.warpPerspective(img,T,(cols,rows))

#图像金字塔  使图像叠加出金字塔形状
img1 = cv.pyrUp(img) #上采样
img2 = cv.pyrDown(img) #下采样

#腐蚀
cv.erode(img,kernel,iterations) #图像，核结构，腐蚀的次数、默认为1
 #创建核结构 5*5的卷积核
 kernel = np.ones((5,5),np.uint8)
#膨胀
cv.dilate(img,kernel,iterations)

#开运算 先腐蚀后膨胀 cv.MORPH_OPEN 消除噪点，去除小的干扰块
#闭运算 先膨胀后腐蚀 cv.MORPH_CLOSE 消除,闭合孔洞，填充闭合区域
cv.morphologyEx(img,op,kernel) #op:处理方式

#礼帽运算 进行背景提取 cv.MORPH_TOPHAT 显示比较亮的点
#闭帽运算 cv.MORPH_BLACKHAT 显示比较暗的点
cv.morphologyEx(img,op,kernel)

# 均值滤波 缺:将图像变得更模糊
cv.blur(src,ksize,anchor,boderType)
#输入图像，卷积核的大小，默认值(-1,-1)、表示核中心，边界类型
#高斯滤波
cv.GaussianBlur(src,ksize,sigmaX,sigmay,boderType)
#输入图像，卷积核大小：都应为奇数且可以不同，水平方向的标准差，垂直方向的标准差：默认值为0 与sigmaX值相同，填充边界类型
#中值滤波
cv.medianBlur(src,ksize)

#直方图  数字图像中亮度分布的直方图 较亮的话直方图靠右 根据灰度图进行绘制
#dims:需要统计的特征数目 dims=1，仅仅统计了灰度值
#bins:每个特征空间子区段的数目，即组距
#range:要统计特征的取值范围 例如：[0,255]
cv2.calcHist(images,channels,mask,histSize,ranges[,hist[,accumulate]])
#images:原图像 [] 加中括号
#channels:如果是灰度图就是[0] 如果是彩色图[0] [1] [2] 分别对应B G R
#mask：掩模图像 统计整幅图就设置为None
#histSize:BIN的数目 [256]
#ranges:像素值范围 通常为[0,256]

#mask掩膜:对图像区域进行遮挡 由0和1组成一个二进制图像，1值的区域被处理，0值区域被屏蔽
 #创建蒙版
mask = np.zeros(img.shape[:2],np.uint8)
mask[400:650,200:250] = 1 #感兴趣区域
masked_img = cv.bitwise_and(img,img,mask=mask)  #掩膜后的图像

#直方图均衡化：把原始的灰度直方图从比较集中的某个灰度区间变成在更广泛灰度范围内的分布 X光图像中使用广泛
dst = cv.equalizeHist(img) (灰度图像)

#自适应的直方图均衡化
clache = cv.createCLAHE(clipLimit,tileGridSize) #对比度限制，默认是40， 分块的大小，默认是8*8
cl1 = clache.apply(img) #应用在图像上

#Sobel算子检测边缘图像
Scale_abs = cv2.convertScaleAbs(x) #格式转换函数
result = cv2.addWeighted(scr1,alpha,scl2,beta) #图像混合
  #计算sobel卷积结果
x = cv.Sobel(img,cv.CV_165,1,0)
y = cv.Sobel(img,cv.CV_165,0,1)
  #将数据进行转换
Scale_absX = cv.convertScaleAbs(x) #convert 转换 scale 缩放
Scale_absY = cv.convertScaleAbs(y)
#结果合成
result = cv.addWeighted(Sclae_absX,0.5,Scale_absY,0.5,0)
#Scharr算子进行边缘检测 将sobel算子的部分在将ksize设为-1
x = cv.Sobel(img,cv.CV_165,1,0,ksize=-1)
y = cv.Sobel(img,cv.CV_165,0,1,ksize=-1)

#Laplacian算子进行边缘检测
laplacian = cv2.Laplacian(src,ddepth[,dst[,ksize[,scale[,delta[,borderType]]]]])
#src:需要处理的图像 ddepth：图像的深度 -1表示采用的使原图像相同的深度，目标图像深度必须大于等于原图像深度
#ksize：算子的大小，即卷积核的大小，必须为1，3，5，7
result = cv2.Laplacian(img,cv.CV_165)
Scale_abs = cv.convertScaleAbs(result)

#Canny边缘检测
canny = cv2.Canny(img,threshold1,threshold2) #灰度图，较小的阈值将间断的边缘连接起来，较大的阈值检测图像中明显的边缘
lowThreshold = 0
max_lowThreshold = 100
canny = cv2.Canny(img,lowThreshold,max_lowThreshold)

#模板匹配
res = cv.matchTemplate(img,template,method) #template:模板图片
#method方法 平方差匹配 CV_TM_SQDIFF 相关匹配 CV_TM_CCORR (最大位置为最佳匹配位置)相关系数匹配 CV_TM_CCOEFF(最小位置为最佳匹配位置)
h,w,l = template.shape
res = cv.matchTemplate(img,template,CV_TM_CCORR)
min_val,max_val,min_loc,max_loc = cv.minMaxLoc(res) #最小值，最大值，最小值的位置，最大值的位置
top_left = max_loc #左上角的坐标为最大位置
bottom_right = (top_left[0]+w,top_left[1]+h) #右下角位置
cv.rectangle(img,top_left,bottom_right,(0,255,0),2)

#霍夫线变换：提取直线
cv.HoughLines(img,rho,theta,threshold)
#二值化图像 进行二值化或进行Canny边缘检测
#rho，theta：精确度  0.8 np.pi/180
#阈值 只有累加器中的值高于该阈值时才被认为是直线 例如 150
   #将检测的线绘制在图像上(极坐标)
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0+1000*(-b))
    y1 = int(x0 + 1000 * (a))
    x2 = int(y0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv.line(img,(x1,y1),(x2,y2),(0,255,0)) #线的起点和终点

#霍夫圆变换：提取圆
circles = cv.HoughCircles(image,CV_HOUGH_GRADIENT,dp,minDist,param1=100,param2=30,miRadius=0,maxRadius=100)
#image：灰度图像  dp:霍夫空间的分辨率 1：霍夫空间与输入图像的大小一致 2：使输入图像的一半
#minDist:圆心之间的最小距离  若两个圆心距离小于该值，则为一个圆
#param1：边缘检测使使用Canny算子的高阈值，低阈值时高阈值的一半  param2：检测圆心和确定半径时所共有的阈值
#minRadius:检测到的圆半径的最小值
    #霍夫圆检测对噪声比较敏感，首先进行中值滤波
img = cv.medianBlur(img,7)  #去噪点
#将检测结果绘制在图像上
for i in circles[0,:] #遍历矩阵每一行的数据
    #绘制图形
    cv.circles(img,(i[0],i[1]),i[2],(0,255,0),2)
    #绘制圆心
    cv.circle(img,(i[0],i[1],2,(0,0,255),3)
break
#Hariis角点检测：
dst = cv2.cornerHarris(src,blockSize,ksize,k)
  #图像（必须是float32的图像），角点检测中要考虑的邻域大小，sobel求导使用的核大小，角点检测方程中的自由参数，[0.04，0.06]
img2 = np.float(img1)
#下一步 设置阈值 将角点绘制出来 阈值根据图像进行选择
img[dst>0.001*dst.max()] = [0,0,255]
#图像显示
plt.figure(figsize=(10,8),dpi=100)
plt.xticks([]),plt.yticks([])

#Shi-Tomasi角点检测
corners = cv2.goodFeaturesToTrack(image,maxcorners,qualityLevel,minDistance)
#灰度图像，获取角点数的数目，角点质量水平0-1，最小欧氏距离
#绘制角点
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),2,(0,0,255),-1)

#视频读写
cap = cv2.VideoCapture(视频文件路径)
#获取视频的某些属性
retval = cap.get(propId)
#propId 从0-18的数字 每个数字表示视频的属性)
#0 视频当前位置 1 从0开始索引帧，帧位置 2 视频文件的相对位置，0开始，1结束 3 视频流的帧宽度 4 视频流的帧高度
#5 帧率 6 编解码器四字符代码 7 视频文件的帧
#修改视频的属性信息
cap.set(propId,value) # ,修改后的属性值
#判断图像是否读取成功
isornot = cap.isOpened()
#获取视频的一帧图像
ret,frame = cap.read()
#释放视频对象
cap.release()
#创建视频写入的对象
out = cv2.VideoWriter(filename,fourcc,fps,frameSize)
#保存位置，指定视频编解码器的4字节代码，帧率，帧大小
#设置视频的编解码器，如下所示：
retval = cv2.VideoWriter_fourcc(c1,c2,c3,c4)
   #示例：
#读取视频
#获取图像的属性，并将其转换为整数
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
#创建保存视频的对象，设置编码格式，帧率，图像的宽高等
out = cv2.VideoWriter(filename,fourcc,fps,frame_width,frame_height)
while(True):
    ret,frame = cap.read() #获取视频的每一帧图像
    if ret == True:
        out.write(frame) #将每一帧图像写入到输出文件中
    else:
        break

