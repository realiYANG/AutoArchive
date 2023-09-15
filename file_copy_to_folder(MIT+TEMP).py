# author:HeQiang
import os
import shutil

from_path = 'F:\金浅505-8-H2_固井_20220712_原始-何强'
to_path = 'E:/金浅505-8-H2_固井_20220712_wei-1/'

bg_destination = to_path + 'bg'
mit_data_destination = to_path + 'mit24/data'
mit_map_destination = to_path + 'mit24/map'

midk_data_destination = to_path + 'midk/data'
midk_map_destination = to_path + 'midk/map'

pdf_destination = to_path + 'pdf'

temp_data_destination = to_path + 'temp/data'
temp_map_destination = to_path + 'temp/map'

vdl_data_destination = to_path + 'vdl/data'
vdl_map_destination = to_path + 'vdl/map'

yssj_destination = to_path + 'yssj'
yssj_logging_raw_map_destination = to_path + 'yssj/测井原图'
yssj_scale_file_destination = to_path + 'yssj/刻度文件'
yssj_relevant_file_destination = to_path + 'yssj/相关文件'
yssj_data_destination = to_path + 'yssj/原始数据'

if not os.path.exists(bg_destination):
    os.makedirs(bg_destination)
    print(bg_destination)
if not os.path.exists(mit_data_destination):
    os.makedirs(mit_data_destination)
    print(mit_data_destination)
if not os.path.exists(mit_map_destination):
    os.makedirs(mit_map_destination)
    print(mit_map_destination)

if not os.path.exists(midk_data_destination):
    os.makedirs(midk_data_destination)
    print(midk_data_destination)
if not os.path.exists(midk_map_destination):
    os.makedirs(midk_map_destination)
    print(midk_map_destination)

if not os.path.exists(pdf_destination):
    os.makedirs(pdf_destination)
    print(pdf_destination)

if not os.path.exists(temp_data_destination):
    os.makedirs(temp_data_destination)
    print(temp_data_destination)
if not os.path.exists(temp_map_destination):
    os.makedirs(temp_map_destination)
    print(temp_map_destination)

if not os.path.exists(vdl_data_destination):
    os.makedirs(vdl_data_destination)
    print(vdl_data_destination)
if not os.path.exists(vdl_map_destination):
    os.makedirs(vdl_map_destination)
    print(vdl_map_destination)

if not os.path.exists(yssj_destination):
    os.makedirs(yssj_destination)
    print(yssj_destination)
if not os.path.exists(yssj_logging_raw_map_destination):
    os.makedirs(yssj_logging_raw_map_destination)
    print(yssj_logging_raw_map_destination)
if not os.path.exists(yssj_scale_file_destination):
    os.makedirs(yssj_scale_file_destination)
    print(yssj_scale_file_destination)
if not os.path.exists(yssj_relevant_file_destination):
    os.makedirs(yssj_relevant_file_destination)
    print(yssj_relevant_file_destination)
if not os.path.exists(yssj_data_destination):
    os.makedirs(yssj_data_destination)
    print(yssj_data_destination)

bg_names = []
mit_data_names = []
mit_map_names = []
midk_data_names = []
midk_map_names = []
pdf_names = []
temp_data_names = []
temp_map_names = []
vdl_data_names = []
vdl_map_names = []
yssj_names = []
yssj_logging_raw_map_names = []
yssj_scale_file_names = []
yssj_relevant_file_names = []
yssj_data_names = []

