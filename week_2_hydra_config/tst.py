import hydra
from omegaconf import OmegaConf

@hydra.main(config_name="config.yaml")
def main(cfg):
    # Print the config file using `to_yaml` method which prints in a pretty manner
    print(OmegaConf.to_yaml(cfg))
    print(cfg.preferences.user)
    log.info("Info level message")
    log.debug("Debug level message")

if __name__ == "__main__":
    main()

# from hydra import initialize, compose
# from omegaconf import OmegaConf

# initialize(".")  # Assume the configuration file is in the current folder
# cfg = compose(config_name="config.yaml")
# print(OmegaConf.to_yaml(cfg))