def normalize(items: RatedItem[]):
    sorted_songs = []
    for insert_song in all_songs:
        ind = 0
        for song in sorted_songs:
            if insert_song.user_rating < song.user_rating:
                sorted_songs.insert(ind,insert_song)
                break
            ind += 1

    # Find sample standard deviation
    # Shift full distribution to a mean of 5.5
    # Multiply their distance from the mean by ???