for dirName, subDirList, fileList in os.walk(from_path):
    for fname in fileList:
        if os.path.splitext(fname)[1] == '.docx' or os.path.splitext(fname)[1] == '.doc' or os.path.splitext(fname)[
            1] == '.ppt':
            bg_names.append(dirName + '/' + fname)
            print(bg_names)

        if os.path.splitext(fname)[1] == '.exe' or os.path.splitext(fname)[1] == '.zip' or os.path.splitext(fname)[
            1] == '.rar' or os.path.splitext(fname)[
            1] == '.cmi' or os.path.splitext(fname)[1] == '.wvd' or os.path.splitext(fname)[1] == '.wvp' or \
                os.path.splitext(fname)[1] == '.gds':
            mit_data_names.append(dirName + '/' + fname)
            print(mit_data_names)
        if os.path.splitext(fname)[1] == '.jpg' or os.path.splitext(fname)[1] == '.bmp':
            mit_map_names.append(dirName + '/' + fname)
            print(mit_map_names)

        if os.path.splitext(fname)[1] == '.mdk' or os.path.splitext(fname)[1] == '.MDK' or os.path.splitext(fname)[
            1] == '.las' or os.path.splitext(fname)[1] == '.LAS':
            midk_data_names.append(dirName + '/' + fname)
            print(midk_data_names)
        if os.path.splitext(fname)[1] == '.jpg' or os.path.splitext(fname)[1] == '.bmp':
            midk_map_names.append(dirName + '/' + fname)
            print(midk_map_names)

        if os.path.splitext(fname)[1] == '.pdf':
            pdf_names.append(dirName + '/' + fname)
            print(pdf_names)

        if os.path.splitext(fname)[1] == '.exe' or os.path.splitext(fname)[1] == '.zip' or os.path.splitext(fname)[
            1] == '.rar' or os.path.splitext(fname)[
            1] == '.gds':
            temp_data_names.append(dirName + '/' + fname)
            print(temp_data_names)
        if os.path.splitext(fname)[1] == '.jpg' or os.path.splitext(fname)[1] == '.bmp':
            temp_map_names.append(dirName + '/' + fname)
            print(temp_map_names)

        if os.path.splitext(fname)[1] == '.exe' or os.path.splitext(fname)[1] == '.zip' or os.path.splitext(fname)[
            1] == '.rar' or os.path.splitext(fname)[1] == '.gds' or os.path.splitext(fname)[1] == '.716' or \
                os.path.splitext(fname)[1] == '.wis' or os.path.splitext(fname)[1] == '.txt' or os.path.splitext(fname)[
            1] == '.list':
            vdl_data_names.append(dirName + '/' + fname)
            print(vdl_data_names)
        if os.path.splitext(fname)[1] == '.jpg' or os.path.splitext(fname)[1] == '.bmp':
            vdl_map_names.append(dirName + '/' + fname)
            print(vdl_map_names)

        if os.path.splitext(fname)[1] == '.docx' or os.path.splitext(fname)[1] == '.doc':  # splitext写入的文件后缀
            yssj_names.append(dirName + '/' + fname)
            print(yssj_names)
        if os.path.splitext(fname)[1] == '.pdf' or os.path.splitext(fname)[1] == '.PDF':  # splitext写入的文件后缀
            yssj_logging_raw_map_names.append(dirName + '/' + fname)
            print(yssj_logging_raw_map_names)
        if os.path.splitext(fname)[1] == '.24F' or os.path.splitext(fname)[1] == '.60F' or os.path.splitext(fname)[
            1] == '.meta' or os.path.splitext(fname)[1] == '.META' or os.path.splitext(fname)[1] == '.cvi' or \
                os.path.splitext(fname)[1] == '.CVI' or os.path.splitext(fname)[1] == '.cali' or \
                os.path.splitext(fname)[1] == '.CALI':  # splitext写入的文件后缀
            yssj_scale_file_names.append(dirName + '/' + fname)
            print(yssj_scale_file_names)
        if os.path.splitext(fname)[1] == '.docx' or os.path.splitext(fname)[1] == '.doc' or os.path.splitext(fname)[
            1] == '.xlsx' or os.path.splitext(fname)[1] == '.xls' or os.path.splitext(fname)[1] == '.zip' or \
                os.path.splitext(fname)[1] == '.rar' or os.path.splitext(fname)[1] == '.png' or os.path.splitext(fname)[
            1] == '.pdf':
            yssj_relevant_file_names.append(dirName + '/' + fname)
            print(yssj_relevant_file_names)
        if os.path.splitext(fname)[1] == '.db' or os.path.splitext(fname)[1] == '.mdk' or os.path.splitext(fname)[
            1] == '.zip' or os.path.splitext(fname)[
            1] == '.rar' or os.path.splitext(fname)[1] == '.aff' or os.path.splitext(fname)[1] == '.xtf' or \
                os.path.splitext(fname)[
                    1] == '.CBL' or os.path.splitext(fname)[1] == '.DAT' or os.path.splitext(fname)[1] == '.ORI':
            yssj_data_names.append(dirName + '/' + fname)
            print(yssj_data_names)

