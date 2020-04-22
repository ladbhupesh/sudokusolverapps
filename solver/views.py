from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    if request.method == "POST":
        listel = [
            [request.POST.get('r1c1'), request.POST.get('r1c2'), request.POST.get('r1c3'), request.POST.get('r1c4'),
             request.POST.get('r1c5'), request.POST.get('r1c6'), request.POST.get('r1c7'), request.POST.get('r1c8'),
             request.POST.get('r1c9')],
            [request.POST.get('r2c1'), request.POST.get('r2c2'), request.POST.get('r2c3'), request.POST.get('r2c4'),
             request.POST.get('r2c5'), request.POST.get('r2c6'), request.POST.get('r2c7'), request.POST.get('r2c8'),
             request.POST.get('r2c9')],
            [request.POST.get('r3c1'), request.POST.get('r3c2'), request.POST.get('r3c3'), request.POST.get('r3c4'),
             request.POST.get('r3c5'), request.POST.get('r3c6'), request.POST.get('r3c7'), request.POST.get('r3c8'),
             request.POST.get('r3c9')],
            [request.POST.get('r4c1'), request.POST.get('r4c2'), request.POST.get('r4c3'), request.POST.get('r4c4'),
             request.POST.get('r4c5'), request.POST.get('r4c6'), request.POST.get('r4c7'), request.POST.get('r4c8'),
             request.POST.get('r4c9')],
            [request.POST.get('r5c1'), request.POST.get('r5c2'), request.POST.get('r5c3'), request.POST.get('r5c4'),
             request.POST.get('r5c5'), request.POST.get('r5c6'), request.POST.get('r5c7'), request.POST.get('r5c8'),
             request.POST.get('r5c9')],
            [request.POST.get('r6c1'), request.POST.get('r6c2'), request.POST.get('r6c3'), request.POST.get('r6c4'),
             request.POST.get('r6c5'), request.POST.get('r6c6'), request.POST.get('r6c7'), request.POST.get('r6c8'),
             request.POST.get('r6c9')],
            [request.POST.get('r7c1'), request.POST.get('r7c2'), request.POST.get('r7c3'), request.POST.get('r7c4'),
             request.POST.get('r7c5'), request.POST.get('r7c6'), request.POST.get('r7c7'), request.POST.get('r7c8'),
             request.POST.get('r7c9')],
            [request.POST.get('r8c1'), request.POST.get('r8c2'), request.POST.get('r8c3'), request.POST.get('r8c4'),
             request.POST.get('r8c5'), request.POST.get('r8c6'), request.POST.get('r8c7'), request.POST.get('r8c8'),
             request.POST.get('r8c9')],
            [request.POST.get('r9c1'), request.POST.get('r9c2'), request.POST.get('r9c3'), request.POST.get('r9c4'),
             request.POST.get('r9c5'), request.POST.get('r9c6'), request.POST.get('r9c7'), request.POST.get('r9c8'),
             request.POST.get('r9c9')],
        ]
        is_solve =  False
        anslist = [[int(x) for x in item] for item in listel]
        is_solve = solve_sudoku(anslist)
        if is_solve:
            return render(request, 'results.html', {"anslis": enumerate(anslist)})
        else:
            return HttpResponse("no solution found")
    return render(request, 'index.html')

def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if (arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False
def used_in_row(arr, row, num):
    for i in range(9):
        if (arr[row][i] == num):
            return True
    return False
def used_in_col(arr, col, num):
    for i in range(9):
        if (arr[i][col] == num):
            return True
    return False
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if (arr[i + row][j + col] == num):
                return True
    return False
def check_location_is_safe(arr, row, col, num):
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3,
                                                                                                 col - col % 3, num)
def solve_sudoku(arr):
    l = [0, 0]
    if (not find_empty_location(arr, l)):
        return True
    row = l[0]
    col = l[1]
    for num in range(1, 10):
        if (check_location_is_safe(arr, row, col, num)):
            arr[row][col] = num
            if (solve_sudoku(arr)):
                return True
            arr[row][col] = 0
    return False
