import yt_dlp

link = str(input("Enter link: "))

ydl_opts = {'format': 'best', # video format download
            'no_warnings': True, # disable warning log
            'quiet': True # quiet mode
            }

def main():
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            data = ydl.extract_info(link, download=True)
            print(f"Downloading {data['title']}...")
        except Exception:
            return print(Exception)

    print(f"{data['title']} downloaded!")

if __name__ == "__main__":
    main()