for item in bg_names:
    print(item)
    if os.path.splitext(item)[1] == '.docx' and '解释成果报告' in os.path.splitext(item)[0]:
        shutil.copy(item, bg_destination)


    elif os.path.splitext(item)[1] == '.doc' and '解释成果报告' in os.path.splitext(item)[0]:
        shutil.copy(item, bg_destination)
    elif os.path.splitext(item)[1] == '.docx' and '固井质量测井评价报告' in os.path.splitext(item)[0]:
        shutil.copy(item, bg_destination)
    elif os.path.splitext(item)[1] == '.doc' and '固井质量测井评价报告' in os.path.splitext(item)[0]:
        shutil.copy(item, bg_destination)
    elif os.path.splitext(item)[1] == '.docx' and '上井解释登记卡' in os.path.splitext(item)[0]:
        shutil.copy(item, bg_destination)
    elif os.path.splitext(item)[1] == '.doc' and '上井解释登记卡' in os.path.splitext(item)[0]:
        shutil.copy(item, bg_destination)
    elif os.path.splitext(item)[1] == '.ppt' and '汇报' in os.path.splitext(item)[0]:
        shutil.copy(item, bg_destination)
    elif os.path.splitext(item)[1] == '.ppt' and '方案' in os.path.splitext(item)[0]:
        shutil.copy(item, bg_destination)

for item in mit_data_names:
    print(item)
    if os.path.splitext(item)[1] == '.exe' and '井径' in os.path.splitext(item)[0] and '井温' not in \
            os.path.splitext(item)[0] and '固井质量' not in os.path.splitext(item)[0]:
        shutil.copy(item, mit_data_destination)
    if os.path.splitext(item)[1] == '.zip' and '井径' in os.path.splitext(item)[0] and '井温' not in \
            os.path.splitext(item)[0] and '固井质量' not in os.path.splitext(item)[0]:
        shutil.copy(item, mit_data_destination)
    if os.path.splitext(item)[1] == '.rar' and '井径' in os.path.splitext(item)[0] and '井温' not in \
            os.path.splitext(item)[0] and '固井质量' not in os.path.splitext(item)[0]:
        shutil.copy(item, mit_data_destination)
    if os.path.splitext(item)[1] == '.gds' and '井径' in os.path.splitext(item)[0] and '井温' not in \
            os.path.splitext(item)[0] and '固井质量' not in os.path.splitext(item)[0]:
        shutil.copy(item, mit_data_destination)
    if os.path.splitext(item)[1] == '.cmi' and '井径' in os.path.splitext(item)[0]:
        shutil.copy(item, mit_data_destination)
    if os.path.splitext(item)[1] == '.wvd' and '井径' in os.path.splitext(item)[0]:
        shutil.copy(item, mit_data_destination)
    if os.path.splitext(item)[1] == '.wvp' and '井径' in os.path.splitext(item)[0]:
        shutil.copy(item, mit_data_destination)
for item in mit_map_names:
    print(item)
    if os.path.splitext(item)[1] == '.jpg' and '井径' in os.path.splitext(item)[0] and '井温' not in \
            os.path.splitext(item)[0] and '固井质量' not in os.path.splitext(item)[0] and '电磁探伤' not in \
            os.path.splitext(item)[0]:
        shutil.copy(item, mit_map_destination)
    if os.path.splitext(item)[1] == '.bmp' and '井径' in os.path.splitext(item)[0] and '井温' not in \
            os.path.splitext(item)[0] and '固井质量' not in os.path.splitext(item)[0] and '电磁探伤' not in \
            os.path.splitext(item)[0]:
        shutil.copy(item, mit_map_destination)

for item in midk_data_names:
    print(item)
    if os.path.splitext(item)[1] == '.LAS' and '电磁探伤' in os.path.splitext(item)[0]:
        shutil.copy(item, midk_data_destination)
    elif os.path.splitext(item)[1] == '.las' and '电磁探伤' in os.path.splitext(item)[0]:
        shutil.copy(item, midk_data_destination)
    elif os.path.splitext(item)[1] == '.mdk' and '电磁探伤' in os.path.splitext(item)[0]:
        shutil.copy(item, midk_data_destination)
    elif os.path.splitext(item)[1] == '.MDK' and '电磁探伤' in os.path.splitext(item)[0]:
        shutil.copy(item, midk_data_destination)
for item in midk_map_names:
    print(item)
    if os.path.splitext(item)[1] == '.jpg' and '电磁探伤' in os.path.splitext(item)[0]:
        shutil.copy(item, midk_map_destination)
    if os.path.splitext(item)[1] == '.bmp' and '电磁探伤' in os.path.splitext(item)[0]:
        shutil.copy(item, midk_map_destination)

