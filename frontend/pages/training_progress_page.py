import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from loguru import logger


def load_data():
    """Load and preprocess the training progress data."""
    file_path = "../public/training_progress.csv"

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        return df

    logger.error(f"File not found: {file_path}")
    return None


def plot_losses(df):
    """Plot training and validation losses over epochs."""
    st.header("Losses Over Epochs")
    st.write(
        "These plots show how the main components of loss (box_loss, obj_loss, cls_loss) "
        "change over the training and validation datasets."
    )

    fig, ax = plt.subplots(3, 1, figsize=(12, 12))

    sns.lineplot(x="epoch", y="train/box_loss", data=df, ax=ax[0], label="Train Box Loss")
    sns.lineplot(x="epoch", y="val/box_loss", data=df, ax=ax[0], label="Val Box Loss")
    ax[0].set_title("Box Loss Over Epochs")
    ax[0].set_xlabel("Epoch")
    ax[0].set_ylabel("Loss")
    ax[0].legend()

    sns.lineplot(x="epoch", y="train/obj_loss", data=df, ax=ax[1], label="Train Obj Loss")
    sns.lineplot(x="epoch", y="val/obj_loss", data=df, ax=ax[1], label="Val Obj Loss")
    ax[1].set_title("Object Loss Over Epochs")
    ax[1].set_xlabel("Epoch")
    ax[1].set_ylabel("Loss")
    ax[1].legend()

    sns.lineplot(x="epoch", y="train/cls_loss", data=df, ax=ax[2], label="Train Cls Loss")
    sns.lineplot(x="epoch", y="val/cls_loss", data=df, ax=ax[2], label="Val Cls Loss")
    ax[2].set_title("Classification Loss Over Epochs")
    ax[2].set_xlabel("Epoch")
    ax[2].set_ylabel("Loss")
    ax[2].legend()

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.4)
    st.pyplot(fig)


def plot_metrics(df):
    """Plot detection metrics over epochs."""
    st.header("Detection Metrics Over Epochs")
    st.write(
        "These plots track the dynamics of the main detection metrics "
        "(precision, recall, mAP_0.5, mAP_0.5:0.95)."
    )

    fig, ax = plt.subplots(2, 1, figsize=(12, 8))

    sns.lineplot(x="epoch", y="metrics/precision", data=df, ax=ax[0], label="Precision")
    sns.lineplot(x="epoch", y="metrics/recall", data=df, ax=ax[0], label="Recall")
    ax[0].set_title("Precision and Recall Over Epochs")
    ax[0].set_xlabel("Epoch")
    ax[0].set_ylabel("Value")
    ax[0].legend()

    sns.lineplot(x="epoch", y="metrics/mAP_0.5", data=df, ax=ax[1], label="mAP@0.5")
    sns.lineplot(x="epoch", y="metrics/mAP_0.5:0.95", data=df, ax=ax[1], label="mAP@0.5:0.95")
    ax[1].set_title("mAP Over Epochs")
    ax[1].set_xlabel("Epoch")
    ax[1].set_ylabel("mAP")
    ax[1].legend()

    best_epoch = df["metrics/mAP_0.5"].idxmax()
    best_map = df["metrics/mAP_0.5"].max()
    ax[1].axvline(x=best_epoch, color="red", linestyle="--", label=f"Best epoch = {best_epoch}")
    ax[1].annotate(
        f"Best epoch = {best_epoch}",
        xy=(best_epoch, best_map),
        xytext=(best_epoch + 1, best_map),
        arrowprops={"facecolor": "black", "shrink": 0.05},
    )

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.4)
    st.pyplot(fig)


def plot_learning_rates(df):
    """Plot learning rates over epochs."""
    st.header("Learning Rates Over Epochs")
    st.write(
        "This plot visualizes how the learning rates (lr0, lr1, lr2) change during training. "
        "In YOLO, they can differ for different layer groups, so it's useful to see how they decrease."
    )

    fig, ax = plt.subplots(figsize=(12, 4))

    sns.lineplot(x="epoch", y="x/lr0", data=df, ax=ax, label="LR0")
    sns.lineplot(x="epoch", y="x/lr1", data=df, ax=ax, label="LR1")
    sns.lineplot(x="epoch", y="x/lr2", data=df, ax=ax, label="LR2")
    ax.set_title("Learning Rates Over Epochs")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Learning Rate")
    ax.legend()

    plt.tight_layout()
    st.pyplot(fig)


st.title("Training Progress YOLOv5")
st.write("Training progress by 28 epochs of model yolov5_weights.pt")

data_frame = load_data()

if not data_frame:
    st.error("No data available to plot.")
else:
    plot_losses(data_frame)
    plot_metrics(data_frame)
    plot_learning_rates(data_frame)
