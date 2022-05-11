mvtec_path = "/content/mvtec_anomaly"
# "cait_m48_448" or "deit_base_distilled_patch16_384" is supported.
backbone = "cait_m48_448"
device = "cuda:1"
batch_size = 32
nb_epoch = 7 # original 500
learning_rate = 0.001 ## original 2e-4
warmup_epoch = 2
validate_per_epoch = 50

clamp = 0.15
clamp_activation = "ATAN"

weight_path = "/content/FastFlow/weight"
result_path = "/content/FastFlow/result"
