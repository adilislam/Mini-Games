def main():
    text = open("artists.txt")
    count = 0
    for line in text:
        count += 1
    print("Each of", count, "artists will receieve $" + str(1000000000 / count))

main()