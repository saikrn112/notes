* clear application_support

### docker clean
docker system prune

### clear vscode cache
```
rm -rf ~/Library/Application\ Support/Code/Cache/*
rm -rf ~/Library/Application\ Support/Code/CachedData/*
```

### conda clean
conda clean --all

### mac purgeable data
https://appletoolbox.com/how-to-manage-or-delete-purgeable-storage-on-your-mac/

### mac check swap file
```
sudo fs_usage | grep swapfile
```