def estimate(num_files, size_mb):
    """Return total storage in MB."""
    return num_files * size_mb


n = int(input("Number of files: "))
s = float(input("Average size (MB): "))
print(f"Total storage needed: {estimate(n, s):.2f} MB")
print(f"Total storage needed: {estimate(n, s) / 1024:.4f} GB")
