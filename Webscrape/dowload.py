from bing_image_downloader import downloader
downloader.download("termometro+digital", limit=220,  output_dir='dataset', 
                    adult_filter_off=True, force_replace=False, timeout=60)