for item in pdf_names:
    print(item)
    if os.path.splitext(item)[1] == '.pdf' and '解释成果报告' in os.path.splitext(item)[0]:
        shutil.copy(item, pdf_destination)
    if os.path.splitext(item)[1] == '.pdf' and '固井质量测井评价报告' in os.path.splitext(item)[0]:
        shutil.copy(item, pdf_destination)
    if os.path.splitext(item)[1] == '.pdf' and '井径' in os.path.splitext(item)[0]:
        shutil.copy(item, pdf_destination)
    if os.path.splitext(item)[1] == '.pdf' and '电磁探伤' in os.path.splitext(item)[0]:
        shutil.copy(item, pdf_destination)
    if os.path.splitext(item)[1] == '.pdf' and '井温' in os.path.splitext(item)[0]:
        shutil.copy(item, pdf_destination)
    if os.path.splitext(item)[1] == '.pdf' and '固井质量' in os.path.splitext(item)[0]:
        shutil.copy(item, pdf_destination)
    if os.path.splitext(item)[1] == '.pdf' and '水泥胶结评价图' in os.path.splitext(item)[0]:
        shutil.copy(item, pdf_destination)

for item in temp_data_names:
    print(item)
    if os.path.splitext(item)[1] == '.exe' and '井温' in os.path.splitext(item)[0]:
        shutil.copy(item, temp_data_destination)
    elif os.path.splitext(item)[1] == '.zip' and '井温' in os.path.splitext(item)[0]:
        shutil.copy(item, temp_data_destination)
    elif os.path.splitext(item)[1] == '.rar' and '井温' in os.path.splitext(item)[0]:
        shutil.copy(item, temp_data_destination)
    elif os.path.splitext(item)[1] == '.gds' and '井温' in os.path.splitext(item)[0]:
        shutil.copy(item, temp_data_destination)
for item in temp_map_names:
    print(item)
    if os.path.splitext(item)[1] == '.jpg' and '井温' in os.path.splitext(item)[0]:
        shutil.copy(item, temp_map_destination)
    if os.path.splitext(item)[1] == '.bmp' and '井温' in os.path.splitext(item)[0]:
        shutil.copy(item, temp_map_destination)

for item in vdl_data_names:
    print(item)
    if os.path.splitext(item)[1] == '.exe' and '固井质量' in os.path.splitext(item)[0]:
        shutil.copy(item, vdl_data_destination)
    elif os.path.splitext(item)[1] == '.zip' and '固井质量' in os.path.splitext(item)[0]:
        shutil.copy(item, vdl_data_destination)
    elif os.path.splitext(item)[1] == '.rar' and '固井质量' in os.path.splitext(item)[0]:
        shutil.copy(item, vdl_data_destination)
    elif os.path.splitext(item)[1] == '.gds' and '固井质量' in os.path.splitext(item)[0]:
        shutil.copy(item, vdl_data_destination)
    elif os.path.splitext(item)[1] == '.716' and '固井质量' in os.path.splitext(item)[0]:
        shutil.copy(item, vdl_data_destination)
    elif os.path.splitext(item)[1] == '.wis' and '固井质量' in os.path.splitext(item)[0]:
        shutil.copy(item, vdl_data_destination)
    elif os.path.splitext(item)[1] == '.txt' and '固井质量' in os.path.splitext(item)[0]:
        shutil.copy(item, vdl_data_destination)
    elif os.path.splitext(item)[1] == '.list' and '固井质量' in os.path.splitext(item)[0]:
        shutil.copy(item, vdl_data_destination)
for item in vdl_map_names:
    print(item)
    if os.path.splitext(item)[1] == '.jpg' and '固井质量' in os.path.splitext(item)[0]:
        shutil.copy(item, vdl_map_destination)
    if os.path.splitext(item)[1] == '.bmp' and '固井质量' in os.path.splitext(item)[0]:
        shutil.copy(item, vdl_map_destination)
    if os.path.splitext(item)[1] == '.jpg' and '水泥胶结评价图' in os.path.splitext(item)[0]:
        shutil.copy(item, vdl_map_destination)
    if os.path.splitext(item)[1] == '.bmp' and '水泥胶结评价图' in os.path.splitext(item)[0]:
        shutil.copy(item, vdl_map_destination)

for item in yssj_names:
    print(item)
    if os.path.splitext(item)[1] == '.docx' and '测井数据文件清单' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_destination)
    if os.path.splitext(item)[1] == '.doc' and '测井数据文件清单' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_destination)
