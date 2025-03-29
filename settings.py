OUTPUT_FILE_EXT = "ts"  # cause the format is MPEG-2 TS
FFMPEG_PART_LIST = "PartList.txt"
CONVERT_TO_MP4 = True
MIN_LOG = True
CONVERT_RESOLUTION_TO_360P = False

FILMNAME_STR = "{filmname}"
FILENAME_STR = "{filename}"
FILEEXT_STR = "{fileext}"
OUTPUT_TEMP_DIR = "./downloads/" + FILMNAME_STR + "/TEMP/"
OUTPUT_VIDEO_PATH = "./downloads/" + FILMNAME_STR + "/" + FILMNAME_STR + "." + FILEEXT_STR

# VIDEO_DATA = [ ["film_name", M3U8_URL], ...]
VIDEO_DATA = [
    ["Vtangavor Hyuraxax 2009", "https://hls.armdb.org/file/armdb-hls/videos/25368/p_0.m3u8"],
    ["Transformerner 2 - ynkacneri vrejy", "https://hls.armdb.org/file/armdb-hls/videos/11976/p_1.m3u"],
    ["yerkrord-shans", "https://hls.armdb.org/file/armdb-hls/videos/16440/p_0.m3u8"],
    ["hencock-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/9070/p_1.m3u8"],
    ["aveli-vat-chi-linum-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/14347/p_0.m3u8"],
    ["herkules-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/14551/p_0.m3u8"],
    ["vaghn-amen-inch-ksksvi-norits-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/14830/p_0.m3u8"],
    ["parsic-arqayazne-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/61239/p_1.m3u8"],
    ["13-rd-taghamas-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/8493/p_1.m3u8"],
    ["mexanik-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/10851/p_1.m3u8"],
    ["sarrtse-chanaparhy-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/59899/p_1.m3u8"],
    ["ardar-gorts-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/14177/p_0.m3u8"],
    ["zhamanaki-pahapany-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/14148/p_0.m3u8"],
    ["sevazgest-mardik-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/11818/p_0.m3u8"],
    ["kanach-asepety-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/58737/p_1.m3u8"],
    ["casum-mardkayin-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/58727/p_1.m3u8"],
    ["hrashagortsi-ashakerty-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/9011/p_0.m3u8"],
    ["jumanji-hajord-makardak-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/73357/p_1.m3u8"],
    ["yurayi-darashrjani-zbosaygin-1", "https://hls.armdb.org/file/armdb-hls/videos/33414/p_0.m3u8"],
    ["yurayi-darashrjani-zbosaygin-2", "https://hls.armdb.org/file/armdb-hls/videos/32615/p_0.m3u8"],
    ["yurayi-darashrjani-zbosaygin-3-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/34221/p_0.m3u8"],
    ["yuryan-darashrjani-ashkharhy-hayeren", "https://hls.armdb.org/file/armdb-hls/videos/34371/p_0.m3u8"]

    # ["", ""]
]
