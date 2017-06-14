import os

work_dir = "dilation_front_base/"
if not os.path.exists(work_dir):
    os.mkdir(work_dir)

train_list = "../data/cscapes/train_vlow_data.txt"
train_label = "../data/cscapes/train_vlow_label.txt"

test_list = "/x/vashishtm/data/cityscapes/val_data.txt"
test_label = "/x/vashishtm/data/cityscapes/val_labels.txt"

classes = 19
lr = 0.0001
gpu = 0

weights = "/x/vashishtm/caffemodels/vgg_conv.caffemodel"
caffe_dir = "/home/vashishtm/caffe-dilation/build_master/tools/caffe"

log_file = work_dir + "train.log"

runstring = """python train.py frontend \
--work_dir %s \
--train_image %s \
--train_label %s \
--test_image %s \
--test_label %s \
--train_batch 14 \
--test_batch 2 \
--caffe %s \
--weights %s \
--crop_size 500 \
--classes %s \
--lr %s \
--gpu %s \
--momentum 0.9 2>&1 | tee -a %s""" % (work_dir, train_list, train_label, test_list, test_label,caffe_dir, weights, str(classes), str(lr), str(gpu), log_file)

os.system(runstring)
~                   