for item in yssj_logging_raw_map_names:
    print(item)
    if os.path.splitext(item)[1] == '.pdf' and 'MIT' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.PDF' and 'MIT' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.pdf' and 'mit' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.PDF' and 'mit' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.pdf' and 'MID-K' in os.path.splitext(item)[0] and '电磁探伤' not in \
            os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.PDF' and 'MID-K' in os.path.splitext(item)[0] and '电磁探伤' not in \
            os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.pdf' and 'mid-k' in os.path.splitext(item)[0] and '电磁探伤' not in \
            os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.PDF' and 'mid-k' in os.path.splitext(item)[0] and '电磁探伤' not in \
            os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.pdf' and 'RBT' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.PDF' and 'RBT' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.pdf' and 'rbt' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.PDF' and 'rbt' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.pdf' and 'VDL' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.PDF' and 'VDL' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.pdf' and 'vdl' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
    if os.path.splitext(item)[1] == '.PDF' and 'vdl' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_logging_raw_map_destination)
for item in yssj_scale_file_names:
    print(item)
    if os.path.splitext(item)[1] == '.24F' or os.path.splitext(item)[1] == '.60F' or os.path.splitext(item)[
        1] == '.meta' or os.path.splitext(item)[1] == '.META' or os.path.splitext(item)[1] == '.cvi' or \
            os.path.splitext(item)[1] == '.CVI' or os.path.splitext(item)[1] == '.cali' or \
            os.path.splitext(item)[1] == '.CALI':
        shutil.copy(item, yssj_scale_file_destination)
for item in yssj_relevant_file_names:
    print(item)
    if os.path.splitext(item)[1] == '.docx' and '设计' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_relevant_file_destination)
    if os.path.splitext(item)[1] == '.doc' and '设计' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_relevant_file_destination)
    if os.path.splitext(item)[1] == '.docx' and '原始资料收集登记表' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_relevant_file_destination)
    if os.path.splitext(item)[1] == '.doc' and '原始资料收集登记表' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_relevant_file_destination)
    if os.path.splitext(item)[1] == '.pdf' and '设计' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_relevant_file_destination)
    if os.path.splitext(item)[1] == '.pdf' and '井史' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_relevant_file_destination)
    if os.path.splitext(item)[1] == '.docx' and '连续油管' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_relevant_file_destination)
    if os.path.splitext(item)[1] == '.doc' and '连续油管' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_relevant_file_destination)
    if os.path.splitext(item)[1] == '.xlsx' and '套管' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_relevant_file_destination)
    if os.path.splitext(item)[1] == '.xls' and '套管' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_relevant_file_destination)

for item in yssj_data_names:
    print(item)
    # 多臂井径
    if os.path.splitext(item)[1] == '.db' and '验证' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.db' and '主测' in os.path.splitext(item)[0] and '套损' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.db' and '重复' in os.path.splitext(item)[0] and '套损' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    # 对压缩文件
    if os.path.splitext(item)[1] == '.zip' and 'mit' in os.path.splitext(item)[0] and '套损' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.zip' and 'MIT' in os.path.splitext(item)[0] and '套损' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.zip' and 'mid-k' in os.path.splitext(item)[0] and '套损' in os.path.splitext(item)[
        0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.zip' and 'MID-K' in os.path.splitext(item)[0] and '套损' in os.path.splitext(item)[
        0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.zip' and 'rbt' in os.path.splitext(item)[0] and '固井' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.zip' and 'RBT' in os.path.splitext(item)[0] and '固井' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.rar' and 'mit' in os.path.splitext(item)[0] and '套损' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.rar' and 'MIT' in os.path.splitext(item)[0] and '套损' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.rar' and 'mid-k' in os.path.splitext(item)[0] and '套损' in os.path.splitext(item)[
        0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.rar' and 'MID-K' in os.path.splitext(item)[0] and '套损' in os.path.splitext(item)[
        0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.rar' and 'rbt' in os.path.splitext(item)[0] and '固井' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.rar' and 'RBT' in os.path.splitext(item)[0] and '固井' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    # 对磁测井
    if os.path.splitext(item)[1] == '.MDK' and '主测' in os.path.splitext(item)[0] and '套损' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.MDK' and '重复' in os.path.splitext(item)[0] and '套损' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.mdk' and '主测' in os.path.splitext(item)[0] and '套损' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.mdk' and '重复' in os.path.splitext(item)[0] and '套损' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    # 对固井水泥胶结
    if os.path.splitext(item)[1] == '.aff' and '主测' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.aff' and '重复' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.xtf' and '主测' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.xtf' and '重复' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.CBL' and '主测' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.DAT' and '主测' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.ORI' and '主测' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.CBL' and '重复' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.DAT' and '重复' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
    if os.path.splitext(item)[1] == '.ORI' and '重复' in os.path.splitext(item)[0]:
        shutil.copy(item, yssj_data_destination)
