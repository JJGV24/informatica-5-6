
import time

def main():

    playlist = ["Boston","Dracula","I Knew It, I Knew You", "i hate that i made you love me", "Risk It All"]
    playlist.append("Be By You")

    playlist.insert(0,"Bohemian Rhapsody")

    playlist.pop(4)


    print(playlist.index("Risk It All"))
    print("Number of songsin playlist:", len(playlist))

    playlist.reverse()
    print(playlist)
    playlist.sort()
    print(playlist)

    #challenge
    repeat = len(playlist)
    while repeat > 0:
        print(playlist)
        song = playlist[0]
        playlist.pop(0)
        playlist.append(song)
        repeat -= 1
        time.sleep(2)


if __name__=="__main__":
    main()
