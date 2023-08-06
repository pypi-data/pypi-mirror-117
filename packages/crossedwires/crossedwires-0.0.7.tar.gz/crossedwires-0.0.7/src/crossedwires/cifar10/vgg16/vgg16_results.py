import crossedwires
from pathlib import Path
from crossedwires.base_class import ModelWeightDataset

# import torchvision.models as models
from cross_framework_hpo.vgg16.updated_torchvision_vgg import vgg16
import tensorflow as tf
from os.path import exists


class VGG16Dataset(ModelWeightDataset):
    # inheriting from base class, specialized to VGG
    def __init__(self, filename="vgg_cifar10_wandb_export.csv", num_spaces_searched=16):
        super().__init__(filename, num_spaces_searched)
        self.baseline_url = (
            "https://storage.googleapis.com/crossed-wires-dataset/cifar10/vgg_lambda"
        )

    def trial_lookup(self, epochs, learning_rate, batch_size, adam_epsilon) -> list:
        # returns the name(s) of the trial which fits those criteria
        df = self.wandb_dataframe
        # filter the dataframe based off the attributes selected
        df = df[df["epochs"] == epochs]
        df = df[df["learning_rate"] == learning_rate]
        df = df[df["batch_size"] == batch_size]
        df = df[df["adam_epsilon"] == adam_epsilon]
        return list(df.Name)

    def get_pytorch_weights(self, trial_name):
        weights = ModelWeightDataset.get_pytorch_weights(self, "vgg_lambda", trial_name)
        return weights

    def get_tensorflow_weights(self, trial_name):
        ModelWeightDataset.get_tensorflow_weights(self, "vgg_lambda", trial_name)
        return

    def get_pytorch_model(self, trial_name):
        """Returns pretrained torch model in eval mode"""
        # define the pytorch model - NOTE THAT THIS IS A CUSTOM MODEL
        model = vgg16(pretrained=False, num_classes=10)
        weights = self.get_pytorch_weights(trial_name)
        model.load_state_dict(weights)
        model.eval()
        return model

    def get_tensorflow_model(self, trial_name):
        """Returns tensorflow model"""
        weights_file_name = "/tmp/{}_{}tf_model/".format("vgg_lambda", trial_name)
        if not exists(weights_file_name):
            self.get_tensorflow_weights(trial_name)
        model = tf.keras.models.load_model(weights_file_name)
        return model
