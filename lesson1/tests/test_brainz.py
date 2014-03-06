from music_brainz import *

def test_main():
    results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
    #pretty_print(results)
    print len(results['artist'])
    artist_id = results["artist"][1]["id"]
    print "\nARTIST:"
    pretty_print(results["artist"][1])

    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]
    print "\nONE RELEASE:"
    pretty_print(releases[0], indent=2)
    release_titles = [r["title"] for r in releases]

    print "\nALL TITLES:"
    for t in release_titles:
        print t
