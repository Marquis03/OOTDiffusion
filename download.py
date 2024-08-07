from modelscope import snapshot_download

model_dir = snapshot_download("Marquis03/OOTDiffusion", cache_dir="./download")
model_dir = snapshot_download(
    "Marquis03/clip-vit-large-patch14", cache_dir="./download"
)
