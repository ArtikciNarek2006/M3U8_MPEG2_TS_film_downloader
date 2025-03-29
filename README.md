# Film / Video Downloader

> A tool to download and merge `.m3u8` video files containing `.ts` segments.

## How to Use

### 1. Install `ffmpeg` and Requirements
- For ffmpeg installation see `https://www.ffmpeg.org/`
- Requirements
```sh
pip install -r requirements.txt
```

### 2. Configure `settings.py`

Edit `settings.py` and add the video name and its `.m3u8` URL in `VIDEO_DATA`.\
Example:

```python
VIDEO_DATA = [
    ["video_name", "https://example.com/path/to/playlist.m3u8"]
]
```

### 3. Run the Script

```sh
python3 main.py
```

## Example `.m3u8` File (Check Compatibility)
> The lines starting with # are ignored

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:11
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-PLAYLIST-TYPE:VOD
#EXTINF:11.211200,
p_0_00.ts
#EXTINF:9.609600,
p_0_01.ts
#EXTINF:9.609600,
p_0_02.ts
#EXTINF:9.609600,
p_0_03.ts
#EXT-X-ENDLIST
```

## Notes

- Ensure the `.m3u8` and `.ts` files are publicly accessible and downloadable.

## Troubleshooting

- **Error: 'No such file or directory'**
  - Ensure the `.m3u8` URL is correct and accessible.
- **Corrupt or incomplete video files**
  - Check if all `.ts` segments are downloaded properly.
  - Use `ffmpeg` to manually merge the segments if needed.

