for tmp in range(4**cctv_cnt):
    dirs = []
    for i in range(cctv_cnt):
        dirs.append(int(tmp%4))
        tmp /=4
    direct_set.append(dirs)