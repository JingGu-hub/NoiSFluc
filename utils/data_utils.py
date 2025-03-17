import torch
import numpy as np
import torch.utils.data as data
from torch.utils.data import DataLoader

from utils.trend_season_decom import ts_decom
from utils.utils import build_dataset_pt, build_dataset_uea, flip_label


class TimeDataset(data.Dataset):
    def __init__(self, dataset, target):
        self.dataset = dataset
        # self.dataset = np.expand_dims(self.dataset, 1)
        # print("dataset shape = ", dataset.shape)
        if len(self.dataset.shape) == 2:
            self.dataset = torch.unsqueeze(self.dataset, 1)
        # print("dataset shape = ", self.dataset.shape)
        self.target = target

    def __getitem__(self, index):
        return self.dataset[index], self.target[index], index

    def __len__(self):
        return len(self.target)

def get_dataset(args, is_pretrain=False):
    if args.archive == 'other':
        train_dataset, train_target, test_dataset, test_target, num_classes = build_dataset_pt(args)
    elif args.archive == 'UEA':
        train_dataset, train_target, test_dataset, test_target, num_classes = build_dataset_uea(args)

    # conduct feature enhance
    ts_aug = ts_decom(kernel_size=5, block_size=2, beta=0.01, gama=0.5)
    train_dataset, train_target = ts_aug(torch.from_numpy(train_dataset).type(torch.FloatTensor).cuda(),
                                         torch.from_numpy(train_target).type(torch.FloatTensor).cuda())

    # corrupt label
    if args.noise_flag == True:
        train_target, mask_train_target = flip_label(dataset=train_dataset, target=train_target, ratio=args.label_noise_rate,
                                                     args=args, pattern=args.label_noise_type)
    # supple data to mitigate class imbalance
    if is_pretrain:
        train_dataset, train_target = ts_aug.common_pad(train_dataset, train_target, num_classes)

    # load train_loader
    train_loader = load_loader(args, train_dataset, train_target)
    # load test_loader
    test_loader = load_loader(args, test_dataset, test_target, shuffle=False)

    return train_loader, test_loader, train_dataset, train_target, test_dataset, test_target, num_classes

def load_loader(args, data, target, shuffle=True):
    dataset = TimeDataset(torch.from_numpy(data).type(torch.FloatTensor).cuda(),
                          torch.from_numpy(target).type(torch.LongTensor).cuda())
    loader = DataLoader(dataset, batch_size=args.batch_size, num_workers=args.num_workers, shuffle=shuffle)

    return loader