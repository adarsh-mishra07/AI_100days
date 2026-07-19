def water(height):
    n=len(height)
    left=0
    right=n-1
    maxx=0
    while left<right:
        area=min(height[left],height[right])*(right-left)
        if area>maxx:
            maxx=area
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return maxx

print(water([1,8,6,2,5,4,8,3,7]))

