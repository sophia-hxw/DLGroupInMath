import cv2
import time 
# 通过路径读取视频的指定帧
def get_video(video_path, png_path, zhen_num=1):
    '''
    video_path：视频文件路径
    png_path：截取图片储存路径
    zhen_num：指定截取视频的第几帧
    '''
    vidcap = cv2.VideoCapture(video_path)
    # 获取帧数
    zhen_count = vidcap.get(7)
    
    if zhen_num > zhen_count:
        zhen_num = 1
    
    print(f"zhen_count = {zhen_count} | last zhen_num = {zhen_num}")
 
    # 获取视频的帧率
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    
    # 获取视频图像的宽和高
    width = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
    
    # 指定帧
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, zhen_num)
    
    # 读取指定帧
    success, image = vidcap.read()
    
    if success:
        # 储存图片
        cv2.imwrite(png_path, image)
    else:
        print("读取失败！")
    # 释放图像读取对象
    vidcap.release()
    
    # 可以按时间保存图片
    #t_str = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())
    #imag = cv2.imwrite("./t_str", image)
    
    # 显示读取对象
    cv2.imshow("img1", image)
    cv2.waitKey(30)
    return image

if __name__=='__main__':
    zhen_num = 15
    video_path = './preview.mp4'
    png_path = f'./test_{zhen_num}.png'
    imag = get_video(video_path, png_path, zhen_num)
    print(imag.shape)
    cv2.imshow("img1", imag)
    cv2.waitKey(10000)