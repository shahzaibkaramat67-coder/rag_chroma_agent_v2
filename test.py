from pathlib import Path

base_dir = Path(__file__).resolve().parent
base_dir3 = Path(__file__).resolve().parent / "document" / "FYP_Blog_Site_Final.pdf"
base_dir1 = Path(__file__).resolve().parent / "Agent"
base_dir2 = Path(__file__).resolve().parent / "Agent2"

base_dir2.mkdir(parents=True, exist_ok=True)

# print("path", Path(__file__).resolve().parent)
print("base_dir", base_dir)
print("base_dir1", base_dir1)
print("base_dir2", base_dir2)
print("base_dir3", base_dir3)
