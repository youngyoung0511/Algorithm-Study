
def solution(sizes):
    rotated_sizes=[(min(w,h),max(w,h)) for w,h in sizes]

    max_width=max(size[0] for size in rotated_sizes)
    max_height=max(size[1] for size in rotated_sizes)

    return max_height*max_width
