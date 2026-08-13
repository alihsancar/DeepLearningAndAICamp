import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

NUM_WORKERS = 0
def create_data(
                train_dir: str,
                test_dir: str,
                batch_size: int,
                transform: transforms.Compose,
                num_workers=NUM_WORKERS):

    train_data = datasets.ImageFolder(
        root=train_dir,
        transform=transform
    )
    test_data = datasets.ImageFolder(
        root=test_dir,
        transform=transform
    )

    class_names = train_data.classes

    train_dataloader = DataLoader(
        dataset=train_data,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers
    )
    test_dataloader = DataLoader(
        dataset=test_data,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers
    )

    return train_dataloader, test_dataloader, class_names