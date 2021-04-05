import wave
import numpy as np
import matplotlib.pyplot as plt
from python_speech_features import mfcc
from math import cos, sin, sqrt, pi
'''将AI课上学习的知识进行简单的整理,可以识别简单的0-9的单个语音。
基本方法就是利用库函数提取mfcc,然后计算误差矩阵,再利用动态规划计算累积矩阵。
并且限制了匹配路径的范围。具体的技术网上很多,不再细谈。
现有缺点就是输入的语音长度都是1s,如果不固定长度则识别效果变差。
改进思路是提取有效语音部分。但是该部分尚未完全做好,只写了一个原形函数,尚未完善。'''

def read_file(file_name):
    with wave.open(file_name, 'r') as file:
        params = file.getparams()
        index1, index2, framerate, nframes = params[:4]
        str_data = file.readframes(nframes)
        wave_data = np.fromstring(str_data, dtype=np.short)
        time = np.arange(0, nframes) * (1.0/framerate)
        return wave_data, time
    return index1, index2


def find_point(data):
    count1, count2 = 0, 0
    for index, val in enumerate(data):
        if count1 < 40:
            count1 = count1+1 if abs(val) > 0.15 else 0
            index1 = index
        if count1 == 40 and count2 < 5:
            count2 = count2+1 if abs(val) < 0.001 else 0
            index2 = index
        if count2 == 5:
            break
    return index1, index2


def select_valid(data):
    start, end = find_point(normalized(data))
    print(start, end)
    return data[start:end]


def normalized(a):
    maximum = max(a)
    minimum = min(a)
    return a/maximum


def compute_mfcc_coff(file_prefix=''):
    mfcc_feats = []
    s = range(10)
    I = [0, 3, 4, 8]
    II = [5, 7, 9]
    Input = {'': s, 'I': I, 'II': II, 'B': s}
    for index, file_name in enumerate(file_prefix+'{0}.wav'.format(i) for i in Input[file_prefix]):
        data, time = read_file(file_name)
        # data = select_valid(data)
        # if file_prefix=='II':data = select_valid(data)
        mfcc_feat = mfcc(data, 48000)[:75]
        mfcc_feats.append(mfcc_feat)
    t = np.array(mfcc_feats)
    return np.array(mfcc_feats)


def create_dist():
    for i, m_i in enumerate(mfcc_coff_input):  # get the mfcc of input
        for j, m_j in enumerate(mfcc_coff):  # get the mfcc of dataset
            # build the distortion matrix bwtween i wav and j wav
            N = len(mfcc_coff[0])
            distortion_mat = np.array([[0]*len(m_i)
                                      for i in range(N)], dtype=np.double)
            for k1, mfcc1 in enumerate(m_i):
                for k2, mfcc2 in enumerate(m_j):
                    distortion_mat[k1][k2] = sqrt(
                        sum((mfcc1[1:]-mfcc2[1:])**2))
            yield i, j, distortion_mat


def create_Dist():
    for _i, _j, dist in create_dist():
        N = len(dist)
        Dist = np.array([[0]*N for i in range(N)], dtype=np.double)
        Dist[0][0] = dist[0][0]
        for i in range(N):
            for j in range(N):
                if i | j == 0:
                    continue
            pos = [(i-1, j), (i, j-1), (i-1, j-1)]
            Dist[i][j] = dist[i][j] + min(Dist[k1][k2]
                                          for k1, k2 in pos if k1 > -1 and k2 > -1)
        # if _i==0 and _j==1 :print(_i,_j,'\n',Dist,len(Dist[0]),len(Dist[1]))
        yield _i, _j, Dist


def search_path(n):

    comparison = np.array([[0]*10 for i in range(n)], dtype=np.double)
    for _i, _j, Dist in create_Dist():
        N = len(Dist)
        cut_off = 5
        row = [(d, N-1, j)
                for j, d in enumerate(Dist[N-1]) if abs(N-1-j) <= cut_off]
        col = [(d, i, N-1)
                for i, d in enumerate(Dist[:, N-1]) if abs(N-1-i) <= cut_off]
        min_d, min_i, min_j = min(row+col)
        comparison[_i][_j] = min_d
        optimal_path_x, optimal_path_y = [min_i], [min_j]
        while min_i and min_j:
            optimal_path_x.append(min_i)
            optimal_path_y.append(min_j)
            pos = [(min_i-1, min_j), (min_i, min_j-1), (min_i-1, min_j-1)]
            # try:
            min_d, min_i, min_j = min(((Dist[int(k1)][int(k2)], k1, k2) for k1, k2 in pos
                                       if abs(k1-k2) <= cut_off))

        if _i == _j and _i == 4:
            plt.scatter(optimal_path_x[::-1],
                        optimal_path_y[::-1], color='red')
            plt.show()
    return comparison


mfcc_coff_input = []
mfcc_coff = []


def match(pre):
    global mfcc_coff_input
    global mfcc_coff
    mfcc_coff_input = compute_mfcc_coff(pre)
    compare = np.array([[0]*10 for i in range(len(mfcc_coff_input))], dtype=np.double)
    for prefix in ['', 'B']:
        mfcc_coff = compute_mfcc_coff(prefix)
        compare += search_path(len(mfcc_coff_input))
    for l in compare:
         print([int(x) for x in l])
         print(min(((val, index)for index, val in enumerate(l)))[1])
data, time = read_file('8.wav')
match('I')
match('II')
