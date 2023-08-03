def minimum_demolished_roads(n, m):
    # Calculate the total number of roads when m houses are selected, and they all have direct connections
    total_roads_m_houses = m * (m - 1) // 2

    # Calculate the minimum number of roads to be demolished
    min_demolished_roads = (n * (n - 1) // 2) - total_roads_m_houses
    return min_demolished_roads

def main():
    n = int(input("Enter the number of houses (n): "))
    m = int(input("Enter the size of subset (m): "))

    result = minimum_demolished_roads(n, m)
    print("Minimum number of roads to be demolished:", result)

if __name__ == "__main__":
    main()
