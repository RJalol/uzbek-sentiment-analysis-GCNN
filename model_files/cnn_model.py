import torch
import torch.nn as nn
import torch.nn.functional as F


class CNN_Basic(nn.Module):
    def __init__(self, args):
        super(CNN_Basic, self).__init__()
        # embedding
        self.embed = nn.Embedding(args.embed_num, args.embed_dim, padding_idx=1)

        # convolution layers: kernel_sizes = [3,4,5]
        kernel_sizes = [3, 4, 5]
        self.convs = nn.ModuleList(
            [nn.Conv2d(1, args.kernel_num, (k, args.embed_dim)) for k in kernel_sizes]
        )

        # fully connected layer
        self.fc = nn.Linear(len(kernel_sizes) * args.kernel_num, args.class_num)

    def forward(self, x, aspect=None):
        x = self.embed(x)               # [batch, seq_len, embed_dim]
        x = x.unsqueeze(1)              # [batch, channel=1, seq_len, embed_dim]

        # apply conv + relu
        conv_outs = [F.relu(conv(x)).squeeze(3) for conv in self.convs]

        # max-pooling
        pooled = [F.max_pool1d(out, out.size(2)).squeeze(2) for out in conv_outs]

        # concatenate
        cat = torch.cat(pooled, 1)

        # classification
        logit = self.fc(cat)
        return logit, None, None
