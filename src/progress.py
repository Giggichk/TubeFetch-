from tqdm import tqdm


pbar = None

def progress_hook(d):
    global pbar
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate') or 0
        downloaded = d.get('downloaded_bytes', 0)

        if pbar is None and total > 0:
            pbar = tqdm(total=total, unit='B', unit_scale=True, desc="Скачивание")

        if pbar:
            pbar.n = downloaded
            pbar.refresh()

    elif d['status'] == 'finished':
        if pbar:
            pbar.close()
            pbar = None
        print("\nSaving a file")