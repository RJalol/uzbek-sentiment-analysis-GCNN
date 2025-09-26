import torch
import torch.nn as nn
import torch.nn.functional as F

class LSTM_Text(nn.Module):
    def __init__(self, args):
        super(LSTM_Text, self).__init__()
        # embedding
        self.embed = nn.Embedding(args.embed_num, args.embed_dim, padding_idx=1)

        # LSTM
        self.lstm = nn.LSTM(
            input_size=args.embed_dim,
            hidden_size=args.lstm_dsz,
            num_layers=args.lstm_nlayers,
            bidirectional=args.lstm_bidirectional,
            batch_first=True
        )

        # chiqish layer
        hidden_dim = args.lstm_dsz * (2 if args.lstm_bidirectional else 1)
        self.dropout = nn.Dropout(0.5)
        self.fc = nn.Linear(hidden_dim, args.class_num)

    def forward(self, feature, aspect):
        # embedding
        x = self.embed(feature)                  # [batch, seq_len, embed_dim]
        lstm_out, _ = self.lstm(x)               # [batch, seq_len, hidden*dir]
        pooled = torch.mean(lstm_out, dim=1)     # [batch, hidden*dir]
        out = self.dropout(pooled)
        logit = self.fc(out)
        return logit, None, None
