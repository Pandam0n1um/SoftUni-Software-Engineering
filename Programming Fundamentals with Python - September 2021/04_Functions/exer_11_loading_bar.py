def loading_bar(progress):
    result = ""
    is_complete = False
    if progress == 10:
        is_complete = True
    progress_left = 10 - progress
    for num in range(progress):
        result += "%"
    for num in range(progress_left):
        result += "."

    if is_complete:
        print("100% Complete!")
        print(f"[{result}]")
    else:
        print(f"{progress}0% [{result}]")
        print("Still loading...")
    return


progress_value = int(input()) // 10

loading_bar(progress_value)
