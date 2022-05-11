mvtec_path = "/content/drive/MyDrive/boschanomaly"
# "cait_m48_448" or "deit_base_distilled_patch16_384" is supported.
backbone = "cait_m48_448"
device = "cuda:0"
batch_size = 16 # original 32
nb_epoch = 10 # original 500
learning_rate = 0.001 ## original 2e-4
warmup_epoch = 4
validate_per_epoch = 5 # original 50

clamp = 0.15
clamp_activation = "ATAN"

weight_path = "/content/FastFlow/weight"
result_path = "/content/FastFlow/result"
