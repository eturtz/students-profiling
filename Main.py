from youtubesearchpython import VideosSearch
from youtube_search import YoutubeSearch
def main():
    hobbiesAndInterests ={
        1 : "painting",
        2 : "sculpting",
        3 : "lego",
        4 : "photography",
        5 : "music",
        11: "soccer",
        12: "basketball",
        13: "surfing",
        14: "tennis",
        15: "dancing",
        16:  "hiking",
        17: "workout",
        18: "trips",
        19: "walking",
        20: "fishing",
        21: "scouts",
        24 : "Krembo Wings"
    }
    youtubeAddresses=[]
    GetFromYoutube("fishing",2,youtubeAddresses)
def GetFromYoutube(hobby:str, amount:int,youtubeAddresses:list):
    results = YoutubeSearch(hobby, max_results=amount).to_dict()

    for result in results:
        youtubeAddresses.append("https://www.youtube.com/"+result["url_suffix"])

    print(youtubeAddresses)
if __name__ == '__main__':
    main()