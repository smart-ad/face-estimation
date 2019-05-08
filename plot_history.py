import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os
import h5py
import nexusformat.nexus as nx


def get_args():
    parser = argparse.ArgumentParser(description="This script shows training graph from history file.")
    parser.add_argument("--input", "-i", type=str, required=True,
                        help="path to input history h5 file")
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    #print(args)
    input_path = args.input
    #print(input_path)
    #df=h5py.File('input_path', 'r')
    #df.to_hdf(path, 'df', mode='w')
    #print(store)
    df = pd.read_hdf(input_path,'history')
    #df=pd.HDFStore('checkpoints_final/weights.78-3.51.hdf5')
    input_dir = os.path.dirname(input_path)
    plt.plot(df["pred_gender_loss"], label="loss (gender)")
    plt.plot(df["pred_age_loss"], label="loss (age)")
    plt.plot(df["val_pred_gender_loss"], label="val_loss (gender)")
    plt.plot(df["val_pred_age_loss"], label="val_loss (age)")
    plt.xlabel("number of epochs")
    plt.ylabel("loss")
    plt.legend()
    plt.savefig(os.path.join(input_dir, "loss.png"))
    plt.cla()

    plt.plot(df["pred_gender_acc"], label="accuracy (gender)")
    plt.plot(df["pred_age_acc"], label="accuracy (age)")
    plt.plot(df["val_pred_gender_acc"], label="val_accuracy (gender)")
    plt.plot(df["val_pred_age_acc"], label="val_accuracy (age)")
    plt.xlabel("number of epochs")
    plt.ylabel("accuracy")
    plt.legend()
    plt.savefig(os.path.join(input_dir, "accuracy.png"))

if __name__ == '__main__':
    main()