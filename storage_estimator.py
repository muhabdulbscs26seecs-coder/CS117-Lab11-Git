def estimate(num_files, size_mb):
    """Return total storage in MB."""
    return num_files * size_mb


n = int(input("Number of files: "))
s = float(input("Average size (MB): "))
print("Total MB:", estimate(n, s))
