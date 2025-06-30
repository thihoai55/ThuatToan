def bubble_sort(arr):
    n = len(arr)
    # Lặp qua tất cả phần tử trong danh sách
    for i in range(n - 1):
        # Duyệt các phần tử chưa được sắp xếp
        for j in range(n - i - 1):
            # Nếu phần tử đứng trước lớn hơn phần tử đứng sau → hoán đổi
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Hoán đổi

# Hàm in danh sách
def print_array(arr):
    print("Danh sách sau khi sắp xếp:", arr)

# Chạy thử
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Danh sách ban đầu:", arr)
    bubble_sort(arr)
    print_array(arr)
