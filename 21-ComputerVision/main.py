import torch
import setup_data, model_creation, train_test, utils
from torchvision import transforms

def main():
    train_dir = "data/desert101/train"
    test_dir = "data/desert101/test"

    BATCH_SIZE = 32
    HIDDEN_UNITS = 32
    LEARNING_RATE = 0.001
    NUM_EPOCHS = 10

    data_transform = transforms.Compose([
        transforms.Resize(size=(64,64)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(degrees=15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5483, 0.4638, 0.3865],
                             std=[0.2173, 0.2279, 0.2263])
    ])

    train_dataloader, test_dataloader, class_names = setup_data.create_data(
        train_dir=train_dir,
        test_dir=test_dir,
        batch_size=BATCH_SIZE,
        transform=data_transform
    )

    model = model_creation.Desert101Classifier(
        input_shape=3,
        hidden_units=HIDDEN_UNITS,
        output_shape=len(class_names)
    )

    loss_fn = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(
        params=model.parameters(),
        lr=LEARNING_RATE
    )

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    train_test.train(
        model=model,
        train_dataloader=train_dataloader,
        test_dataloader=test_dataloader,
        optimizer=optimizer,
        loss_fn=loss_fn,
        epochs=NUM_EPOCHS,
        device=device,
        accuracy_function=train_test.calculate_accuracy
    )

    utils.save_model(
        model=model,
        target_dir="models",
        model_name="desert_classifier.pth"
    )

if __name__ == "__main__":
    main()